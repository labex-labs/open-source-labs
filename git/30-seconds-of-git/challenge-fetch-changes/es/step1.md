# Obtener los últimos cambios desde el repositorio remoto

Supongamos que estás trabajando en un proyecto con un equipo de desarrolladores y que el proyecto está almacenado en un repositorio remoto. Quieres obtener los últimos cambios del repositorio remoto sin aplicarlos a tu repositorio local.

## Tareas

Para demostrar cómo obtener los últimos cambios de un repositorio remoto, usaremos el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clona el repositorio y navega hasta el directorio.
2. Encuentra el repositorio `git-playground` en tu cuenta en el sitio web de Github, crea y cambia a una rama llamada `fetch-branch`, crea un archivo llamado `hello.txt`, agrega "hello, world" y confirma con el mensaje "Create hello.txt".
3. Ver las ramas en los repositorios remotos.
4. Obtén los últimos cambios del repositorio remoto.
5. Vuelve a ver las ramas en los repositorios remotos y verifica que se hayan obtenido los últimos cambios.

Este es el resultado de ejecutar `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
