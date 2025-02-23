# Eliminar archivos del área de preparación

Estás trabajando en un proyecto en el repositorio `git-playground`. Has realizado algunos cambios en los archivos y los has agregado al área de preparación usando el comando `git add`. Sin embargo, te das cuenta de que accidentalmente has agregado un archivo que no quieres comitear. Necesitas eliminar este archivo del área de preparación.

1. Ver el estado del directorio de trabajo actual:

```shell
git status
```

2. Eliminar el archivo `newfile.txt` del área de preparación usando el comando `git restore --staged`:

```shell
git restore --staged newfile.txt
```

3. Verificar que el archivo ha sido eliminado del área de preparación usando el comando `git status`:

```shell
git status
```

Este es el resultado final:

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
