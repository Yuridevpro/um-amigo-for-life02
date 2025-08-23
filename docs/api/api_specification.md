### **Arquivo: `docs/api/api_specification.md`**
```markdown
# Documento de Especificação de APIs e Interfaces

Este documento descreve as principais interfaces de comunicação e os endpoints (views) da plataforma "A Friend for Life".

### 1. Visão Geral da Comunicação

A plataforma utiliza uma arquitetura de renderização no servidor, onde as "APIs internas" são os endpoints de URL definidos no Django. A comunicação ocorre via requisições HTTP (GET e POST). Adicionalmente, o sistema consome APIs externas.

### 2. Endpoints da Aplicação (APIs Internas)

| Método | Endpoint (URL) | View Responsável | Parâmetros de Requisição | Formato de Resposta | Descrição da Funcionalidade |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GET`/`POST` | `/auth/cadastro/` | `views.cadastro` | Campos do formulário (nome, e-mail, senha, etc.) | HTML | Exibe o formulário (GET) ou processa o registro do novo usuário (POST). |
| `GET`/`POST` | `/auth/login/` | `views.logar` | `email`, `senha` | HTML | Exibe o formulário (GET) ou autentica e inicia a sessão do usuário (POST). |
| `GET`/`POST` | `/auth/esqueceu_senha/` | `views.esqueceu_senha` | `email` | HTML | Exibe o formulário (GET) ou inicia o processo de recuperação de senha (POST). |
| `GET`/`POST` | `/auth/criar_senha/<uidb64>/<token>/`| `views.criar_senha` | `senha_nova`, `confirmar_senha` | HTML | Permite que o usuário defina uma nova senha após a validação do token. |
| `GET` | `/auth/confirmar_email/<uidb64>/<token>/`| `views.confirmar_email`| - | HTML (Redirecionamento)| Ativa a conta do usuário a partir do link de confirmação do e-mail. |
| `GET` | `/perfil/sair/` | `views.sair` | - | HTML (Redirecionamento)| Encerra a sessão do usuário (logout). |
| `GET`/`POST` | `/divulgar/novo_pet/` | `views.novo_pet` | Campos do formulário do pet, `foto_principal`, `fotos_secundarias` | HTML | Exibe o formulário (GET) ou cadastra um novo pet (POST). |
| `GET`/`POST` | `/divulgar/ver_pet/<id>/` | `views.ver_pet` | - | HTML | Exibe os detalhes de um pet (GET) ou marca o pet como adotado (POST). |
| `GET` | `/adotar/listar_pets/` | `views.listar_pets` | Parâmetros de filtro (`estado`, `cidade`, `tamanho`, `especie`, `page`) | HTML | Exibe a lista de pets disponíveis, aplicando os filtros fornecidos. |
| `GET` | `/perfil/meu_perfil/` | `views.meu_perfil` | - | HTML | Exibe o perfil do usuário logado. |
| `GET`/`POST` | `/perfil/editar_perfil/` | `views.editar_perfil` | Campos do formulário de perfil (nome, telefone, etc.) | HTML | Exibe o formulário (GET) ou atualiza os dados do perfil (POST). |
| `GET`/`POST` | `/perfil/alterar_senha/`| `views.alterar_senha`| `senha_atual`, `senha_nova` | HTML | Exibe o formulário (GET) ou processa a alteração de senha (POST). |
| `POST` | `/perfil/remover_conta/`| `views.remover_conta`| - | HTML (Redirecionamento)| Remove a conta do usuário. |
| `GET` | `/mais_depoimentos/` | `views.mais_depoimentos` | `pagina_atual` (query param) | JSON | Retorna uma lista paginada de depoimentos para carregamento dinâmico. |

### 3. Interfaces de Comunicação com Serviços Externos

*   **API de Localidades do IBGE:** Consumida via `GET` para popular formulários de localização. Resposta em JSON.
*   **Serviço de E-mail (SMTP):** Utilizado para enviar e-mails transacionais (confirmação de cadastro, reset de senha).
```

---

### **Arquivo: `docs/prototypes/prototypes.md`**
```markdown
# Documento de Prototipação: A Friend for Life

Este documento detalha o processo de prototipação da interface do usuário (UI) para a plataforma, abrangendo desde os wireframes até os protótipos de alta fidelidade e a validação dos fluxos de usuário.

### 1. Elaboração de Wireframes (Protótipos de Baixa Fidelidade)

A fase inicial consistiu na criação de wireframes para definir a estrutura das seis telas principais do sistema, focando na funcionalidade e na experiência do usuário (UX).

*   **Wireframe 1: Página Inicial (`home.html`)**
    *   **[Blocos]**: Header, Formulário de Filtro, Grid de Pets, Paginação, Seções Informativas, Depoimentos, Footer.

*   **Wireframe 2: Página de Listagem de Pets (`listar_pets.html`)**
    *   **[Blocos]**: Header, Formulário de Filtro, Grid de Pets (área principal), Paginação, Footer.

