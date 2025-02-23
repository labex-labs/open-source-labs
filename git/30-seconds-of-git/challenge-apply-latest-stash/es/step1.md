# Aplicar el último stash

Estás trabajando en un proyecto en tu repositorio de Git y has hecho algunos cambios que aún no están listos para ser confirmados. Sin embargo, necesitas cambiar a otra rama o confirmación para trabajar en una característica diferente. No quieres perder tus cambios, así que decides guardarlos en un stash. Más tarde, cuando estés listo para continuar trabajando en tus cambios, necesitas aplicar el último stash a tu directorio de trabajo.

## Tareas

Para aplicar el último stash a tu repositorio de Git, sigue estos pasos:

1. Lista tus stashes. Deberías ver un stash en la lista.
2. Aplica el último stash a tu directorio de trabajo.
3. Verifica el archivo `README.md` para comprobar que tus cambios se han aplicado.

Este es el resultado de ejecutar el comando `cat README.md`:

![README file changes applied](../assets/challenge-apply-latest-stash-step1-1.png)

Este comando vuelve a aplicar los cambios guardados en el último stash al directorio de trabajo actual, y agrega la nueva línea "Esta es una nueva línea" al archivo `README.md`.
