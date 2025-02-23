# Deshacer el último commit

Acabas de hacer un commit con cambios en tu repositorio de Git, pero te das cuenta de que cometiste un error. Quieres deshacer el último commit sin perder ninguno de los cambios que hiciste. ¿Cómo puedes hacer esto?

Para esta práctica, vamos a usar el repositorio de `https://github.com/labex-labs/git-playground`. Sigue estos pasos:

1. Clona el repositorio, navega hasta el directorio y configura la identidad:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "tu-nombre-de-usuario"
git config --global user.email "tu-correo-electrónico"
```

2. Verifica el historial de commits:

```shell
git log
```

3. Deshaz el último commit, creando un nuevo commit con los cambios inversos del commit:

```shell
git revert HEAD
```

4. Verifica el historial de commits nuevamente:

```shell
git log
```

Este es el resultado de ejecutar el comando `git log --oneline`:

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
