# divulgar/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet, PetImage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def novo_pet(request):
    if request.method == 'POST':
        especie = request.POST.get('especie')
        sexo = request.POST.get('sexo')
        tamanho = request.POST.get('tamanho')
        nome_pet = request.POST.get('nome_pet')
        historia_pet = request.POST.get('historia_pet')
        cuidados = request.POST.getlist('cuidados')
        vive_bem_em = request.POST.getlist('vive_bem_em')
        temperamento = request.POST.getlist('temperamento')
        sociavel_com = request.POST.getlist('sociavel_com')
       

        # Validation
        errors = []
        if not request.FILES.get('foto_principal'):
            errors.append('Foto principal é obrigatória.')
        if not especie:
            errors.append('Espécie é obrigatória.')
        if not sexo:
            errors.append('Sexo é obrigatório.')
        if not tamanho:
            errors.append('Tamanho é obrigatório.')
        if not nome_pet:
            errors.append('Nome do Pet é obrigatório.')
        if not cuidados:
            errors.append('Cuidados são obrigatórios.')
        if not vive_bem_em:
            errors.append('Vive bem em é obrigatório.')
        if not temperamento:
            errors.append('Temperamento é obrigatório.')
        if not sociavel_com:
            errors.append('Sociável com é obrigatório.')
        
        secondary_images = request.FILES.getlist('fotos_secundarias')
        if len(secondary_images) > 5:
            errors.append('Você pode enviar no máximo 5 imagens secundárias.')
        
        if errors:
            return render(request, 'novo_pet.html', {
                'especie': especie,
                'sexo': sexo,
                'tamanho': tamanho,
                'cuidados': cuidados,
                'vive_bem_em': vive_bem_em,
                'temperamento': temperamento,
                'sociavel_com': sociavel_com,
                'nome_pet': nome_pet,
                'historia_pet': historia_pet,
                'errors': errors,
            })

        # Save Pet instance
        pet = Pet(
            especie=especie,
            sexo=sexo,
            tamanho=tamanho,
            nome_pet=nome_pet,
            historia_pet=historia_pet,
            usuario=request.user,
            cuidados=cuidados,
            vive_bem_em=vive_bem_em,
            temperamento=temperamento,
            sociavel_com=sociavel_com,
           
        )
        pet.save()

        # Save Pet Images
        main_image = request.FILES.get('foto_principal')
        if main_image:
            pet.foto_principal = main_image
            pet.save()

        secondary_images = request.FILES.getlist('fotos_secundarias')
        for image in secondary_images[:5]:
            secondary_image = PetImage.objects.create(pet=pet, image=image)
            pet.fotos_secundarias.add(secondary_image)

        messages.success(request, 'Pet cadastrado com sucesso!')
        return redirect(reverse('listar_pets'))

    return render(request, 'novo_pet.html')





def ver_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    
    if request.method == "GET":
        return render(request, 'ver_pet.html', {'pet': pet})

    if request.method == "POST":
        # Verifica se o usuário é o dono do pet
        if pet.usuario != request.user:
            messages.add_message(request, messages.ERROR, 'Esse pet não é seu!')
            return redirect('ver_pet', id=id)

        # Atualiza o status do pet para "Adotado"
        pet.status = 'A'
        pet.save()

        messages.success(request, 'Pet marcado como adotado com sucesso.')
        return redirect('ver_pet', id=id)

# divulgar/views.py (NOVA VIEW ADICIONADA)

# divulgar/views.py (FUNÇÃO editar_pet CORRIGIDA)

# divulgar/views.py (FUNÇÃO editar_pet CORRIGIDA E FINAL)

