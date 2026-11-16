# Sistema de Gerenciamento de Clientes — Portfólio de Engenharia de Software

[![Testes automatizados](https://github.com/gabrielle-software/meu-primeiro-projeto/actions/workflows/tests.yml/badge.svg)](https://github.com/gabrielle-software/meu-primeiro-projeto/actions/workflows/tests.yml)

Projeto em Python desenvolvido para praticar lógica de programação, funções, estruturas de dados, validação de entradas, persistência em JSON e testes automatizados.

## Funcionalidades

- Cadastrar clientes com nome obrigatório e contato opcional.
- Listar clientes cadastrados.
- Editar o nome e/ou contato de um cliente.
- Excluir clientes após confirmação.
- Validar dados e remover espaços extras.
- Carregar dados de um arquivo JSON.
- Tratar arquivo ausente, JSON inválido e registros malformados.
- Tratar falhas de gravação sem confirmar operações que não foram salvas.

## Tecnologias

- Python 3
- JSON
- `pathlib` para manipulação de caminhos e arquivos
- `unittest` para testes automatizados
- Git e GitHub
- GitHub Actions para integração contínua

## Como executar

**Pré-requisito:** Python 3 instalado.

1. Clone o repositório:

```bash
git clone https://github.com/gabrielle-software/meu-primeiro-projeto.git
```

2. Acesse a pasta:

```bash
cd meu-primeiro-projeto
```

3. Execute a aplicação:

```bash
python main.py
```

No Windows, também é possível usar `py main.py`. Em alguns sistemas Linux, use `python3 main.py`.

## Testes automatizados

O projeto possui **25 testes automatizados** com a biblioteca `unittest`. Eles verificam:

1. Retorno de lista vazia quando o arquivo não existe.
2. Leitura de JSON válido.
3. Tratamento de JSON inválido.
4. Ignorar registros malformados.
5. Rejeitar JSON válido que não seja uma lista.
6. Gravação correta em JSON.
7. Retorno de falha quando a gravação gera erro.
8. Cadastro com remoção de espaços extras.
9. Rejeição de nome vazio.
10. Rejeição de contato com tipo inválido.
11. Cadastro e persistência pelo menu.
12. Rejeição de cadastro sem nome pelo menu.
13. Listagem de clientes pelo menu.
14. Edição de nome e contato.
15. Rejeição de número inválido na edição.
16. Rejeição de nome vazio na edição.
17. Rejeição de contato inválido na edição.
18. Exclusão de cliente selecionado.
19. Rejeição de número inválido na exclusão.
20. Rejeição de número de cliente que não seja inteiro.
21. Edição e persistência pelo menu.
22. Exclusão e persistência pelo menu.
23. Não confirmar cadastro quando a gravação falha.
24. Não confirmar edição quando a gravação falha.
25. Não confirmar exclusão quando a gravação falha.

Para executar os testes localmente:

```bash
python -m unittest -v
```

## Integração contínua

O GitHub Actions executa os testes automaticamente em atualizações (*push*) e solicitações de alteração (*pull requests*) direcionadas à branch `main`. O workflow utiliza Python 3.12 e executa `python -m unittest -v`.

[Consultar as execuções do GitHub Actions](https://github.com/gabrielle-software/meu-primeiro-projeto/actions).

## Armazenamento e privacidade

Os registros são armazenados localmente no arquivo `customers.json`, criado quando um cliente é cadastrado. O arquivo está listado no `.gitignore` para reduzir o risco de envio acidental de dados locais ao GitHub.

**Importante:** este projeto é demonstrativo. Não utilize dados pessoais ou informações reais/sensíveis de clientes.

## Próximas melhorias

- Adicionar exportação e importação de dados.
- Aprimorar a experiência de uso do menu.
- Ampliar a documentação de exemplos de execução.

---

Desenvolvido por **Gabrielle Sousa** como parte dos estudos em Engenharia de Software.

---

# Customer Management System — Software Engineering Portfolio

A Python command-line project created to practice programming logic, functions, data structures, input validation, JSON persistence, and automated testing.

## Features

- Add customers with a required name and optional contact information.
- List saved customers.
- Edit a customer's name and/or contact information.
- Delete customers after confirmation.
- Validate input and trim extra whitespace.
- Load records from a JSON file.
- Handle missing files, invalid JSON, and malformed records.
- Handle file-writing errors without confirming operations that were not saved.

## Technologies

- Python 3
- JSON
- `pathlib` for file and path handling
- `unittest` for automated tests
- Git and GitHub
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

The project includes **25 automated tests** using Python's `unittest` library. They cover:

1. Returning an empty list when the data file is missing.
2. Loading valid JSON.
3. Handling invalid JSON.
4. Ignoring malformed records.
5. Rejecting valid JSON that is not a list.
6. Saving records as JSON.
7. Returning a failure result when writing raises an error.
8. Trimming whitespace when adding a customer.
9. Rejecting a blank customer name.
10. Rejecting a contact value with an invalid type.
11. Adding and saving a customer through the menu.
12. Rejecting a customer without a name through the menu.
13. Listing customers through the menu.
14. Editing a customer's name and contact.
15. Rejecting an invalid customer number when editing.
16. Rejecting a blank name when editing.
17. Rejecting an invalid contact value when editing.
18. Deleting a selected customer.
19. Rejecting an invalid customer number when deleting.
20. Rejecting a customer number that is not an integer.
21. Editing and saving through the menu.
22. Deleting and saving through the menu.
23. Not confirming an addition when saving fails.
24. Not confirming an edit when saving fails.
25. Not confirming a deletion when saving fails.

Run the tests locally:

```bash
python -m unittest -v
```

## Continuous Integration

GitHub Actions automatically runs the tests on pushes and pull requests targeting the `main` branch. The workflow uses Python 3.12 and runs `python -m unittest -v`.

[View GitHub Actions workflow runs](https://github.com/gabrielle-software/meu-primeiro-projeto/actions).

## Data Storage and Privacy

Customer records are stored locally in `customers.json`, which is created when a customer is added. The file is listed in `.gitignore` to reduce the risk of accidentally pushing local data to GitHub.

**Important:** this is a demonstration project. Do not use real or sensitive personal/customer information.

## Planned Improvements

- Add data import and export.
- Improve the menu user experience.
- Expand the documentation with usage examples.

---

Developed by **Gabrielle Sousa** as part of my Software Engineering studies.
