# Encuentra los commits que manipularon una cadena específica

Como desarrollador, es posible que necesites encontrar todos los commits que modificaron una cadena específica en tu código base. Por ejemplo, es posible que desees encontrar todos los commits que agregaron o eliminaron un nombre de función o variable específica. Esto puede ser útil al depurar problemas o localizar la fuente de un error.

Supongamos que estás trabajando en un proyecto alojado en GitHub llamado `git-playground`. Quieres encontrar todos los commits que modificaron la cadena "Git Playground" en el archivo `README.md`. Aquí está cómo puedes hacerlo:

1. Navega hasta el directorio del repositorio:

```shell
cd git-playground
```

2. Utiliza el comando `git log -S` para encontrar todos los commits que modificaron la cadena "Git Playground" en el archivo `README.md` y utiliza las flechas para navegar por la lista de commits. Presiona <kbd>Q</kbd> para salir del registro:

```shell
git log -S"Git Playground" README.md
```

Git mostrará una lista de todos los commits que modificaron la cadena "Git Playground" en el archivo `README.md`:

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
