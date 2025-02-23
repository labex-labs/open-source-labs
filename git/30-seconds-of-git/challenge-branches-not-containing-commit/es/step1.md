# Encontrar ramas que no contienen un commit

Estás trabajando en un proyecto con múltiples ramas y necesitas encontrar todas las ramas que no contienen un commit específico. Esto puede ser útil si quieres asegurarte de que un cambio determinado se ha aplicado a todas las ramas, o si quieres saber qué ramas están desactualizadas y necesitan ser actualizadas.

## Tareas

Para este desafío, usaremos el repositorio de Git llamado `https://github.com/your-username/git-playground`.

1. Clona este repositorio en tu máquina local.
2. Una vez que hayas clonado el repositorio, navega hasta el directorio.
3. Crea y cambia a una rama `new-branch` y haz algunos cambios de código en esa rama y luego confirma los cambios, el mensaje de confirmación es "Create a new-branch branch".
4. Verifica el hash del mensaje de confirmación "Create a new-branch branch".
5. Encuentra todas las ramas que no contienen un hash con el mensaje de confirmación "Create a new-branch branch".

Esto devolverá una lista de todas las ramas que no contienen el commit especificado. En este caso, la salida será:

```shell
master
```

Esto significa que la rama `master` no contiene el commit con el hash `31c5ac20129151af1`.
