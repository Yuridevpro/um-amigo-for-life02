# 🐾 A Friend for Life - Plataforma de Adoção de Animais

Sistema web completo para conectar protetores de animais a pessoas interessadas em adoção, facilitando o encontro entre pets e seus futuros lares.

![Status](https://img.shields.io/badge/Status-Pronto%20para%20Deploy-brightgreen)![Versão](https://img.shields.io/badge/Versão-1.0-blue)![Python](https://img.shields.io/badge/Python-3.x-blue)![Django](https://img.shields.io/badge/Django-4.x-darkgreen)![Database](https://img.shields.io/badge/Database-PostgreSQL-blueviolet)

---

## 🚀 Início Rápido (Ambiente de Desenvolvimento)

### 1. Pré-requisitos
- Python 3.x
- Git

### 2. Configuração do Ambiente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/um-amigo-for-life02.git
cd um-amigo-for-life02

# Crie e ative um ambiente virtual
python3 -m venv ambiente_virtual
source ambiente_virtual/bin/activate  # No Windows: ambiente_virtual\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e preencha com as suas chaves. Use o exemplo abaixo:
```ini
# .env
ENVIRONMENT='development'
SECRET_KEY='sua-chave-secreta-django'

# Chaves AWS (Opcional para rodar localmente com SQLite)
AWS_ACCESS_KEY_ID='sua_chave_aws'
AWS_SECRET_ACCESS_KEY='sua_chave_secreta_aws'
AWS_STORAGE_BUCKET_NAME='nome-do-seu-bucket'
AWS_S3_REGION_NAME='us-east-1'
```

### 4. Banco de Dados e Execução
```bash
# Aplique as migrações do banco de dados
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

### 5. Acesso
Abra seu navegador e acesse: **http://127.0.0.1:8000/**

## ✨ Funcionalidades Principais

### 👤 Para Adotantes
- **Busca Avançada:** Filtre pets por localização, espécie e tamanho.
- **Perfis Detalhados:** Veja a história, fotos e características de cada pet.
- **Contato Direto:** Acesse facilmente o contato do protetor (WhatsApp, E-mail).
- **Perfis de Protetores:** Conheça quem está cuidando do animal.

### 💖 Para Protetores
- **Cadastro de Pets:** Adicione animais para adoção com um formulário completo.
- **Galeria de Fotos:** Faça upload de múltiplas imagens para cada pet.
- **Gerenciamento de Perfil:** Edite suas informações e gerencie seus animais cadastrados.
- **Status de Adoção:** Marque seus pets como "Adotado" com um clique.

### ⚙️ Sistema Robusto
- **Autenticação Segura:** Cadastro com confirmação por e-mail e recuperação de senha.
- **Perfis Completos:** Middleware que garante que os usuários preencham seus dados.
- **Armazenamento em Nuvem:** Uso de AWS S3 para escalabilidade e segurança das imagens.
- **Interface Responsiva:** Experiência otimizada para Desktop e Mobile.

## 🎯 Casos de Uso

### 👨‍👩‍👧‍👦 Famílias
- Encontrar o pet ideal que se encaixe no estilo de vida da família (tamanho, temperamento, etc.).
- Conectar-se com protetores locais de forma segura.

### 🐕 Protetores Independentes e ONGs
- Aumentar a visibilidade dos animais resgatados.
- Gerenciar de forma centralizada todos os pets disponíveis para adoção.
- Manter a comunidade atualizada sobre o status de cada animal.

### 📚 Acadêmico (ODS 11)
- O projeto serve como um caso prático de tecnologia aplicada para resolver um problema social urbano, contribuindo para a meta do **ODS 11: Cidades e Comunidades Sustentáveis**.

## 📁 Estrutura do Projeto

```
um-amigo-for-life02/
um-amigo-for-life02/
├── 📄 manage.py                # Utilitário de linha de comando
├── 📜 requirements.txt         # Dependências do projeto
├── 🔑 .env                     # Arquivo de variáveis de ambiente (local)
├── 📦 ambiente_virtual/         # Pasta do ambiente virtual Python
│
├── ⚙️ adote/                   # App de configuração principal do projeto
│   ├── settings.py            # Configurações centrais (BD, Apps, Mídia, etc.)
│   ├── urls.py                # Roteador principal de URLs
│   ├── wsgi.py                # Configuração do servidor WSGI
│   └── asgi.py                # Configuração do servidor ASGI
│
├── ❤️ adotar/                  # App: Funcionalidades de adoção (listagem/busca)
│   ├── views.py               # Lógica para listar e filtrar pets
│   ├── urls.py                # Rotas do app adotar
│   └── templates/
│       └── listar_pets.html
│
├── 🐶 divulgar/                # App: Funcionalidades de cadastro de pets
│   ├── models.py              # Modelos Pet e PetImage
│   ├── views.py               # Lógica para cadastrar e ver pets
│   ├── urls.py                # Rotas do app divulgar
│   ├── admin.py               # Customização do Django Admin
│   └── templates/
│       ├── novo_pet.html
│       └── ver_pet.html
│
├── 🏠 pagina_inicio/           # App: Home page e depoimentos
│   ├── models.py              # Modelo Depoimento
│   ├── views.py               # Lógica da home e depoimentos (AJAX)
│   ├── urls.py                # Rotas do app pagina_inicio
│   └── templates/
│       ├── home.html
│       └── depoimento.html
│
├── 👤 perfil/                  # App: Gerenciamento de perfis de usuário
│   ├── models.py              # Modelo UserProfile
│   ├── views.py               # Lógica para ver/editar perfil, alterar senha, etc.
│   ├── middleware.py          # Middleware para forçar preenchimento do perfil
│   ├── urls.py                # Rotas do app perfil
│   └── templates/
│       ├── meu_perfil.html
│       ├── editar_perfil.html
│       └── ...
│
├── ℹ️ sobre_nos/               # App: Páginas institucionais (estáticas)
│   ├── views.py               # Lógica para renderizar páginas
│   ├── urls.py                # Rotas do app sobre_nos
│   └── templates/
│       ├── quem_somos.html
│       └── ...
│
├── 📱 usuarios/                # App: Autenticação (cadastro, login, etc.)
│   ├── models.py              # Modelos para ativação e reset de senha
│   ├── views.py               # Lógica de cadastro, login, recuperação de senha
│   ├── urls.py                # Rotas do app usuarios
│   └── templates/
│       ├── cadastro.html
│       ├── login.html
│       └── ...
│
└── 🎨 templates/               # Diretório central de templates e arquivos estáticos
    ├── base.html              # Template base para todas as páginas
    ├── admin/                 # Customização do admin
    └── static/                # Arquivos CSS, JS e Imagens
        ├── adotar/
        ├── divulgar/
        ├── perfil/
        └── ...
```

## 🔬 Tecnologias Utilizadas

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, jQuery
- **Banco de Dados:** PostgreSQL (Produção), SQLite (Desenvolvimento)
- **Armazenamento:** Amazon S3
- **Infraestrutura (Produção):** Gunicorn, Nginx

## 🤝 Equipe

**Projeto desenvolvido para a disciplina de Projeto Aplicado Multiplataforma (N705).**

- **Integrante 1:** [Seu Nome Completo]
- **Integrante 2:** [Nome Completo]
- **Integrante 3:** [Nome Completo]
- **Integrante 4:** [Nome Completo]

## 📄 Documentação Completa

Toda a documentação técnica, incluindo requisitos, arquitetura, modelagem de dados e prototipação, está disponível na pasta [`/docs`](./docs/).

---

**Versão:** 1.0 | **Status do Projeto Acadêmico**: ✅ Etapa 1 Concluída
