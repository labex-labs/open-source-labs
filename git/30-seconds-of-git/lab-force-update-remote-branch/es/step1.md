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
commit b8c530558ecd004156dd05ac7d22d8cf07b2c28e (HEAD -> master, origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Update file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
