# Deshacer el último commit

Acabas de hacer un commit con los cambios en tu repositorio de Git, pero te das cuenta de que cometiste un error. Quieres deshacer el último commit sin perder ninguno de los cambios que hiciste. ¿Cómo puedes hacer esto?

## Tareas

Para este desafío, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`.

1. Verifica el historial de commits.
2. Deshaz el último commit, creando un nuevo commit con la inversa de los cambios del commit.

Este es el resultado de ejecutar el comando `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
