# Ver ramas fusionadas

Tu tarea es imprimir una lista de todas las ramas locales fusionadas en el repositorio de Git denominado `https://github.com/labex-labs/git-playground`. Necesitarás utilizar el comando `git branch -a --merged` para mostrar la lista de ramas fusionadas. Una vez que tengas la lista, deberías poder navegar por ella utilizando las flechas y salir presionando <kbd>Q</kbd>.

1. Navega hasta el directorio del repositorio:

```shell
cd git-playground
```

2. Ver la lista de ramas fusionadas:

```shell
git branch -a --merged
```

Este es el resultado final:

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
