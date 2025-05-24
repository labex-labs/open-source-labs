# Remover Arquivos da Área de Staging

Você está trabalhando em um projeto no repositório `git-playground`. Você fez algumas alterações nos arquivos e os adicionou à área de staging usando o comando `git add`. No entanto, você percebe que adicionou acidentalmente um arquivo que não deseja commitar. Você precisa remover este arquivo da área de staging.

1. Visualizar o status atual do diretório de trabalho:

```shell
git status
```

2. Remover o arquivo `newfile.txt` da área de staging usando o comando `git restore --staged`:

```shell
git restore --staged newfile.txt
```

3. Verificar se o arquivo foi removido da área de staging usando o comando `git status`:

```shell
git status
```

Este é o resultado final:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
