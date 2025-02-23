# Eliminar un archivo del último commit

Has agregado un archivo al último commit que no pretendías incluir. Quieres eliminar el archivo del último commit sin cambiar su mensaje.

## Tareas

Para este desafío, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`. Supongamos que tienes un repositorio de Git llamado `git-playground` con un archivo llamado `file2.txt` que accidentalmente agregaste al último commit.

1. Navega hasta el directorio del repositorio y configura tu identidad de GitHub.
2. Elimina el archivo `file2.txt` especificado del índice.
3. Actualiza el contenido del último commit, sin cambiar su mensaje.

Después de ejecutar estos comandos, el archivo `file2.txt` se eliminará del último commit sin cambiar su mensaje.

Esto es lo que sucede cuando se elimina `file2.txt` del control de versiones de Git:

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
