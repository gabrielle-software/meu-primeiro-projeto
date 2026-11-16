# Meu Primeiro Projeto — Portfólio de Engenharia de Software

Repositório com projetos práticos desenvolvidos durante meus estudos de Engenharia de Software. Cada projeto é apresentado de acordo com o código e os recursos realmente disponíveis.

## Projeto disponível

### Sistema de Gerenciamento de Clientes (Python)

Aplicação de linha de comando para praticar lógica de programação, funções, estruturas de dados e persistência de informações em arquivo JSON.

**Funcionalidades**
- Cadastrar clientes com nome e contato opcional.
- Listar os clientes cadastrados.
- Validar o preenchimento do nome.
- Salvar e carregar os registros em um arquivo JSON.
- Tratar situações em que o arquivo ainda não existe ou contém JSON inválido.

**Tecnologias**
- Python 3
- JSON
- `pathlib` para localizar e manipular o arquivo de dados
- Git e GitHub para versionamento

## Como executar

**Pré-requisito:** Python 3 instalado.

1. Clone o repositório:

```bash
git clone https://github.com/gabrielle-software/meu-primeiro-projeto.git
```

2. Entre na pasta:

```bash
cd meu-primeiro-projeto
```

3. Execute a aplicação:

```bash
python main.py
```

No Windows, também é possível usar `py main.py`. Em alguns sistemas Linux, use `python3 main.py`.

## Armazenamento e privacidade

Os registros são armazenados localmente no arquivo `customers.json), criado automaticamente quando um cliente é cadastrado. Esse arquivo está listado no `.gitignore` para evitar o envio acidental de dados locais ao GitHub.

**Importante:** este projeto é demonstrativo. Não utilize dados pessoais ou informações reais/sensíveis de clientes.

## Próximas melhorias

- Criar testes automatizados para as funções de cadastro e leitura.
- Permitir editar e excluir registros.
- Melhorar a validação dos dados.
- Desenvolver projetos adicionais e documentá-los quando estiverem implementados.

---

Desenvolvido por **Gabrielle Sousa** como parte dos estudos em Engenharia de Software.

---

# English Version

## First Project — Software Engineering Portfolio

This repository contains practical projects developed during my Software Engineering studies. Each project is documented according to the code and features that are actually available.

## Available Project

### Customer Management System (Python)

A command-line application built to practice programming logic, functions, data structures, and JSON file persistence.

**Features**
- Add customers with a name and optional contact information.
- List saved customers.
- Validate that the customer name is provided.
- Save and load records using a JSON file.
- Handle cases where the data file does not exist or contains invalid JSON.

**Technologies**
- Python 3
- JSON
- `pathlib` for file path handling
- Git and GitHub for version control

## How to Run

**Requirement:** Python 3 installed.

1. Clone the repository:

```bash
git clone https://github.com/gabrielle-software/meu-primeiro-projeto.git
```

2. Open the project directory:

```bash
cd meu-primeiro-projeto
```

3. Run the application:

```bash
python main.py
```

On Windows, you can also use `py main.py`. On some Linux systems, use `python3 main.py`.

## Data Storage and Privacy

Customer records are stored locally in `customers.json), which is automatically created when a customer is added. This file is listed in `.gitignore` to help prevent local data from being accidentally pushed to GitHub.

**Important:** this is a demonstration project. Do not use real or sensitive personal/customer information.

## Planned Improvements

- Add automated tests for customer creation and data loading.
- Support editing and deleting customer records.
- Improve input validation.
- Build and document additional projects as they are implemented.

---

Developed by **Gabrielle Sousa** as part of my Software Engineering studies.
