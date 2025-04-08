# Fusionar una rama y crear un commit de fusión

Como desarrollador, es posible que necesites fusionar una rama en la rama actual, creando un commit de fusión. Esto puede resultar un poco complicado si no estás familiarizado con Git. El problema consiste en fusionar una rama en la rama actual, creando un commit de fusión, utilizando el repositorio Git denominado `https://github.com/labex-labs/git-playground` en el directorio.

Para este desafío, vamos a utilizar el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clonar un repositorio de `https://github.com/labex-labs/git-playground.git`:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegar hasta el directorio y configurar la identidad:

```shell
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

3. Crear y cambiar a una rama llamada `feature-branch`:

```shell
git checkout -b feature-branch
```

4. Agregar "This is a new line." al archivo `README.md`, agregarlo al área de preparación y confirmarlo, el mensaje de confirmación es "Add new line to README.md":

```shell
echo "This is a new line." >> README.md
git add.
git commit -am "Add new line to README.md"
```

5. Cambiar a la rama `master`:

```shell
git checkout master
```

6. Fusionar la rama `feature-branch` en la rama `master`, lo que creará un commit de fusión con el mensaje "Merge feature-branch":

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

Este es el resultado de ejecutar `git log`:

```shell



ADD new line to README.md
```
