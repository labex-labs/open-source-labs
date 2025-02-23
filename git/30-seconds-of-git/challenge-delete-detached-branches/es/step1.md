# Eliminar ramas desatadas

Tienes un repositorio Git con varias ramas desatadas que ya no necesitas. Estas ramas están desordenando tu repositorio y dificultando su gestión. Quieres eliminar todas las ramas desatadas para limpiar tu repositorio.

## Tareas

Para completar este desafío, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. No marque "Copiar solo la rama master".

1. Clona el repositorio, navega hasta el directorio y configura la identidad.
2. Dado que hay una rama `feature-branch` en el repositorio remoto, cambia a `feature-branch`, lo que hará que la `feature-branch` local siga la rama `feature-branch` del repositorio remoto y elimina la rama `feature-branch` en el repositorio remoto.
3. Muestra la relación de seguimiento entre las ramas locales y las ramas remotas que siguen.
4. Vuelve a cambiar a la rama `master`.
5. Elimina todas las ramas desatadas de tu repositorio local.
6. Verifica que las ramas desatadas hayan sido eliminadas.

La salida solo debe mostrar las ramas que están asociadas a una rama específica:

```shell
* master d22f46b [origin/master] Added file2.txt
```
