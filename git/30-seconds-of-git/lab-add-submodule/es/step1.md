# Agregar un submódulo

Tu tarea es agregar un nuevo submódulo a un repositorio Git. Necesitarás usar el comando `git submodule add` para agregar el submódulo desde un repositorio remoto a un directorio local en tu repositorio. La sintaxis del comando es la siguiente:

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` es la URL o la ruta al repositorio remoto que quieres agregar como submódulo.
- `<local-path>` es la ruta donde quieres almacenar el submódulo en tu repositorio local.

Supongamos que tienes un repositorio Git llamado `my-project` y quieres agregar un submódulo del repositorio Git `https://github.com/labex-labs/git-playground.git` a un directorio llamado `git-playground` en tu repositorio local. Aquí te muestra cómo hacerlo:

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git./git-playground
```

Este es el resultado después de completar el laboratorio:

![Git submodule add result](../assets/challenge-add-submodule-step1-1.png)
