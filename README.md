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
- Tratar arquivo ausente e interromper a execução com segurança quando o JSON estiver inválido ou houver registros malformados.
- Gravar por meio de arquivo temporário para preservar os dados originais em caso de falha.

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

O projeto possui **28 testes automatizados** com a biblioteca `unittest`. Eles verificam:

1. Retorno de lista vazia quando o arquivo não existe.
2. Leitura de JSON válido.
3. Rejeição de JSON inválido sem alterar o arquivo original.
4. Rejeição de registros malformados sem alterar o arquivo original.
5. Rejeitar JSON válido que não seja uma lista.
6. Gravação correta em JSON.
7. Preservação do arquivo original quando a gravação temporária falha.
8. Preservação do arquivo original quando a substituição falha.
9. Remoção do arquivo temporário após falha na substituição.
10. Cadastro com remoção de espaços extras.
11. Rejeição de nome vazio.
12. Rejeição de contato com tipo inválido.
13. Interrupção segura do programa quando o arquivo de clientes está corrompido.
14. Cadastro e persistência pelo menu.
15. Rejeição de cadastro sem nome pelo menu.
16. Listagem de clientes pelo menu.
17. Edição de nome e contato.
18. Rejeição de número inválido na edição.
19. Rejeição de nome vazio na edição.
20. Rejeição de contato inválido na edição.
21. Exclusão de cliente selecionado.
22. Rejeição de número inválido na exclusão.
23. Rejeição de número de cliente que não seja inteiro.
24. Edição e persistência pelo menu.
25. Exclusão e persistência pelo menu.
26. Não confirmar cadastro quando a gravação falha.
27. Não confirmar edição quando a gravação falha.
28. Não confirmar exclusão quando a gravação falha.

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
- Handle missing files and stop safely when JSON or customer records are invalid.
- Use a temporary file when saving to preserve the original data if a write or replacement fails.

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

The project includes **28 automated tests** using Python's `unittest` library. They cover:

1. Returning an empty list when the data file is missing.
2. Loading valid JSON.
3. Rejecting invalid JSON without changing the original file.
4. Rejecting malformed records without changing the original file.
5. Rejecting valid JSON that is not a list.
6. Saving records as JSON.
7. Preserving the original file when writing the temporary file fails.
8. Preserving the original file when replacing it fails.
9. Removing the temporary file after a failed replacement.
10. Trimming whitespace when adding a customer.
11. Rejecting a blank customer name.
12. Rejecting a contact value with an invalid type.
13. Stopping safely when the customer file is corrupted.
14. Adding and saving a customer through the menu.
15. Rejecting a customer without a name through the menu.
16. Listing customers through the menu.
17. Editing a customer's name and contact.
18. Rejecting an invalid customer number when editing.
19. Rejecting a blank name when editing.
20. Rejecting an invalid contact value when editing.
21. Deleting a selected customer.
22. Rejecting an invalid customer number when deleting.
23. Rejecting a customer number that is not an integer.
24. Editing and saving through the menu.
25. Deleting and saving through the menu.
26. Not confirming an addition when saving fails.
27. Not confirming an edit when saving fails.
28. Not confirming a deletion when saving fails.

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
