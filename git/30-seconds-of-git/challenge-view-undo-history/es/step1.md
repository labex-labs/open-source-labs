# Ver el historial de "Deshacer"

Como desarrollador, es posible que necesites deshacer los cambios que has realizado en tu código base. Git ofrece varias maneras de deshacer cambios, como utilizar los comandos `git reset` o `git revert`. Sin embargo, puede ser difícil de seguir el registro de todas las acciones que has realizado, especialmente si has utilizado comandos más avanzados como `git rebase`.

## Tareas

Digamos que has realizado algunos cambios en un repositorio y quieres deshacerlos.

1. Navega hasta el repositorio.
2. Ahora, te das cuenta de que has cometido un error y quieres deshacer el último commit.
3. Puedes darte cuenta de que has cometido otro error y quieres deshacer el reset. Ver el registro de referencias y encontrar el hash del commit anterior.
4. Puedes ver que el hash del commit anterior es `d22f46b` y utilizar este hash para restablecer el repositorio al commit anterior.
5. Ver los registros históricos de commits para verificar los resultados.

A continuación se muestra el resultado del paso 3. Esto mostrará una lista de todas las acciones que has realizado en el repositorio, incluyendo el reset:

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```
