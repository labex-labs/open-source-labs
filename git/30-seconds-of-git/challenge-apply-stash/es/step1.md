# Aplicar un stash

Estás trabajando en una rama de función en el repositorio `git-playground` y necesitas cambiar a otra rama para trabajar en la corrección de un error. Sin embargo, tienes algunos cambios que no están listos para ser confirmados aún. Quieres guardar estos cambios y cambiar a la otra rama. Una vez que hayas terminado con la corrección del error, quieres aplicar el stash y continuar trabajando en tu rama de función.

## Tareas

Los cambios se han guardado en la rama `feature-branch`, y el mensaje del stash es "mis cambios".

1. Cambia al directorio `git-playground`.
2. Cambia a la rama `master` y guárdala después de corregir el error, el mensaje del stash es "corregir el error". Corrige el error actualizando el contenido del archivo `file1.txt` a "hello,world".
3. Cambia a la rama `feature-branch`, mira la lista de stashes y aplica el stash cuya información es "mis cambios".

Este es el contenido del archivo `README.md`:

```
# git-playground
Git Playground
some changes
```

Deberías ver que los cambios que hiciste antes de guardar el stash ahora se han aplicado.
