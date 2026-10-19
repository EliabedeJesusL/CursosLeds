# Projeto Prático: CI com GitHub Actions e Pytest

Este repositório contém funções matemáticas simples em Python, testadas com `pytest` e integradas a um pipeline de Continuous Integration (CI) usando o GitHub Actions.

## Como executar o projeto localmente

1. Certifique-se de ter o Python 3.12 instalado.
2. Clone este repositório:
   `git clone <LINK_DO_SEU_REPOSITORIO>`
3. Navegue até a pasta do projeto e instale as dependências:
   `pip install -r requirements.txt`

## Como rodar os testes

Com as dependências instaladas, execute o seguinte comando na raiz do projeto:
`pytest --verbose`
Isso executará os testes definidos no arquivo `test_operations.py` e exibirá o resultado detalhado no terminal.

## Como funciona o pipeline criado

O pipeline está configurado no arquivo `.github/workflows/ci.yml` e funciona da seguinte forma:
- **Gatilhos (Triggers):** É executado automaticamente sempre que ocorre um `push` ou `pull_request` nas branches principais.
- **Ambiente:** Roda em uma máquina virtual (runner) com o sistema operacional `ubuntu-latest`.
- **Passos (Steps):**
  1. `actions/checkout@v4`: Faz o download do código do repositório para o runner.
  2. `actions/setup-python@v5`: Configura o ambiente com a versão `3.12` do Python.
  3. Instala as dependências lendo o arquivo `requirements.txt`.
  4. Roda o comando `pytest --verbose` para validar se as funções estão operando corretamente.

## Evidência de Execução

![Evidência do Pipeline](evidencia.png)
