# Eliminar ramas fusionadas

Tu tarea es eliminar todas las ramas locales que se han fusionado en la rama `master` del repositorio `https://github.com/labex-labs/git-playground`.

1. Cambia al directorio del repositorio:

```shell
cd git-playground
```

2. Lista todas las ramas locales que se han fusionado en `master`:

```shell
git branch --merged
```

Salida:

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. Elimina todas las ramas fusionadas:

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. Lista todas las ramas nuevamente:

```shell
git branch
```

Este es el resultado final:

```
* master
```
