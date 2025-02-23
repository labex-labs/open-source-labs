# Encontrar archivos perdidos

Has estado trabajando en un proyecto en el repositorio `git-playground`. Sin embargo, has notado que algunos archivos están faltando y no estás seguro de cuándo fueron eliminados o cómo recuperarlos. Tu tarea es usar Git para encontrar cualquier archivo y commit perdido en el repositorio.

1. Clona el repositorio `git-playground`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navega al directorio y configura la identidad:

```shell
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

3. Crea y cambia a una rama llamada `one-branch`, elimina `file2.txt` y confirma con el mensaje "Eliminar file2":

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Eliminar file2"
```

4. Vuelve a la rama `master` y elimina la rama `one-branch`:

```shell
git checkout master
git branch -D one-branch
```

5. Ejecuta el comando `git fsck --lost-found` para encontrar cualquier archivo y commit perdido:

```shell
git fsck --lost-found
```

6. Verifica el directorio `.git/lost-found` para ver si se recuperaron archivos perdidos:

```shell
ls.git/lost-found
```

7. Si se encontraron archivos perdidos, revisalos para determinar si son los archivos que faltan.

Este es el resultado de ejecutar el comando `ls.git/lost-found`:

```shell
commit
```
