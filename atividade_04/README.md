# Atividade 4 - Pipeline de Deploy Contínuo (CD) com Ambientes e Aprovação Manual

Esta atividade demonstra a criação de um fluxo automatizado de Continuous Deployment (CD) utilizando o GitHub Actions, com separação de ambientes (`staging` e `production`), proteção com aprovação manual e utilização segura de secrets.

## Como o pipeline funciona

O pipeline (configurado no arquivo `.github/workflows/cd.yml`) é acionado automaticamente sempre que há um novo *push* na branch `main`. Ele é dividido em três etapas sequenciais:

1. **`ci` (Continuous Integration)**: 
   - É o primeiro *job* a rodar. Ele simula a execução de testes automatizados para garantir que o código está íntegro.
2. **`deploy-staging`**: 
   - Depende do sucesso do `ci` (configurado com a diretiva `needs: ci`). Realiza o deploy automático no ambiente de homologação/testes.
3. **`deploy-production`**: 
   - Depende do sucesso de `deploy-staging` (`needs: deploy-staging`). É a última etapa que envia o código para os usuários finais, mas, devido à configuração do ambiente "production" no GitHub, o processo **pausa** e aguarda uma aprovação manual antes de executar.

## O papel de cada ambiente

- **`staging` (Homologação):** Um ambiente idêntico à produção, utilizado para a equipe de QA (Qualidade) e desenvolvedores validarem as novas funcionalidades antes que elas cheguem aos clientes. O deploy aqui é automático após os testes passarem.
- **`production` (Produção):** O ambiente real acessado pelos usuários finais. Exige estabilidade máxima, por isso os deploys para cá são controlados por uma camada extra de segurança (Aprovação Manual).

## Onde ocorre a aprovação manual e como configurar

A aprovação manual não fica escrita diretamente no código YAML, ela é configurada na interface do próprio GitHub.

**Como funciona a aprovação:**
Quando o pipeline termina o *job* `deploy-staging`, ele entra no estado "Waiting" no *job* `deploy-production`. Um e-mail é enviado aos revisores (Reviewers), que precisam entrar na aba **Actions** e clicar no botão **"Review deployments"** para aprovar ou rejeitar o deploy para produção.

**Passo a passo para você configurar isso no seu repositório:**
1. Vá na aba **Settings** do seu repositório no GitHub.
2. No menu lateral esquerdo, clique em **Environments**.
3. Clique no botão **New environment** e crie um ambiente com o nome exato: `production`.
4. Dentro das configurações deste ambiente recém-criado, marque a caixa **Required reviewers**.
5. Na barra de pesquisa que aparece, digite o seu próprio usuário do GitHub e adicione-se como revisor.
6. Clique em **Save protection rules**.
*(Opcional: Crie também um ambiente chamado `staging`, mas deixe sem reviewers, pois queremos que seja automático).*

## Como os secrets seriam utilizados

Secrets são variáveis de ambiente criptografadas, usadas para guardar senhas, tokens e chaves de API sem expô-las no código do repositório. No nosso `.yml`, referenciamos as secrets assim: `${{ secrets.NOME_DA_SECRET }}`.

**Como configurar os Secrets:**
1. Vá em **Settings** > **Secrets and variables** > **Actions**.
2. Clique em **New repository secret**.
3. Crie uma secret chamada `STAGING_API_TOKEN` e coloque qualquer valor fictício (ex: `12345-staging`).
4. Crie outra secret chamada `PROD_API_KEY` e coloque outro valor fictício (ex: `98765-prod`).
*(Quando o workflow rodar, o GitHub mascarará o valor real no console substituindo-o por `***`)*.

## Como visualizar a execução do workflow

1. Após fazer o *commit* e *push* das configurações para a branch `main`, clique na aba **Actions** na parte superior do seu repositório.
2. Clique na execução mais recente listada (com o título do seu último commit).
3. Você verá um gráfico visual mostrando os blocos `ci` -> `deploy-staging` -> `deploy-production`.
4. Poderá clicar em cada bloco para ver o log do terminal ("preto") mostrando os comandos (como os nossos `echo`) sendo executados em tempo real.
