# Atividade 3: Testes Automatizados e Cobertura (Coverage)

Este projeto contém uma aplicação Python com validação de testes automatizados e verificação de cobertura de código (coverage) integrados ao GitHub Actions.

## Como instalar as dependências

Para rodar este projeto, você precisa ter o Python instalado. Com o ambiente pronto, instale as dependências executando o comando abaixo na pasta raiz desta atividade:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` instalará o `pytest` (para execução dos testes) e o `pytest-cov` (para medir a cobertura do código).

## Como executar os testes localmente

Para rodar os testes e gerar o relatório de cobertura no seu terminal, certifique-se de estar dentro da pasta desta atividade e execute:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=70
```

**O que este comando faz:**
* `--cov=src`: Mede a cobertura apenas dos arquivos que estão dentro da pasta `src/`.
* `--cov-report=term-missing`: Exibe no terminal as linhas exatas de código que não foram testadas.
* `--cov-fail-under=70`: Força o teste a falhar caso a cobertura total do código seja inferior a 70%.

## Como interpretar os resultados da aba Actions

O pipeline de CI foi configurado para rodar em eventos de `push` (para as branches `develop` ou `main`) e em `pull_request` (para a `main`). 

Na aba **Actions** do GitHub, você verá a execução do workflow. 
- **Verde (Success):** Significa que todos os testes passaram E a cobertura do código atingiu o mínimo exigido de 70%.
- **Vermelho (Failed):** Significa que algum teste falhou em sua asserção (lógica) OU a cobertura de código ficou abaixo de 70%, o que acusa que novas funcionalidades foram enviadas sem a devida criação de testes. Os detalhes das linhas não cobertas podem ser vistos nos logs do *step* de testes.

## Cobertura Atingida
A cobertura de código atual do projeto atingiu **100%**, ultrapassando a meta exigida de 70%.