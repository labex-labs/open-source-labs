# Restaurar un archivo eliminado

Estás trabajando en un proyecto utilizando Git y accidentalmente eliminaste un archivo llamado `file2.txt` que necesitas. Afortunadamente, conoces el commit en el que se eliminó el archivo. Tu tarea es restaurar el archivo eliminado utilizando Git.

Para completar este laboratorio, utilizarás el repositorio Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Sigue los pasos siguientes:

1. Navega hasta el directorio del repositorio utilizando el comando `cd git-playground`.
2. Ejecuta el comando `git log --oneline` para ver el historial de commits.
3. Identifica un commit en el que se eliminó un archivo con el mensaje "Added file2.txt".
4. Ejecuta el comando `git checkout <commit> -- <file>` para restaurar el `<file>` especificado eliminado en el `<commit>` especificado. Reemplaza `<commit>` con el hash del commit y `<file>` con el nombre del archivo eliminado.

Por ejemplo, si el archivo `file2.txt` fue eliminado en el commit `d22f46b`, ejecutarías el siguiente comando:

```shell
git checkout d22f46b -- file2.txt
```

Esto restaurará el archivo `file2.txt` en tu repositorio local.

Este es el resultado de ejecutar el comando `ll`:

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
