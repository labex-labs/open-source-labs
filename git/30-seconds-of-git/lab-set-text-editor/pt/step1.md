# Configurar o editor de texto do Git

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Você deseja configurar o editor de texto usado pelo Git para o seu editor preferido.

1. Clone o repositório `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navegue até o repositório clonado e configure a identidade:

```shell
cd git-playground
git config --global user.name "seu-nome-de-usuário"
git config --global user.email "seu-email"
```

3. Configure o Git para usar seu editor de texto preferido (neste exemplo, usaremos vim):

```shell
git config --global core.editor "vim"
```

4. Faça uma alteração em um arquivo e prepare-o para o commit:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Faça o commit da alteração:

```shell
git commit
```

6. Seu editor de texto preferido (neste exemplo, vim) deve abrir com a mensagem de commit. Escreva sua mensagem de commit "Update hello.txt" e salve o arquivo.
7. Feche o editor de texto. O commit será feito com a mensagem que você escreveu.

Este é o resultado final:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
