# Eliminar una rama remota

A veces, es posible que necesites eliminar una rama remota que ya no se necesita. Por ejemplo, si una rama de función se ha fusionado en la rama principal, es posible que desees eliminar la rama de función remota para mantener el repositorio limpio.

## Tareas

Supongamos que se ha clonado un repositorio de GitHub llamado `git-playground` desde tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Quieres eliminar la rama remota llamada `feature-branch` que ya no se necesita.

1. Abre la terminal y navega hasta el directorio del repositorio local.
2. Agrega la rama `feature-branch` al repositorio remoto `origin`.
3. Lista todas las ramas remotas.
4. Elimina la rama remota `feature-branch` en el repositorio remoto `origin`.
5. Verifica que la rama remota se haya eliminado.

La salida no debe incluir la rama remota `feature-branch`:

```
origin/HEAD -> origin/master
origin/master
```
