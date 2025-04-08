# Actualizar rama remota después de reescribir el historial

Cuando reescribes el historial localmente, creas un nuevo commit con un hash SHA-1 diferente. Esto significa que el historial de commits en tu rama local es diferente al historial de commits en la rama remota. Si intentas empujar tus cambios a la rama remota, Git rechazará el empuje porque verá el historial de commits como divergido. Para resolver este problema, necesitas forzar una actualización de la rama remota.

Para completar este laboratorio, usarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clona el repositorio `git-playground` en tu máquina local:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Actualiza un commit con el mensaje "Added file2.txt" a un commit con el mensaje "Update file2.txt":

```shell
git commit --amend
```

3. Empuja los cambios de la rama local al repositorio remoto:

```shell
git push
```

4. Si no puedes empujarlo correctamente, forzará el empuje:

```shell
git push -f origin master
```

La bandera `-f` fuerza a Git a actualizar la rama remota con tus cambios, aunque el historial de commits haya divergido.

Este es el resultado final:

```shell

```
