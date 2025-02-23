# Enviar cambios locales a remoto

Como desarrollador, es posible que necesites enviar tus cambios locales a un repositorio remoto para compartir tu trabajo con otros miembros del equipo o para desplegar tu código en un entorno de producción. Sin embargo, antes de enviar los cambios, debes asegurarte de que tu rama local esté actualizada con la rama remota. Si hay conflictos entre las ramas local y remota, debes resolverlos antes de enviar los cambios.

## Tareas

Para completar este desafío, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Has realizado algunos cambios en la rama `master` y quieres enviarlos al repositorio remoto.

1. Clona el repositorio en tu máquina local desde `https://github.com/your-username/git-playground`, navega hasta el directorio y configura la identidad.
2. Asegúrate de que tu rama local esté actualizada con la rama remota.
3. Después de extraer los últimos cambios de la rama remota, puedes escribir "hello,world" en el archivo `file1.txt` de la rama `master`, agregar la área de preparación y confirmarlo con el mensaje "Added new feature ".
4. Finalmente, envía los cambios al repositorio remoto.

Este es el resultado de ejecutar `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
