# Renomear _Branch_ Remoto

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta GitHub, que vem de um _fork_ de `https://github.com/labex-labs/git-playground.git`. Por favor, desmarque "Copy master branch only" ao fazer o _fork_.

Você tem um repositório Git chamado `https://github.com/your-username/git-playground`. Você criou um _branch_ chamado `feature-branch` e o enviou para o remoto. Agora você quer renomear o _branch_ para `new-feature-1` tanto localmente quanto no remoto.

1. Clone o repositório, navegue até o diretório e configure a identidade:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Mude para o _branch_ chamado `feature-branch`:
   ```shell
   git checkout feature-branch
   ```
3. Renomeie o _branch_ tanto localmente quanto no remoto:
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Verifique se o _branch_ foi renomeado:
   ```shell
   git branch -a
   ```

Este é o resultado da execução de `git branch -a`:

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
