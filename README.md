# 🐾 A Friend for Life - Plataforma de Adoção de Animais

Sistema web completo para conectar protetores de animais a pessoas interessadas em adoção, facilitando o encontro entre pets e seus futuros lares.

## 🚀 Acesso à Plataforma

**Acesse a aplicação em produção no seguinte link:**
### [https://um-amigo-for-life02.onrender.com/](https://um-amigo-for-life02.onrender.com/)

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


EMAIL_HOST = SEU_HOST_EMAIL
EMAIL_HOST_PASSWORD = SEU_APP_EMAILPASSWORD
EMAIL_HOST_USER = SEU_HOST_USER
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DB_HOST = SEU_DB_HOST
DB_NAME = SEU_DB_EMAIL
DB_PASSWORD = SEU_DB_PASSWORD
DB_USER = SEU_DB_USER
```

### 4. Banco de Dados e Execução
```bash
python manage.py makemigrations

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
├── 📄 README.md
├── 📄 manage.py
├── 📜 requirements.txt
├── 🔑 .env
├── 🐍 my_storages.py
├── 📦 ambiente_virtual/
├── ⚙️ adote/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ❤️ adotar/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── listar_pets.html
│
├── 🐶 divulgar/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── novo_pet.html
│       └── ver_pet.html
│
├── 🏠 pagina_inicio/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── depoimento.html
│       └── home.html
│
├── 👤 perfil/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── middleware.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── alterar_senha.html
│       ├── editar_perfil.html
│       ├── meu_perfil.html
│       └── perfil_protetor.html
│
├── ℹ️ sobre_nos/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── politica_privacidade.html
│       ├── quem_somos.html
│       └── termos_servico.html
│
├── 📱 usuarios/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── cadastro.html
│       ├── criar_senha.html
│       ├── email_confirmacao.html
│       ├── email_reset_senha.html
│       ├── esqueceu_senha.html
│       └── login.html
│
├── 📂 media/
│   ├── pet_images/
│   │   └── secondary/
│   └── profile_pics/
│
├── 🎨 templates/
│   ├── base.html
│   ├── admin/
│   │   └── base_site.html
│   └── static/
│       ├── admin/
│       │   └── css/
│       ├── adotar/
│       │   ├── css/
│       │   └── img/
│       ├── base/
│       │   ├── css/
│       │   └── img/
│       ├── divulgar/
│       │   ├── novo_pet/
│       │   └── ver_pet/
│       ├── pagina_inicio/
│       │   ├── depoimento/
│       │   └── home/
│       ├── perfil/
│       │   ├── alterar_senha/
│       │   ├── editar_perfil/
│       │   └── meu_perfil/
│       ├── sobre_nos/
│       │   ├── politica_privacidade/
│       │   ├── quem_somos/
│       │   └── termos_servico/
│       └── usuarios/
│           └── cadastro/
│
└── 📂 docs/
    ├── 📂 requirements/
    │   └── 📄 requirements.md
    ├── 📂 architecture/
    │   └── 📄 architecture.md
    ├── 📂 database/
    │   └── 📄 database_model.md
    ├── 📂 api/
    │   └── 📄 api_specification.md
    └── 📂 prototypes/
        ├── 📄 prototypes.md
        ├── 📂 web/
        │   └── (prototipos web)
        └── 📂 mobile/
            └── (prototipos mobile)        
