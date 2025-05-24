# Visualizar o Último Commit

Você está trabalhando em um projeto com uma equipe de desenvolvedores e precisa visualizar o último commit feito no repositório Git do projeto. Você quer ver os detalhes do commit, incluindo a mensagem do commit, o autor e a data.

Para visualizar o último commit feito em um repositório Git, siga estes passos:

1.  Abra o terminal no seu computador.
2.  Navegue até o diretório onde o repositório Git está localizado:

```shell
cd git-playground
```

3.  Visualize o último commit:

```shell
git log -1
```

A saída mostrará os detalhes do último commit, incluindo a mensagem do commit, o autor e a data:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
