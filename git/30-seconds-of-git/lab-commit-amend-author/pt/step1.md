# Alterar o Autor do Último Commit

Você acabou de fazer um commit no seu repositório Git, mas percebeu que o nome e o endereço de e-mail do autor estão incorretos. Você deseja atualizar as informações do autor sem alterar o conteúdo do commit. Como você pode fazer isso usando o Git?

Para alterar o autor do último commit, você pode usar o comando `git commit --amend`. Este comando permite que você modifique o último commit em seu repositório Git. Aqui está um exemplo de como você pode alterar o nome e o endereço de e-mail do autor:

1. Clone o repositório Git chamado `https://github.com/labex-labs/git-playground` para sua máquina local:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Configure as informações de identidade do Git usando sua conta do GitHub:

```shell
cd git-playground
git config user.email "your email"
git config user.name "your username"
```

3. Use o comando `git commit --amend` para modificar o autor do último commit e salvar o conteúdo:

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. Verifique se as informações do autor foram atualizadas:

```shell
git log
```

Você deve ver que o autor do último commit agora é `Duck Quackers`:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
