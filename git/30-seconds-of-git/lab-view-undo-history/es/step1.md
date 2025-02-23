# Ver el historial de "deshacer"

Como desarrollador, es posible que necesites deshacer los cambios que has realizado en tu repositorio de código. Git ofrece varias maneras de deshacer cambios, como utilizar los comandos `git reset` o `git revert`. Sin embargo, puede ser difícil seguir el registro de todas las acciones que has tomado, especialmente si has utilizado comandos más avanzados como `git rebase`. Aquí es donde el comando `git reflog` resulta útil.

El comando `git reflog` muestra el registro de referencias de Git, que es un registro de todas las acciones que has tomado en tu repositorio. Esto incluye no solo los commits, sino también otras acciones como fusiones de ramas, rebases y resets. Al ver el registro de referencias, puedes ver un historial completo de todos los cambios que has realizado en tu repositorio, incluso si no aparecen en el historial de commits.

Para ver el historial de "deshacer" en Git, puedes utilizar el comando `git reflog`. Digamos que has realizado algunos cambios en un repositorio y quieres deshacerlos.

1. Navega al repositorio utilizando la línea de comandos:

```shell
cd git-playground
```

2. Ahora, digamos que te das cuenta de que has cometido un error y quieres deshacer el último commit. Puedes utilizar el comando `git reset` para hacer esto:

```shell
git reset HEAD~1
```

3. Después de ejecutar este comando, es posible que te des cuenta de que has cometido otro error y quieres deshacer el reset. Aquí es donde el comando `git reflog` resulta útil. Puedes utilizarlo para ver el registro de referencias y encontrar el hash del commit anterior:

```shell
git reflog
```

Esto mostrará una lista de todas las acciones que has tomado en el repositorio, incluyendo el reset:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. A partir de esta salida, puedes ver que el hash del commit anterior es `d22f46b`. Puedes utilizar este hash para restablecer el repositorio al commit anterior:

```shell
git reset d22f46b
```

5. Ver los registros históricos de commits para verificar los resultados:

```shell
git log
```
