# Rebase sobre otra rama

Como desarrollador, estás trabajando en un proyecto con múltiples ramas. Has realizado cambios en tu rama y quieres incorporar esos cambios a otra rama. Sin embargo, no quieres fusionar las ramas porque quieres mantener un historial limpio y lineal. En este caso, puedes usar el comando `git rebase` para rebasar tu rama sobre otra rama.

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Siga los pasos siguientes para completar el laboratorio:

1. Clonar el repositorio, navegar al directorio y configurar la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "su-nombre-de-usuario"
git config --global user.email "su-correo-electrónico"
```

2. Crear y cambiar a una rama llamada `one-branch`:

```shell
git checkout -b one-branch
```

3. Agregar "hello,world" al archivo `README.md`, agregarlo al área de preparación y confirmarlo con el mensaje "Agregados algunos cambios a README.md":

```shell
echo "hello,world" >> README.md
git add.
git commit -am "Agregados algunos cambios a README.md"
```

4. Cambiar a la rama `master`:

```shell
git checkout master
```

5. Asegurarse de que su rama local `master` esté actualizada con el repositorio remoto:

```shell
git pull
```

6. Rebasar la rama `one-branch` sobre la rama `master`:

```shell
git rebase one-branch
```

7. Resolver cualquier conflicto que surja durante el proceso de rebase.

Este es el resultado de ejecutar `git log`:

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Agregados algunos cambios a README.md
```
