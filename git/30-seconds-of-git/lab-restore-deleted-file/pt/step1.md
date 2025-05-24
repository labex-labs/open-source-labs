# Restaurar um Arquivo Excluído

Você está trabalhando em um projeto usando Git e acidentalmente excluiu um arquivo chamado `file2.txt` que você precisa. Felizmente, você sabe o commit onde o arquivo foi excluído. Sua tarefa é restaurar o arquivo excluído usando Git.

Para completar este laboratório, você usará o repositório Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Siga os passos abaixo:

1. Navegue até o diretório do repositório usando o comando `cd git-playground`.
2. Execute o comando `git log --oneline` para visualizar o histórico de commits.
3. Identifique um commit onde um arquivo foi excluído com a mensagem "Added file2.txt".
4. Execute o comando `git checkout <commit> -- <file>` para restaurar o `<file>` especificado excluído no `<commit>` especificado. Substitua `<commit>` pelo hash do commit e `<file>` pelo nome do arquivo excluído.

Por exemplo, se o arquivo `file2.txt` foi excluído no commit `d22f46b`, você executaria o seguinte comando:

```shell
git checkout d22f46b -- file2.txt
```

Isso restaurará o arquivo `file2.txt` para o seu repositório local.

Este é o resultado da execução do comando `ll`:

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
