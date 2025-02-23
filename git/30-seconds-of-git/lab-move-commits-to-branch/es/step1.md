# Mover commits a una nueva rama

Para este laboratorio, usemos el repositorio de `https://github.com/labex-labs/git-playground`. Has estado trabajando en un proyecto en la rama `master`. Te das cuenta de que algunos de los cambios que hiciste deberían haber sido hechos en una rama separada. Quieres mover estos cambios a una nueva rama llamada `feature`.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Haz checkout de la rama `master`:

```shell
git checkout master
```

3. Crea un archivo llamado `hello.txt`, agrega "hello, world" a él, agréguelo al área de preparación y envíalo con el mensaje "Agregado hello.txt":

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "Agregado hello.txt"
```

4. Crea una nueva rama llamada `feature` sin cambiar a ella. Cuando creas una nueva rama en la rama `master`, el estado de la nueva rama es el mismo que el de la rama `master`, es decir, los archivos en la nueva rama son los mismos que los archivos en la rama `master`, con el mismo contenido y historial de versiones:

```shell
git branch feature
```

5. Deshace el último commit en `master`:

```shell
git reset HEAD~1 --hard
```

6. Verifica el historial de commits en la rama `master` y el historial de commits en la rama `feature` para verificar los resultados:

```shell
git log
git checkout feature
git log
```

Este es el resultado de ejecutar `git log`:

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Agregado hello.txt
```
