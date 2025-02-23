# Encontrar ramas que contienen un commit

Se te ha dado un repositorio de Git denominado `https://github.com/labex-labs/git-playground`. Tu tarea es encontrar todas las ramas que contengan un hash con el mensaje de commit "Added file2.txt".

1. Cambia al directorio del repositorio:

```shell
cd git-playground
```

2. Utiliza el comando `git branch --contains` para encontrar todas las ramas que contengan un hash con el mensaje de commit "Added file2.txt":

```shell
git branch --contains d22f46b
```

La salida debe ser:

```shell
* master
new-branch
new-branch-1
new-branch-2
```
