# Visualizar Mudanças Entre Commits

Como desenvolvedor, você tem trabalhado em um projeto hospedado no repositório `https://github.com/labex-labs/git-playground`. Você fez vários commits no repositório e deseja visualizar um resumo das alterações entre dois commits específicos. No entanto, você não tem certeza de como fazer isso usando Git.

Para visualizar um resumo das alterações entre dois commits, digamos que você queira visualizar as alterações entre o commit `HEAD` e o commit com a mensagem "Initial commit". Veja como você pode fazer isso:

1. Abra uma janela de terminal e navegue até o diretório onde o repositório `git-playground` está localizado:

```
cd git-playground
```

2. Execute o seguinte comando:

```
git shortlog 3050fc0de..HEAD
```

Git exibirá um resumo das alterações entre os dois commits. Você pode usar as setas do teclado para navegar pelo resumo e pressionar `Q` para sair.

Aqui está um exemplo de como a saída pode ser:

```shell
Hang (2):
      Added file1.txt
      Added file2.txt
```

Neste exemplo, Git está mostrando que houve dois commits entre o commit `3050fc0de` e o commit `HEAD`. O primeiro commit adicionou `file1.txt` e o segundo commit adicionou `file2.txt`.
