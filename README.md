# Sistema de Gerenciamento de Usuários com SQLAlchemy

Sistema simples de CRUD (Create, Read, Update, Delete) de usuários utilizando SQLAlchemy e SQLite.

## 📋 Descrição

Esta aplicação permite gerenciar usuários através de um menu interativo no terminal, com as seguintes funcionalidades:

- Adicionar novos usuários
- Listar todos os usuários cadastrados
- Filtrar usuários por idade
- Atualizar informações de usuários existentes
- Remover usuários do banco de dados

## 🚀 Tecnologias

- Python 3.x
- SQLAlchemy (ORM)
- SQLite (Banco de dados)

## 📦 Instalação

### 1. Clone ou baixe o projeto

```bash
cd sqlalchemy
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Como Usar

### Executar a aplicação

```bash
python main.py
```

### Menu de Opções

Ao executar o programa, você verá o seguinte menu:

```
==================================================
SISTEMA USUARIO
1 - Adicionar um usuário
2 - Listar todos usuários
3 - Filtrar por idade
4 - Atualizar um usuário
5 - Remover um usuário
0 - Sair
==================================================
```

### Funcionalidades

#### 1. Adicionar Usuário
- Escolha a opção `1`
- Informe: nome, idade e endereço
- O usuário será cadastrado no banco de dados

#### 2. Listar Todos os Usuários
- Escolha a opção `2`
- Todos os usuários cadastrados serão exibidos

#### 3. Filtrar por Idade
- Escolha a opção `3`
- Informe uma idade mínima
- Serão exibidos usuários com idade superior ao valor informado

#### 4. Atualizar Usuário
- Escolha a opção `4`
- Informe o ID do usuário
- Atualize: nome, idade e endereço

#### 5. Remover Usuário
- Escolha a opção `5`
- Informe o ID do usuário a ser removido

#### 0. Sair
- Encerra a aplicação e fecha a conexão com o banco de dados

## 🗄️ Estrutura do Banco de Dados

### Tabela: usuarios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto incremento) |
| nome | String(50) | Nome do usuário (obrigatório) |
| idade | Integer | Idade do usuário (obrigatório) |
| endereco | String(150) | Endereço (padrão: "Rua das pedras, 10") |
| created_at | DateTime | Data de criação (automático) |
| updated_at | DateTime | Data da última atualização |

## 🔧 Configuração de Outros Bancos de Dados

O projeto está configurado para usar SQLite por padrão. Para usar outros bancos de dados, descomente e configure as linhas apropriadas em [`main.py`](main.py):

### PostgreSQL
```python
engine = create_engine("postgresql+psycopg2://user:password@localhost/dbname")
```

### MySQL
```python
engine = create_engine("mysql+pymysql://user:password@localhost/dbname")
```

## 📁 Estrutura do Projeto

```
sqlalchemy/
│
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências do projeto
├── README.md           # Documentação
├── .gitignore          # Arquivos ignorados pelo Git
└── name.db             # Banco de dados SQLite (gerado automaticamente)
```

## 🎯 Funções Principais

- [`add_user()`](main.py) - Adiciona um novo usuário
- [`list_all()`](main.py) - Lista todos os usuários
- [`filter_idade()`](main.py) - Filtra usuários por idade
- [`uptade_user()`](main.py) - Atualiza dados de um usuário
- [`remove_user()`](main.py) - Remove um usuário
- [`add_many()`](main.py) - Adiciona múltiplos usuários (executado na inicialização)

## ⚠️ Observações

- O banco de dados `name.db` é criado automaticamente na primeira execução
- A função [`add_many()`](main.py) é executada automaticamente e adiciona 5 usuários de exemplo
- Todos os dados são persistidos no arquivo `name.db`
