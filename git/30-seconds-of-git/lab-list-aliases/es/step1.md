# Lista de todos los alias de Git

Como desarrollador, es posible que desees listar todos los alias de Git que se han configurado en tu sistema. Esto puede ser útil por varios motivos, como:

- Verificar qué alias están disponibles
- Saber a qué comandos está mapeado un alias
- Eliminar o modificar alias existentes

Digamos que tienes un repositorio de Git llamado `git-playground` ubicado en `https://github.com/labex-labs/git-playground`.

1. Navega a este repositorio en tu máquina local:

```shell
cd git-playground
```

2. Configura los siguientes alias:

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. Utiliza el comando `sed` durante la lista de todos los alias de Git:

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Al ejecutar el comando se mostrará:

```shell
st=status
co=checkout
rb=rebase
```
