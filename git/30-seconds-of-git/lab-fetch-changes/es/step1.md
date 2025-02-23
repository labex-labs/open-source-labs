# Obtener los últimos cambios desde el repositorio remoto

Supongamos que estás trabajando en un proyecto con un equipo de desarrolladores y que el proyecto está almacenado en un repositorio remoto. Quieres obtener los últimos cambios del repositorio remoto sin aplicarlos a tu repositorio local. Aquí es donde entra en útil el comando `git fetch`.

El comando `git fetch` descarga los últimos cambios del repositorio remoto a tu repositorio local, pero no los aplica a tu directorio de trabajo. Esto significa que puedes revisar los cambios antes de fusionarlos en tu repositorio local.

Para demostrar cómo obtener los últimos cambios de un repositorio remoto, usaremos el repositorio de Git `git-playground` de tu cuenta de GitHub, que proviene de una bifurcación de `https://github.com/labex-labs/git-playground.git`. Sigue los pasos siguientes:

1. Clona el repositorio y navega hasta el directorio:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Encuentra el repositorio `git-playground` en tu cuenta en el sitio web de Github, crea y cambia a una rama llamada `fetch-branch`, crea un archivo llamado `hello.txt`, agrega "hello, world" y confirma con el mensaje "Create hello.txt".
3. Ver las ramas en los repositorios remotos:

```shell
git branch -r
```

4. Obtén los últimos cambios del repositorio remoto:

```shell
git fetch
```

5. Vuelve a ver las ramas en los repositorios remotos y verifica que se hayan obtenido los últimos cambios:

```shell
git branch -r
git log origin/fetch-branch
```

Esto te mostrará los últimos commits en la rama `origin/fetch-branch`.Este es el resultado de ejecutar `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