*   **Wireframe 3: Página de Detalhes do Pet (`ver_pet.html`)**
    *   **[Blocos]**: Header, Galeria de Imagens, Coluna de Informações Essenciais (contato, etc.), Seção de Detalhes, Bloco de História, Botão de Ação, Footer.

*   **Wireframe 4: Página de Cadastro de Usuário (`cadastro.html`)**
    *   **[Blocos]**: Painel Esquerdo com Formulário (Logo, Título, Campos de Input para dados pessoais, localização e senha), Botão "Salvar". Painel Direito com Imagem de branding.

*   **Wireframe 5: Página de Cadastro de Novo Pet (`novo_pet.html`)**
    *   **[Blocos]**: Header, Título da Página ("Novo Pet"), Formulário com Múltiplas Seções (Upload de Imagens, Dados Básicos do pet, Características), Botão de "Cadastrar", Footer.

*   **Wireframe 6: Página de Perfil do Usuário (`meu_perfil.html`)**
    *   **[Blocos]**: Header, Seção de Informações do Perfil (Foto, Nome, Localização, Contadores, Botões de Ação), Seção "Meus Pets" com Grid de Cards, Paginação para os pets, Footer.

### 2. Criação de Protótipos de Interface (Alta Fidelidade)

Após a validação da estrutura, foram desenvolvidos os protótipos de alta fidelidade, aplicando a identidade visual da marca. Os próprios arquivos de template do projeto (`.html` e `.css`) servem como protótipos funcionais.

**Identidade Visual:**
*   **Paleta de Cores:** Combina tons neutros com cores de destaque para ações e informações importantes.
*   **Tipografia:** Fontes claras e legíveis para garantir a boa leitura.
*   **Componentes:** Uso do framework Bootstrap 5 para consistência e responsividade.

**Telas Principais Prototipadas:**
*(Instrução: Insira aqui as capturas de tela das páginas correspondentes do seu projeto em execução para ilustrar os protótipos de alta fidelidade).*

*   **Tela 1: Página Inicial (`home.html`)**
    *   (Inserir captura de tela da página inicial)
*   **Tela 2: Listagem de Pets (`listar_pets.html`)**
    *   (Inserir captura de tela da página de adoção)
*   **Tela 3: Detalhes do Pet (`ver_pet.html`)**
    *   (Inserir captura de tela da página de um pet específico)
*   **Tela 4: Cadastro de Usuário (`cadastro.html`)**
    *   (Inserir captura de tela da página de registro de novo usuário)
*   **Tela 5: Cadastro de Novo Pet (`novo_pet.html`)**
    *   (Inserir captura de tela do formulário de cadastro de pet)
*   **Tela 6: Perfil do Usuário (`meu_perfil.html`)**
    *   (Inserir captura de tela da página de perfil do usuário logado)

### 3. Validação de Fluxos de Usuário

Os protótipos de alta fidelidade foram utilizados para validar os principais fluxos de interação do usuário, garantindo que as jornadas para completar tarefas-chave fossem intuitivas e eficientes.

**Fluxo 1: Jornada de Adoção (Visitante)**

1.  **Início:** O usuário acessa a Página Inicial (`home.html`).
2.  **Ação:** Utiliza o formulário de filtro para buscar por pets com base em sua localização e preferências.
3.  **Resultado:** O sistema exibe a página de listagem (`listar_pets.html`) com os resultados filtrados.
4.  **Ação:** O usuário clica no card de um pet que lhe interessa.
5.  **Resultado:** O sistema exibe a página de detalhes do pet (`ver_pet.html`).
6.  **Ação:** O usuário lê os detalhes e decide entrar em contato, clicando no botão "Adotar".
7.  **Resultado:** Um modal é exibido com as informações de contato do protetor, permitindo que o usuário inicie a comunicação fora da plataforma.
*   **Validação:** O fluxo é considerado validado, pois permite que um visitante encontre um pet e obtenha os meios para contatar o responsável pela adoção de forma clara e direta.

**Fluxo 2: Jornada do Protetor (Do Cadastro ao Anúncio do Pet)**

1.  **Início:** Um novo usuário (protetor) acessa a plataforma e clica em "Cadastre-se".
2.  **Ação:** O usuário preenche o formulário de registro (`cadastro.html`).
3.  **Resultado:** O sistema valida os dados e envia um e-mail de confirmação.
4.  **Ação:** O usuário clica no link de confirmação em seu e-mail e realiza o login.
5.  **Ação:** Já autenticado, clica em "Novo Pet".
6.  **Resultado:** O sistema exibe o formulário de cadastro de pet (`novo_pet.html`).
7.  **Ação:** O usuário preenche todos os campos sobre o animal e faz o upload das imagens.
8.  **Ação:** Clica no botão "Cadastrar".
9.  **Resultado:** O sistema valida os dados, salva o pet, armazena as imagens no S3, exibe uma mensagem de sucesso e redireciona o usuário.
*   **Validação:** O fluxo é considerado validado, pois guia o novo usuário desde a criação da conta até a publicação bem-sucedida de seu primeiro anúncio, com feedback claro em cada etapa.
```
---