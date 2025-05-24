# Rebase em Outra Branch

Como desenvolvedor, você está trabalhando em um projeto com múltiplas branches. Você fez alterações em sua branch e deseja incorporar essas alterações em outra branch. No entanto, você não quer fazer o merge (merge) das branches porque deseja manter um histórico limpo e linear. Nesse caso, você pode usar o comando `git rebase` para fazer o rebase de sua branch em outra branch.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga os passos abaixo para completar o laboratório:

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crie e mude para uma branch chamada `one-branch`:

```shell
git checkout -b one-branch
```

3. Adicione "hello,world" ao arquivo `README.md`, adicione-o à área de staging (staging area) e faça o commit com a mensagem "Added some changes to README.md":

```shell
echo "hello,world" >> README.md
git add .
git commit -am "Added some changes to README.md"
```

4. Mude para a branch `master`:

```shell
git checkout master
```

5. Certifique-se de que sua branch `master` local está atualizada com o repositório remoto:

```shell
git pull
```

6. Faça o rebase da `one-branch` na branch `master`:

```shell
git rebase one-branch
```

7. Resolva quaisquer conflitos que surjam durante o processo de rebase.

Este é o resultado da execução de `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