```

## 🔬 Tecnologias Utilizadas

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, jQuery
- **Banco de Dados:** PostgreSQL (Produção), SQLite (Desenvolvimento)
- **Armazenamento:** Amazon S3
- **Infraestrutura (Produção):** Gunicorn, Nginx


## 🗓️ Cronograma de Desenvolvimento (Etapa 2)

O plano de desenvolvimento para a implementação do sistema está estruturado em um cronograma de **60 dias**, dividido em **4 Sprints** de duas semanas (10 dias úteis) cada, seguindo a metodologia Scrum.

-   **Reuniões:**
    -   **Sprint Planning:** 1º dia de cada Sprint, às 19h.
    -   **Reuniões Diárias (Daily Scrum):** Todos os dias, das 19h às 20h.
    -   **Sprint Review:** Último dia de cada Sprint, às 19h.
    -   **Sprint Retrospective:** Último dia de cada Sprint, às 20h.

---

### **Entregas - Mínimo Produto Viável (MVP)**

#### **1ª Sprint: Estrutura do Projeto e Autenticação**

*   **Configuração do Ambiente e Backend:**
    *   Configurar `settings.py` com variáveis de ambiente (`.env`) para desenvolvimento e produção.
    *   Integrar o armazenamento de mídia com o Amazon S3 utilizando `django-storages` e `boto3`.
    *   Estruturar o banco de dados PostgreSQL e aplicar as migrações iniciais.

*   **Módulo de Autenticação (`usuarios` app):**
    *   Implementar a view `cadastro` para criar instâncias dos models `User` e `UserProfile`.
    *   Desenvolver o fluxo de confirmação por e-mail, utilizando o model `Ativacao` e o serviço SMTP.
    *   Criar a view `logar` e a lógica de recuperação de senha com o model `ResetSenha`.

*   **Deploy Inicial (Homologação):**
    *   Publicar a estrutura base da aplicação em um ambiente de testes para validar a configuração inicial.

#### **2ª Sprint: Funcionalidades Essenciais de Perfil e Pets**

*   **Módulo de Perfil (`perfil` app):**
    *   Desenvolver as views `meu_perfil` e `editar_perfil`, permitindo a visualização e atualização dos dados do `UserProfile`.
    *   Implementar o `ProfileCompleteMiddleware` para garantir que os usuários completem o perfil antes de navegar.

*   **Módulo de Divulgação (`divulgar` app):**
    *   Construir a view `novo_pet` com o formulário para cadastrar instâncias do model `Pet` e `PetImage`, incluindo o upload de múltiplas imagens para o S3.
    *   Desenvolver a view `ver_pet` para exibir os detalhes de um animal e a lógica para marcá-lo como "Adotado".

*   **Deploy Incremental:**
    *   Atualizar o ambiente de homologação com as novas funcionalidades de gerenciamento de perfis e pets.

#### **3ª Sprint: Interação, Busca e Engajamento**

*   **Módulo de Adoção (`adotar` app):**
    *   Implementar a view `listar_pets` com a lógica de filtragem por localização (do `UserProfile`), espécie e tamanho.
    *   Implementar a paginação (`Paginator` do Django) para otimizar o carregamento da lista de pets.

*   **Módulo de Engajamento (`pagina_inicio` app):**
    *   Desenvolver as views para criar e gerenciar o model `Depoimento`.
    *   Implementar a view `mais_depoimentos` com `JsonResponse` para o carregamento dinâmico na `home`.

*   **Reforço de Segurança e Permissões:**
    *   Revisar todas as views críticas (`editar_pet`, `remover_pet`) para garantir que apenas o proprietário do pet possa realizar as ações.

*   **Deploy Incremental:**
    *   Atualizar o ambiente de homologação com as funcionalidades de busca e depoimentos.

#### **4ª Sprint: Validação, Refinamento e Lançamento**

*   **Testes de Aceitação e Validação (E2E):**
    *   Executar testes manuais nos principais fluxos de usuário: 1) Cadastro completo com ativação de e-mail; 2) Login, cadastro de pet e edição; 3) Busca e visualização de um pet para adoção; 4) Recuperação de senha.

*   **Refinamento da Interface (UI/UX):**
    *   Realizar ajustes finos no CSS e nos templates (`base.html` e outros) com base nos testes para garantir a responsividade e a usabilidade em diferentes dispositivos.

*   **Finalização da Documentação Técnica:**
    *   Revisar e completar todos os documentos na pasta `docs/`, incluindo o `README.md`, garantindo que toda a documentação reflita o estado final do código.

*   **Deploy Final em Produção:**
    *   Migrar a aplicação do ambiente de homologação para o ambiente de produção final.
    *   Realizar um teste piloto, convidando alguns usuários para testar a plataforma em um cenário real.
      
**Projeto desenvolvido para a disciplina de Projeto Aplicado Multiplataforma (N705).**

## 🤝 Equipe e Papéis

| Nome | Papel |
| :--- | :--- |
| José Alves Ferreira Neto | Product Owner / Gestão |
| Alan Magalhães Barros | Scrum Master |
| Alisson Rafael Silva de Almeida | Time (Desenvolvimento) |
| Yuri da Silva Ferreira | Time (Desenvolvimento) |
| Kairo César Ferreira Cunha | Time (Desenvolvimento / Testes) |
| Gabriel Nogueira Ibiapina | UX / Documentação |


---

**Versão:** 1.0 | **Status do Projeto Acadêmico**: ✅ Etapa 1 Concluída
