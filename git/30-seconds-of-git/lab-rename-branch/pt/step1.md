# Renomear um Branch

Como desenvolvedor, você pode precisar renomear um branch por vários motivos, como torná-lo mais descritivo ou seguir uma convenção de nomenclatura. Renomear um branch pode ser uma tarefa simples, mas requer algum conhecimento dos comandos Git. Neste desafio, você aprenderá como renomear um branch usando Git.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground`.

Suponha que você crie um branch chamado `old-branch` para trabalhar em uma nova funcionalidade. Após concluir a funcionalidade, você percebe que o nome do branch não é descritivo o suficiente. Você deseja renomear o branch para `new-branch` para torná-lo mais significativo. Para renomear o branch, siga estas etapas:

1. Abra o terminal e navegue até o diretório do repositório local.
2. Use o comando `git checkout -b old-branch` para criar um branch chamado `old-branch` e use o comando `git branch -m <old-name> <new-name>` para renomear o branch. Em nosso exemplo, o comando seria `git branch -m old-branch new-branch`.
3. Verifique se o branch foi renomeado usando o comando `git branch`.

A saída deve mostrar o novo nome do branch:

```shell
master
* new-branch
```
