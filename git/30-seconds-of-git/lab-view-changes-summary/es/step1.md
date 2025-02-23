# Ver Cambios Entre Commits

Como desarrollador, has estado trabajando en un proyecto alojado en el repositorio `https://github.com/labex-labs/git-playground`. Has realizado varios commits en el repositorio y quieres ver un resumen de los cambios entre dos commits específicos. Sin embargo, no estás seguro de cómo hacerlo utilizando Git.

Para ver un resumen de los cambios entre dos commits, digamos que quieres ver los cambios entre el commit `HEAD` y el commit con el mensaje "Initial commit". Aquí está cómo puedes hacerlo:

1. Abre una ventana de terminal y navega hasta el directorio donde se encuentra el repositorio `git-playground`:

```
cd git-playground
```

2. Ejecuta el siguiente comando:

```
git shortlog 3050fc0de..HEAD
```

Git mostrará un resumen de los cambios entre los dos commits. Puedes usar las flechas para navegar por el resumen y presionar `Q` para salir.

Aquí está un ejemplo de cómo podría ser la salida:

```shell
Hang (2):
      Added file1.txt
      Added file2.txt
```

En este ejemplo, Git está mostrando que hubo dos commits entre el commit `3050fc0de` y el commit `HEAD`. El primer commit agregó `file1.txt` y el segundo commit agregó `file2.txt`.
