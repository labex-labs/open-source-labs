# Fazer Merge de uma Branch e Criar um Commit de Merge

Como desenvolvedor, você pode precisar fazer merge de uma branch na branch atual, criando um commit de merge. Isso pode ser um pouco complicado se você não estiver familiarizado com o Git. O problema é fazer merge de uma branch na branch atual, criando um commit de merge, usando o repositório Git chamado `https://github.com/labex-labs/git-playground` no diretório.

Para este desafio, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone um repositório de `https://github.com/labex-labs/git-playground.git`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o diretório e configure a identidade:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Crie e mude para uma branch chamada `feature-branch`:

```shell
git checkout -b feature-branch
```

4. Adicione "This is a new line." ao arquivo `README.md`, adicione-o à área de staging (preparação) e faça o commit, a mensagem do commit é "Add new line to README.md":

```shell
echo "This is a new line." >> README.md
git add .
git commit -am "Add new line to README.md"
```

5. Mude para a branch `master`:

```shell
git checkout master
```

6. Faça merge da `feature-branch` na branch `master`, o que criará um commit de merge com a mensagem "Merge feature-branch":

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

Este é o resultado da execução de `git log`:

```shell
ADD new line to README.md
```
