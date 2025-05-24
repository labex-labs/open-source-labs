# Desfazer o Último Commit

Você acabou de commitar (fazer commit) alterações em seu repositório Git, mas percebeu que cometeu um erro. Você quer desfazer o último commit sem perder nenhuma das alterações que fez. Como você pode fazer isso?

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estes passos:

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Verifique o histórico de commits:

```shell
git log
```

3. Desfaça o último commit, criando um novo commit com o inverso das alterações do commit:

```shell
git revert HEAD
```

4. Verifique o histórico de commits novamente:

```shell
git log
```

Este é o resultado da execução do comando `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
