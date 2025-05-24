# Encontrar Branches Contendo um Commit

Você recebeu um repositório Git chamado `https://github.com/labex-labs/git-playground`. Sua tarefa é encontrar todas as branches que contêm um hash com a mensagem de commit "Added file2.txt".

1.  Entre no diretório do repositório:

```shell
cd git-playground
```

2.  Use o comando `git branch --contains` para encontrar todas as branches que contêm um hash com a mensagem de commit "Added file2.txt":

```shell
git branch --contains d22f46b
```

A saída deve ser:

```shell
* master
new-branch
new-branch-1
new-branch-2
```
