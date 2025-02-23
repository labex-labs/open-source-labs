# Lista de todos los alias de Git

Como desarrollador, es posible que desees listar todos los alias de Git que se han configurado en tu sistema. Esto puede ser útil por varios motivos, como:

- Verificar qué alias están disponibles
- Saber a qué comandos está mapeado un alias
- Eliminar o modificar alias existentes

## Tareas

Digamos que tienes un repositorio de Git llamado `git-playground` ubicado en `https://github.com/labex-labs/git-playground`.

Has configurado los siguientes alias:

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. Navega hasta este repositorio en tu máquina local.
2. Utiliza el comando `sed` durante la lista de todos los alias de Git.

Ejecutando el comando se mostrará:

```shell
st=status
co=checkout
rb=rebase
```
