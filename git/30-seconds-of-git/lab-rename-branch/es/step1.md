# Renombrar una rama

Como desarrollador, es posible que necesites renombrar una rama por varios motivos, como para que sea más descriptiva o para seguir una convención de nombres. Renombrar una rama puede ser una tarea sencilla, pero requiere algunos conocimientos de comandos de Git. En este desafío, aprenderás cómo renombrar una rama usando Git.

Para este laboratorio, usaremos el repositorio de Git denominado `https://github.com/labex-labs/git-playground`.

Supongamos que crearás una rama llamada `old-branch` para trabajar en una nueva característica. Después de completar la característica, te das cuenta de que el nombre de la rama no es lo suficientemente descriptivo. Quieres renombrar la rama a `new-branch` para que tenga más sentido. Para renombrar la rama, sigue estos pasos:

1. Abre la terminal y navega hasta el directorio del repositorio local.
2. Utiliza el comando `git checkout -b old-branch` para crear una rama llamada `old-branch` y el comando `git branch -m <nombre-antiguo> <nombre-nuevo>` para renombrar la rama. En nuestro ejemplo, el comando sería `git branch -m old-branch new-branch`.
3. Verifica que la rama haya sido renombrada utilizando el comando `git branch`.

La salida debe mostrar el nuevo nombre de la rama:

```shell
master
* new-branch
```
