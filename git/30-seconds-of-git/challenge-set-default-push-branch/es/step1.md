# Establecer el nombre predeterminado de la rama de empuje

Cuando se empujan cambios a un repositorio remoto, Git usará el nombre de la rama local actual como el nombre predeterminado para la rama remota. Sin embargo, a veces puede que desees empujar tus cambios a una rama diferente. En este caso, tendrías que especificar el nombre de la rama remota explícitamente cada vez que empujes tus cambios. Esto puede ser tedioso y propenso a errores, especialmente si estás trabajando con múltiples ramas.

## Tareas

Para completar este desafío, usarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de una bifurcación de `https://github.com/labex-labs/git-playground.git`. Sigue los pasos siguientes para establecer el nombre predeterminado de la rama de empuje:

1. Clona el repositorio desde `https://github.com/your-username/git-playground.git`.
2. Cambia al directorio del repositorio.
3. Establece el nombre predeterminado de la rama de empuje con el nombre de la rama local actual.
4. Crea una nueva rama llamada `my-branch` y cambia a ella.
5. Crea un nuevo archivo llamado `hello.txt` y escribe la cadena "Hello, World" en él. Agrega el archivo recién creado `hello.txt` al área de preparación de Git y confírmalo, usando el mensaje de confirmación "Add hello.txt" para describir los cambios realizados en esta confirmación.
6. Empuja tus cambios al repositorio remoto. Git empujará tus cambios a una rama llamada `my-branch` en el repositorio remoto.

Este es el resultado de ejecutar `git log`:

```shell

ADD hello.txt
```
