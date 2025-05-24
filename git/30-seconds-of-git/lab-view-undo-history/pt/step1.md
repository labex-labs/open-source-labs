# Visualizar o Histórico de "Desfazer"

Como desenvolvedor, você pode precisar desfazer as alterações que fez em seu código-base. O Git oferece várias maneiras de desfazer alterações, como usar os comandos `git reset` ou `git revert`. No entanto, pode ser difícil acompanhar todas as ações que você tomou, especialmente se você usou comandos mais avançados como `git rebase`. É aqui que o comando `git reflog` se torna útil.

O comando `git reflog` exibe o registro de referência do Git, que é um registro de todas as ações que você realizou em seu repositório. Isso inclui não apenas commits, mas também outras ações como merges de branch, rebases e resets. Ao visualizar o registro de referência, você pode ver um histórico completo de todas as alterações que fez em seu repositório, mesmo que elas não apareçam no histórico de commits.

Para visualizar o histórico de "desfazer" no Git, você pode usar o comando `git reflog`. Digamos que você tenha feito algumas alterações em um repositório e queira desfazê-las.

1. Navegue até o repositório usando a linha de comando:

```shell
cd git-playground
```

2. Agora, digamos que você perceba que cometeu um erro e queira desfazer o último commit. Você pode usar o comando `git reset` para fazer isso:

```shell
git reset HEAD~1
```

3. Depois de executar este comando, você pode perceber que cometeu outro erro e quer desfazer o reset. É aqui que o comando `git reflog` é útil. Você pode usá-lo para visualizar o registro de referência e encontrar o hash do commit anterior:

```shell
git reflog
```

Isso exibirá uma lista de todas as ações que você realizou no repositório, incluindo o reset:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. A partir desta saída, você pode ver que o hash do commit anterior é `d22f46b`. Você pode usar este hash para redefinir o repositório de volta ao commit anterior:

```shell
git reset d22f46b
```

5. Visualize os registros históricos de commits para verificar os resultados:

```shell
git log
```
