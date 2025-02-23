# Encontrar archivos perdidos

Has estado trabajando en un proyecto en el repositorio `git-playground`. Sin embargo, has notado que algunos archivos están faltando y no estás seguro de cuándo fueron eliminados o cómo recuperarlos. Tu tarea es usar Git para encontrar cualquier archivo y commit perdido en el repositorio.

## Tareas

1. Navega hasta el directorio y configura la identidad.
2. Crea y cambia a una rama llamada `one-branch`, elimina `file2.txt` y confirma con el mensaje "Eliminar file2".
3. Vuelve a la rama `master` y elimina la rama `one-branch`.
4. Encuentra cualquier archivo y commit perdido.
5. Verifica el directorio `.git/lost-found` para ver si se recuperaron archivos perdidos.
6. Si se encontraron archivos perdidos, revisalos para determinar si son los archivos que faltan.

Este es el resultado de ejecutar el comando `ls.git/lost-found`:

```shell
commit
```
