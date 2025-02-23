# Deshacer un commit

Supongamos que has realizado un commit en tu repositorio de Git, pero te das cuenta de que contiene un error. Quieres deshacer el commit sin reescribir la historia de tu repositorio. ¿Cómo puedes hacer esto?

Para demostrar cómo deshacer un commit, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Siga estos pasos:

1. Clona el repositorio, navega hasta el directorio y configura la identidad:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "tu-nombre-de-usuario"
   git config --global user.email "tu-correo-electrónico"
   ```
2. Ver el historial de commits:
   ```
   git log
   ```
   Deberías ver una lista de commits, cada uno con un identificador único (una larga cadena de letras y números).
3. Selecciona un commit con el mensaje "Added file1.txt" y copia su identificador.
4. Deshaz el commit usando el comando `git revert`:
   ```
   git revert <commit>
   ```
   Reemplaza `<commit>` con el identificador del commit que quieres deshacer.
5. Git abrirá un editor de texto y te permitirá ingresar un mensaje de commit, dejando el mensaje predeterminado en su lugar.
6. Guarda y cierra el editor de texto.
7. Vuelve a ver el historial de commits:
   ```
   git log
   ```
   Deberías ver un nuevo commit que deshace los cambios realizados por el commit original.

Este es el resultado de ejecutar el comando `git log`:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
