# Eliminar un submódulo

Tienes un repositorio Git que incluye un submódulo llamado `sha1collisiondetection`. Quieres eliminar este submódulo de tu repositorio.

Para esta práctica, usaremos el repositorio Git llamado `https://github.com/git/git`. Este repositorio incluye un submódulo llamado `sha1collisiondetection`.

Para eliminar el submódulo `sha1collisiondetection` del repositorio, sigue estos pasos:

1. Abre tu terminal y navega hasta el directorio raíz de tu repositorio Git:
   ```
   cd git
   ```
2. Ejecuta el siguiente comando para desregistrar el submódulo `sha1collisiondetection`:
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. Ejecuta el siguiente comando para eliminar el directorio del submódulo `sha1collisiondetection`:
   ```
   rm -rf.git/modules/sha1collisiondetection
   ```
4. Ejecuta el siguiente comando para eliminar el árbol de trabajo del submódulo `sha1collisiondetection`:
   ```
   git rm -f sha1collisiondetection
   ```

Después de estos pasos, el submódulo `sha1collisiondetection` se eliminará de tu repositorio Git. Si ejecutas el comando `git submodule status`, no recibirás ninguna información sobre el submódulo.
