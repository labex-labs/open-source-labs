# Fusionar una rama y crear un commit de fusión

Como desarrollador, es posible que necesites fusionar una rama en la rama actual, creando un commit de fusión. Esto puede resultar un poco complicado si no estás familiarizado con Git. El problema consiste en fusionar una rama en la rama actual, creando un commit de fusión, utilizando el repositorio Git con el nombre `https://github.com/labex-labs/git-playground` en el directorio.

## Tareas

Para este desafío, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clonar el repositorio, navegar hasta el directorio y configurar la identidad.
2. Crear y cambiar a una rama llamada `feature-branch`.
3. Agregar "Esta es una nueva línea." al archivo `README.md`, agregarlo al área de preparación y confirmarlo, el mensaje de confirmación es "Agregar nueva línea a README.md".
4. Cambiar a la rama `master`.
5. Fusionar la rama `feature-branch` en la rama `master`, lo que creará un commit de fusión con el mensaje "Fusionar feature-branch".

Este es el resultado de ejecutar `git log`:

```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
