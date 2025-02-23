# Aplicar el último stash

Estás trabajando en un proyecto en tu repositorio Git y has hecho algunos cambios que aún no están listos para ser confirmados. Sin embargo, necesitas cambiar a otra rama o confirmación para trabajar en una característica diferente. No quieres perder tus cambios, así que decides guardarlos en un stash. Más tarde, cuando estés listo para continuar trabajando en tus cambios, necesitarás aplicar el último stash a tu directorio de trabajo.

Para aplicar el último stash a tu repositorio Git, sigue estos pasos:

1. Clona el repositorio Git denominado `https://github.com/labex-labs/git-playground` en tu máquina local.
2. Navega hasta el directorio `git-playground`.
3. Haz algunos cambios al archivo `README.md`, por ejemplo, escribe "Esta es una nueva línea" en el archivo `README.md`.
4. Ejecuta el comando `git stash` para guardar tus cambios.
5. Ejecuta el comando `git stash list` para ver una lista de tus stashes. Deberías ver un stash en la lista.
6. Ejecuta el comando `git stash apply` para aplicar el último stash a tu directorio de trabajo.
7. Verifica el archivo `README.md` para comprobar que tus cambios se han aplicado.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

Este es el resultado de ejecutar `cat README.md`:

```shell
# git-playground
Git Playground
This is a new line
```
