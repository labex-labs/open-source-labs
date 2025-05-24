# Remover um Arquivo do Último Commit

Você adicionou um arquivo ao último commit que não pretendia incluir. Deseja remover o arquivo do último commit sem alterar sua mensagem.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Suponha que você tenha um repositório Git chamado `git-playground` com um arquivo chamado `file2.txt` que você adicionou acidentalmente ao último commit. Aqui estão os passos para remover o arquivo do último commit:

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Use `git rm --cached <file>` para remover o `<file>` especificado do índice:

```shell
git rm --cached file2.txt
```

3. Use `git commit --amend` para atualizar o conteúdo do último commit, sem alterar sua mensagem:

```shell
git commit --amend --allow-empty
```

Se o commit for um commit vazio após a exclusão do arquivo, use `--allow-empty`, caso contrário, você pode omiti-lo.

Após executar esses comandos, o arquivo `file2.txt` será removido do último commit sem alterar sua mensagem.

Isto é o que acontece quando você remove `file2.txt` do controle de versão Git:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
