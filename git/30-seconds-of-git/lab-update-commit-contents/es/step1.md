# Editar el último commit

Acabas de hacer algunos cambios en tu repositorio de Git, pero te das cuenta de que olvidaste incluir un archivo o hacer un pequeño cambio. No quieres crear un nuevo commit solo por este pequeño cambio, pero tampoco quieres cambiar el mensaje del commit. ¿Cómo puedes editar el último commit sin cambiar su mensaje?

Para demostrar cómo editar el último commit, usemos el repositorio de `https://github.com/labex-labs/git-playground`.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Dáte cuenta de que olvidaste incluir un archivo o hacer un pequeño cambio. Agrega el texto "Nuevo contenido" al final del archivo `README.md`. Agrega cualquier cambio preparado al último commit, sin cambiar su mensaje:

```shell
echo "Nuevo contenido" >> README.md
git add README.md
git commit --amend --no-edit
```

3. Verifica que el último commit ahora incluya los cambios que hiciste:

```shell
git show HEAD
```

Este es el contenido del commit reciente:
![Updated commit contents display](../assets/challenge-update-commit-contents.png)
