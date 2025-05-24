# Mover Commits para um Novo Branch

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Você tem trabalhado em um projeto no branch `master`. Você percebe que algumas das alterações que fez deveriam ter sido feitas em um branch separado. Você quer mover essas alterações para um novo branch chamado `feature`.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Faça o checkout do branch `master`:

```shell
git checkout master
```

3. Crie um arquivo chamado `hello.txt`, adicione "hello, world" a ele, adicione-o à área de staging (staging area) e faça o commit com a mensagem "Added hello.txt":

```shell
echo "hello,world" >> hello.txt
git add .
git commit -m "Added hello.txt"
```

4. Crie um novo branch chamado `feature` sem mudar para ele. Quando você cria um novo branch no branch `master`, o estado do novo branch é o mesmo do branch `master`, ou seja, os arquivos no novo branch são os mesmos dos arquivos no branch `master`, com o mesmo conteúdo e histórico de versões:

```shell
git branch feature
```

5. Desfaça o último commit no `master`:

```shell
git reset HEAD~1 --hard
```

6. Verifique o histórico de commits no branch `master` e o histórico de commits no branch `feature` para verificar os resultados:

```shell
git log
git checkout feature
git log
```

Este é o resultado da execução de `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
