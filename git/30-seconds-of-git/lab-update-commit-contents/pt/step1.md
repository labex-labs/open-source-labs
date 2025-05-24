# Editar o Último Commit

Você acabou de commitar algumas alterações em seu repositório Git, mas percebeu que esqueceu de incluir um arquivo ou fazer uma pequena alteração. Você não quer criar um novo commit apenas para essa pequena alteração, mas também não quer alterar a mensagem do commit. Como você pode editar o último commit sem alterar sua mensagem?

Para demonstrar como editar o último commit, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Perceba que você esqueceu de incluir um arquivo ou fazer uma pequena alteração. Adicione o texto "New content" ao final do arquivo `README.md`. Adicione quaisquer alterações preparadas (staged changes) ao último commit, sem alterar sua mensagem:

```shell
echo "New content" >> README.md
git add README.md
git commit --amend --no-edit
```

3. Verifique se o último commit agora inclui as alterações que você fez:

```shell
git show HEAD
```

Este é o conteúdo do último commit:
![Updated commit contents display](../assets/challenge-update-commit-contents.png)
