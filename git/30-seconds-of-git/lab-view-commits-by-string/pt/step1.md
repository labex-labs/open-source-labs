# Encontrar Commits que Manipularam uma String Específica

Como desenvolvedor, você pode precisar encontrar todos os commits que modificaram uma string específica em seu código. Por exemplo, você pode querer encontrar todos os commits que adicionaram ou removeram um nome de função ou variável específica. Isso pode ser útil ao depurar problemas ou rastrear a origem de um bug.

Suponha que você esteja trabalhando em um projeto hospedado no GitHub chamado `git-playground`. Você quer encontrar todos os commits que modificaram a string "Git Playground" no arquivo `README.md`. Veja como você pode fazer isso:

1. Navegue até o diretório do repositório:

```shell
cd git-playground
```

2. Use o comando `git log -S` para encontrar todos os commits que modificaram a string "Git Playground" no arquivo `README.md` e use as setas para navegar pela lista de commits. Pressione <kbd>Q</kbd> para sair do log:

```shell
git log -S"Git Playground" README.md
```

O Git exibirá uma lista de todos os commits que modificaram a string "Git Playground" no arquivo `README.md`:

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
