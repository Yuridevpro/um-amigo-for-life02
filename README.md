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

O cronograma a seguir detalha o plano de 8 semanas para a fase de implementação, testes e validação do sistema, conforme a disciplina N708.

| Semana | Atividades Principais | Entregáveis |
| :--- | :--- | :--- |
| **Semana 1** | **Configuração do Ambiente e Backend (Base):** Configuração do ambiente de produção, setup inicial do Django, criação dos modelos de `usuarios` e `perfil`. | Ambiente de desenvolvimento configurado, repositório Git iniciado, modelos iniciais e migrações. |
| **Semana 2** | **Desenvolvimento do Módulo de Autenticação:** Implementação das views de cadastro, login, logout, confirmação de e-mail e recuperação de senha. | Funcionalidades de autenticação completas e operacionais. |
| **Semana 3** | **Desenvolvimento do Módulo de Perfil:** Implementação das views para criar, visualizar e editar perfis de usuário, incluindo o upload de fotos para o S3. | Gerenciamento de perfil completo. |
| **Semana 4** | **Desenvolvimento do Módulo de Pets:** Implementação do cadastro de novos pets, upload de múltiplas imagens e visualização da página de detalhes do pet. | CRUD básico de pets finalizado. |
| **Semana 5** | **Desenvolvimento do Módulo de Busca e Adoção:** Implementação da listagem e filtragem avançada de pets. | Funcionalidade de busca e listagem completa. |
| **Semana 6** | **Desenvolvimento de Funcionalidades Adicionais:** Implementação do sistema de depoimentos e da página "Sobre Nós". Integração final do frontend. | Todas as funcionalidades principais implementadas. |
| **Semana 7** | **Testes e Validação:** Elaboração e execução do plano de testes (testes unitários e de integração). Correção de bugs e refinamento da UI/UX. | Relatório de testes, bugs corrigidos. |
| **Semana 8** | **Documentação Final e Preparação para Deploy:** Finalização da documentação do código, preparação dos scripts de deploy e apresentação final do projeto. | Documentação finalizada, aplicação pronta para o deploy. |

## 🤝 Equipe e Papéis

**Projeto desenvolvido para a disciplina de Projeto Aplicado Multiplataforma (N705).**

| Nome Completo do Integrante | Papel na Equipe |
| :--- | :--- |
| [Seu Nome Completo] | Gerente de Projeto / Arquiteto de Software |
| [Nome Integrante 2] | Desenvolvedor Backend |
| [Nome Integrante 3] | Desenvolvedor Frontend / UI/UX Designer |
| [Nome Integrante 4] | Analista de QA (Testes) / Documentação |

---

**Versão:** 1.0 | **Status do Projeto Acadêmico**: ✅ Etapa 1 Concluída
