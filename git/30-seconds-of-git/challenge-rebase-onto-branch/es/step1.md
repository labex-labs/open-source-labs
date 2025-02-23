# Rebase sobre otra rama

Como desarrollador, estás trabajando en un proyecto con múltiples ramas. Has realizado cambios en tu rama y quieres incorporar esos cambios a otra rama. Sin embargo, no quieres fusionar las ramas porque quieres mantener un historial limpio y lineal.

## Tareas

Para este desafío, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio y configura la identidad.
2. Crea y cambia a una rama llamada `one-branch`.
3. Agrega "hello,world" al archivo `README.md`, agréguelo al área de preparación y confirma los cambios con el mensaje "Added some changes to README.md".
4. Cambia a la rama `master`.
5. Asegúrate de que tu rama local `master` esté actualizada con el repositorio remoto.
6. Rebasa la rama `one-branch` sobre la rama `master`.
7. Resuelve cualquier conflicto que surja durante el proceso de rebase.

Este es el resultado de ejecutar `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
