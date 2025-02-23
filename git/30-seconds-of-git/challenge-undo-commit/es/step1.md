# Deshacer un commit

Supongamos que has realizado un commit en tu repositorio de Git, pero te das cuenta de que contiene un error. Quieres deshacer el commit sin reescribir la historia de tu repositorio. ¿Cómo puedes hacer esto?

## Tareas

Para demostrar cómo deshacer un commit, usaremos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Navega hasta el directorio del repositorio y configura tu identidad de GitHub.
2. Ver el historial de commits.
3. Selecciona un commit con el mensaje "Added file1.txt" y copia su identificador.
4. Revierte el commit y Git abrirá un editor de texto y te permitirá ingresar un mensaje de commit, dejando el mensaje predeterminado en su lugar.
5. Guarda y cierra el editor de texto.
6. Vuelve a ver el historial de commits.

Deberías ver un nuevo commit que deshace los cambios realizados por el commit original.

Este es el resultado de ejecutar el comando `git log`:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
