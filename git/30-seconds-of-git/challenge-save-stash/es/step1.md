# Crear un stash de Git

Como desarrollador, es posible que te encuentres en una situación en la que necesites cambiar a una rama diferente o trabajar en una característica diferente, pero aún no estés listo para confirmar tus cambios. No quieres perder tu progreso, pero tampoco quieres confirmar código incompleto o con errores. Aquí es donde un stash resulta muy útil.

Un stash te permite guardar tus cambios sin confirmarlos, de modo que puedas cambiar a una rama diferente o trabajar en una característica diferente. Luego, puedes aplicar tu stash más tarde cuando estés listo para continuar trabajando en tus cambios.

## Tareas

Digamos que estás trabajando en una rama llamada `feature` en el repositorio `git-playground` y quieres guardar tus cambios antes de cambiar a una rama diferente:

1. Primero, navega hasta el directorio `git-playground`.
2. Cambia a una rama llamada `feature`.
3. Agrega la línea "Algunos cambios" al archivo `README.md`.
4. Guarda tus cambios en un stash y agrega un mensaje descriptivo "Mis cambios" a ese stash.
5. Cambia a una rama diferente.
6. Cuando hayas terminado de hacer cambios en la otra rama, regresa a la rama `feature` y aplica tu stash.

Este es el resultado final:

```shell
stash@{0}: On feature: My changes
```
