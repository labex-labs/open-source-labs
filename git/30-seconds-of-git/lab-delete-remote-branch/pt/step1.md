# Excluir uma _Remote Branch_ (Ramificação Remota)

Às vezes, pode ser necessário excluir uma _remote branch_ (ramificação remota) que não é mais necessária. Por exemplo, se uma _feature branch_ (ramificação de funcionalidade) foi mesclada na _main branch_ (ramificação principal), você pode querer excluir a _feature branch_ remota para manter o repositório limpo.

Suponha que um repositório do GitHub chamado `git-playground` tenha sido clonado da sua conta do GitHub, que vem de um _fork_ de `https://github.com/labex-labs/git-playground.git`. Você deseja excluir a _remote branch_ (ramificação remota) chamada `feature-branch` que não é mais necessária. Aqui estão os passos para excluir a _remote branch_:

1.  Clone o repositório, navegue até o diretório e configure a identidade:
    ```shell
    git clone https://github.com/your-username/git-playground.git
    cd git-playground
    git config --global user.name "your-username"
    git config --global user.email "your-email"
    ```
2.  Adicione a ramificação `feature-branch` ao repositório remoto `origin`:
    ```shell
    git checkout -b feature-branch
    git push -u origin feature-branch
    ```
3.  Use o comando `git branch -r` para listar todas as _remote branches_ (ramificações remotas).
    ```shell
    git branch -r
    ```
    A saída deve incluir a _remote branch_ `feature-branch`:
    ```
    origin/HEAD -> origin/master
    origin/feature-branch
    origin/master
    ```
4.  Use o comando `git push -d <remote> <branch>` para excluir a `<branch>` remota especificada no `<remote>` fornecido.
    ```shell
    git push -d origin feature-branch
    ```
    Este comando exclui a _remote branch_ `feature-branch` no repositório remoto `origin`.
5.  Use o comando `git branch -r` novamente para verificar se a _remote branch_ foi excluída.
    ```shell
    git branch -r
    ```
    A saída não deve incluir a _remote branch_ `feature-branch`:
    ```
    origin/HEAD -> origin/master
    origin/master
    ```
