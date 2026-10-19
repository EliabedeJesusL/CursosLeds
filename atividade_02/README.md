# Atividade 2: CI com GitHub Actions

Este diretório contém uma aplicação simples em Python, testes unitários com pytest e a resolução teórica sobre os elementos do GitHub Actions.

## Evidência de Execução

![Evidência do Pipeline](evidencia_atv2.png)

*(Nota: O workflow que executa esta atividade está na pasta raiz do repositório em `.github/workflows/ci.yml` utilizando a estratégia de matriz).*

## Explicação dos Elementos do GitHub Actions

O pipeline (workflow) do GitHub Actions é estruturado usando um arquivo YAML. Abaixo está a explicação do papel de cada elemento principal exigido na atividade:

* **`on`**: Define os "gatilhos" (triggers) que iniciam a execução do workflow. Por exemplo, podemos configurar para rodar sempre que houver um `push` (envio de código) ou um `pull_request` no repositório.
* **`jobs`**: Representa um conjunto de passos (steps) que são executados em um mesmo ambiente. Um workflow pode ter vários jobs rodando em paralelo ou de forma sequencial.
* **`runs-on`**: Especifica qual é o ambiente virtual ou sistema operacional (runner) onde o job será executado. O uso mais comum é o `ubuntu-latest`, que fornece uma máquina Linux atualizada.
* **`steps`**: É a lista de tarefas sequenciais executadas dentro de um job. Cada step (passo) pode rodar um comando no terminal ou executar uma action pré-configurada.
* **`uses`**: Usado dentro de um *step* para chamar uma "Action" pronta, desenvolvida pelo próprio GitHub ou pela comunidade. Por exemplo, `actions/checkout@v4` é uma action pronta que faz o download do código para o runner.
* **`run`**: Usado dentro de um *step* para executar comandos de terminal (linhas de comando) no sistema operacional do runner, como `pip install` ou rodar scripts de teste.
