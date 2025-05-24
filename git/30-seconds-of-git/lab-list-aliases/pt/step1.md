# Listar Todos os Aliases do Git

Como desenvolvedor, você pode querer listar todos os aliases do Git que foram configurados em seu sistema. Isso pode ser útil por várias razões, como:

- Verificar quais aliases estão disponíveis
- Descobrir a quais comandos um alias está mapeado
- Remover ou modificar aliases existentes

Digamos que você tenha um repositório Git chamado `git-playground` localizado em `https://github.com/labex-labs/git-playground`.

1. Navegue até este repositório em sua máquina local:

```shell
cd git-playground
```

2. Configure os seguintes aliases:

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. Use o comando `sed` durante a listagem de todos os aliases do Git:

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

A execução do comando produzirá a saída:

```shell
st=status
co=checkout
rb=rebase
```