@login_required
def editar_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if pet.usuario != request.user:
        messages.error(request, 'Você não tem permissão para editar este pet.')
        return redirect('meu_perfil')

    if request.method == "POST":
        # Pega os dados do formulário
        nome_pet = request.POST.get('nome_pet')
        historia_pet = request.POST.get('historia_pet')
        especie = request.POST.get('especie')
        sexo = request.POST.get('sexo')
        tamanho = request.POST.get('tamanho')
        cuidados = request.POST.getlist('cuidados')
        vive_bem_em = request.POST.getlist('vive_bem_em')
        temperamento = request.POST.getlist('temperamento')
        sociavel_com = request.POST.getlist('sociavel_com')
        foto_principal = request.FILES.get('foto_principal')
        remover_foto_principal = request.POST.get('remover_foto_principal')
        
        novas_fotos_secundarias = request.FILES.getlist('fotos_secundarias')
        ids_fotos_remover = request.POST.getlist('remover_fotos_secundarias')

        # --- VALIDAÇÃO CORRIGIDA ---
        errors = []
        if not nome_pet: errors.append('Nome do Pet é obrigatório.')
        if not historia_pet: errors.append('A história do Pet é obrigatória.')
        if not especie: errors.append('Espécie é obrigatória.')
        if not sexo: errors.append('Sexo é obrigatório.')
        if not tamanho: errors.append('Tamanho é obrigatório.')
        if not cuidados: errors.append('Cuidados são obrigatórios.')
        if not vive_bem_em: errors.append('Vive bem em é obrigatório.')
        if not temperamento: errors.append('Temperamento é obrigatório.')
        if not sociavel_com: errors.append('Sociável com é obrigatório.')
        if (not pet.foto_principal or remover_foto_principal) and not foto_principal:
            errors.append('A foto principal é obrigatória. Adicione uma antes de salvar.')

        
        # Validação de contagem de fotos usando a relação correta 'images'
        fotos_existentes_count = pet.images.count()
        fotos_a_remover_count = len(ids_fotos_remover)
        fotos_novas_count = len(novas_fotos_secundarias)
        total_fotos_final = (fotos_existentes_count - fotos_a_remover_count) + fotos_novas_count

        if total_fotos_final > 5:
            errors.append(f'O pet só pode ter no máximo 5 fotos secundárias. Você está tentando salvar com {total_fotos_final}.')

        if errors:
            context = {
                'pet': pet,
                'choices_especie': Pet.choices_especie,
                'choices_sexo': Pet.choices_sexo,
                'choices_tamanho': Pet.choices_tamanho,
                'errors': errors,
            }
            return render(request, 'editar_pet.html', context)
        
        # --- ATUALIZAÇÃO DOS DADOS ---
        pet.nome_pet = nome_pet
        pet.historia_pet = historia_pet
        pet.especie = especie
        pet.sexo = sexo
        pet.tamanho = tamanho
        pet.cuidados = cuidados
        pet.vive_bem_em = vive_bem_em
        pet.temperamento = temperamento
        pet.sociavel_com = sociavel_com

        # --- FOTO PRINCIPAL ---
        if foto_principal:
            pet.foto_principal = foto_principal
        elif remover_foto_principal:
            # Só remove depois da validação
            if pet.foto_principal:
                pet.foto_principal.delete(save=False)
                pet.foto_principal = None

        
        pet.save()

        # 1. Remove as fotos marcadas
        if ids_fotos_remover:
            fotos_remover = PetImage.objects.filter(id__in=ids_fotos_remover, pet=pet)
            for foto in fotos_remover:
                pet.fotos_secundarias.remove(foto)  # remove da ManyToMany
                foto.delete()  # deleta do banco e do S3

        # 2. Adiciona as novas fotos
        for foto in novas_fotos_secundarias:
            nova_foto = PetImage.objects.create(pet=pet, image=foto)
            pet.fotos_secundarias.add(nova_foto)  # adiciona na ManyToMany

        
        messages.success(request, f'As informações de {pet.nome_pet} foram atualizadas com sucesso!')
        return redirect('meu_perfil')
    
    else: # GET request
        context = {
            'pet': pet,
            'choices_especie': Pet.choices_especie,
            'choices_sexo': Pet.choices_sexo,
            'choices_tamanho': Pet.choices_tamanho,
        }
        return render(request, 'editar_pet.html', context)