# Mover commits a una nueva rama

Para este desafío, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Has estado trabajando en un proyecto en la rama `master`. Te das cuenta de que algunos de los cambios que hiciste deberían haber sido hechos en una rama separada. Quieres mover estos cambios a una nueva rama llamada `feature`.

## Tareas

1. Navega hasta el directorio del repositorio y configura tu identidad de GitHub.
2. Haz checkout de la rama `master`.
3. Crea un archivo llamado `hello.txt`, agrega "hello, world" a él, agréguelo al área de preparación y envíalo con el mensaje "Added hello.txt".
4. Crea una nueva rama llamada `feature` sin cambiar a ella.
5. Deshaz el último commit en `master`.
6. Verifica el historial de commits en la rama `master` y el historial de commits en la rama `feature` para verificar los resultados.

Este es el resultado de ejecutar `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
