# Eliminar una rama

Has creado una rama local en tu repositorio de Git y ya no la necesitas. Quieres eliminar la rama para mantener tu repositorio limpio y organizado.

1. Navega hasta el repositorio clonado:

```shell
cd git-playground
```

2. Ver las ramas actuales:

```shell
git branch
```

3. Elimina la rama `feature-1`:

```shell
git branch -d feature-1
```

4. Verifica que la rama haya sido eliminada:

```shell
git branch
```

Este es el resultado de ejecutar el comando `git branch`:

```
* master
```
