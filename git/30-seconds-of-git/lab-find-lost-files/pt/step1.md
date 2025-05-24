# Encontrar Arquivos Perdidos

Você tem trabalhado em um projeto no repositório `git-playground`. No entanto, você notou que alguns arquivos estão faltando e não tem certeza de quando foram excluídos ou como recuperá-los. Sua tarefa é usar o Git para encontrar quaisquer arquivos e commits perdidos no repositório.

1. Clone o repositório `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o diretório e configure a identidade:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Crie e altere para uma branch chamada `one-branch`, exclua `file2.txt` e faça o commit com a mensagem "Remove file2":

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
```

4. Volte para a branch `master` e exclua a branch `one-branch`:

```shell
git checkout master
git branch -D one-branch
```

5. Execute o comando `git fsck --lost-found` para encontrar quaisquer arquivos e commits perdidos:

```shell
git fsck --lost-found
```

6. Verifique o diretório `.git/lost-found` para ver se algum arquivo perdido foi recuperado:

```shell
ls .git/lost-found
```

7. Se algum arquivo perdido for encontrado, revise-o para determinar se são os arquivos ausentes.

Este é o resultado da execução do comando `ls .git/lost-found`:

```shell
commit
```
