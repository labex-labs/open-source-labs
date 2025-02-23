# Eliminar un stash de Git

Tienes un repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Has creado un stash utilizando el comando `git stash save "my stash"`. Ahora, quieres eliminar este stash porque ya no lo necesitas.

1. Cambia al directorio del repositorio utilizando el comando `cd git-playground`.
2. Lista todos los stashes utilizando el comando `git stash list`. Deberías ver el stash que acabas de crear.
3. Elimina el stash utilizando el comando `git stash drop stash@{0}`.
4. Lista todos los stashes nuevamente utilizando el comando `git stash list`.

El stash que acabas de eliminar ya no debería estar allí.
