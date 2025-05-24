# Excluir uma Branch (Ramificação)

Você criou uma branch local em seu repositório Git e não precisa mais dela. Deseja excluir a branch para manter seu repositório limpo e organizado.

1. Navegue até o repositório clonado:

```shell
cd git-playground
```

2. Visualize as branches atuais:

```shell
git branch
```

3. Exclua a branch `feature-1`:

```shell
git branch -d feature-1
```

4. Verifique se a branch foi excluída:

```shell
git branch
```

Este é o resultado da execução do comando `git branch`:

```
* master
```
