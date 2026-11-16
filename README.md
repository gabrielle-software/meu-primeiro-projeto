# Meu Primeiro Projeto — Portfólio de Engenharia de Software

[![Testes automatizados](https://github.com/gabrielle-software/meu-primeiro-projeto/actions/workflows/tests.yml/badge.svg)](https://github.com/gabrielle-software/meu-primeiro-projeto/actions/workflows/tests.yml)

Repositório com projetos práticos desenvolvidos durante meus estudos de Engenharia de Software. Cada projeto é apresentado de acordo com o código e os recursos realmente disponíveis.

## Projeto disponível

### Sistema de Gerenciamento de Clientes (Python)

Aplicação de linha de comando para praticar lógica de programação, funções, estruturas de dados e persistência de informações em arquivo JSON.

**Funcionalidades**
- Cadastrar clientes com nome e contato opcional.
- Listar os clientes cadastrados.
- Editar o nome e/ou contato de um cliente existente.
- Excluir um cliente após confirmação no menu.
- Validar o preenchimento do nome.
- Salvar e carregar os registros em um arquivo JSON.
- Tratar arquivo ausente, JSON inválido e registros malformados.\n- Validar nomes e contatos e remover espaços extras.

**Tecnologias**
- Python 3
- JSON
- `pathlib` para localizar e manipular o arquivo de dados
- `unittest` para testes automatizados
- Git e GitHub para versionamento
- GitHub Actions para integração contínua

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

## Testes automatizados

O projeto possui **20 testes automatizados** com a biblioteca `unittest`. Eles verificam:

1. Retorno de uma lista vazia quando o arquivo de clientes não existe.
2. Leitura de registros a partir de um JSON válido.
3. Tratamento de JSON inválido.
4. Gravação correta dos registros em JSON.
5. Cadastro e armazenamento de um cliente pelo menu.
6. Rejeição de cadastro sem nome.
7. Listagem de clientes cadastrados.
8. Edição de nome e contato.
9. Rejeição de número inválido na edição.
10. Rejeição de nome vazio na edição.
11. Exclusão de um registro selecionado.
12. Rejeição de número inválido na exclusão.
13. Edição e exclusão pelo menu com persistência em JSON.\n14. Ignorar registros malformados.\n15. Rejeitar JSON válido que não seja uma lista.\n16. Remover espaços extras no cadastro.\n17. Rejeitar nome vazio e contato com tipo inválido.\n18. Rejeitar contato inválido na edição.\n19. Rejeitar identificador de cliente que não seja inteiro.\n20. Validar cadastro e persistência pelo menu.

Para executar os testes localmente:

```bash
python -m unittest -v
```

### Integração contínua

O GitHub Actions executa os testes automaticamente em atualizações (*push*) e solicitações de alteração (*pull requests*) direcionadas à branch `main`. O workflow utiliza Python 3.12 e executa `python -m unittest -v`.

O selo no início deste README mostra o status mais recente do workflow. [Consulte as execuções no GitHub Actions](https://github.com/gabrielle-software/meu-primeiro-projeto/actions).

## Armazenamento e privacidade

Os registros são armazenados localmente no arquivo `customers.json`, criado automaticamente quando um cliente é cadastrado. Esse arquivo está listado no `.gitignore` para evitar o envio acidental de dados locais ao GitHub.

**Importante:** este projeto é demonstrativo. Não utilize dados pessoais ou informações reais/sensíveis de clientes.

## Próximas melhorias

- Melhorar a validação dos dados.
- Ampliar a cobertura dos testes automatizados.
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
- `unittest` for automated testing
- Git and GitHub for version control
- GitHub Actions for continuous integration

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

## Automated Tests

The project includes **20 automated tests** using Python's `unittest` library. They check:

1. Returning an empty list when the customer file does not exist.
2. Loading records from valid JSON.
3. Handling invalid JSON.
4. Saving customer records correctly as JSON.
5. Adding and saving a customer through the menu.
6. Rejecting a customer record without a name.
7. Listing saved customers.
8. Editing a customer name and contact.
9. Rejecting an invalid customer number when editing.
10. Rejecting a blank customer name when editing.
11. Deleting a selected customer.
12. Rejecting an invalid customer number when deleting.
13. Editing and deleting records through the menu with JSON persistence.\n14. Ignoring malformed records.\n15. Rejecting valid JSON that is not a list.\n16. Trimming whitespace when adding records.\n17. Rejecting blank names and invalid contact types.\n18. Rejecting invalid contact values during editing.\n19. Rejecting non-integer customer identifiers.\n20. Validating customer creation and persistence through the menu.

To run the tests locally:

```bash
python -m unittest -v
```

### Continuous Integration

GitHub Actions automatically runs the tests on pushes and pull requests targeting the `main` branch. The workflow uses Python 3.12 and runs `python -m unittest -v`.

The badge at the top of this README displays the latest workflow status. [View workflow runs on GitHub Actions](https://github.com/gabrielle-software/meu-primeiro-projeto/actions).

## Data Storage and Privacy

Customer records are stored locally in `\`customers.json\`, which is automatically created when a customer is added. This file is listed in `.gitignore` to help prevent local data from being accidentally pushed to GitHub.

**Important:** this is a demonstration project. Do not use real or sensitive personal/customer information.

## Planned Improvements

- Improve input validation and error messages.
- Improve input validation.
- Expand automated test coverage.
- Build and document additional projects as they are implemented.

---

Developed by **Gabrielle Sousa** as part of my Software Engineering studies.
