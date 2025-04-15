# Actualizar rama remota después de reescribir el historial

Cuando reescribes el historial localmente, creas un nuevo commit con un hash SHA-1 diferente. Esto significa que el historial de commits en tu rama local es diferente al historial de commits en la rama remota. Si intentas empujar tus cambios a la rama remota, Git rechazará el empuje porque verá el historial de commits como divergido. Para resolver este problema, debes forzar una actualización de la rama remota.

## Tareas

Para completar este desafío, usarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clona el repositorio `git-playground` en tu máquina local.
2. Actualiza un commit con el mensaje "Added file2.txt" a un commit con el mensaje "Update file2.txt".
3. Empuja los cambios de la rama local al repositorio remoto.
4. Si no puedes empujarlo exitosamente, forzará el empuje.

Este es el resultado final:

```shell
[object Object]
```
