# Editar el archivo de configuración de Git

Como desarrollador, es posible que necesites modificar el archivo de configuración de Git para personalizar el comportamiento de Git. El archivo de configuración de Git es un archivo de texto plano que contiene configuraciones en forma de pares clave-valor. El archivo se puede editar con cualquier editor de texto, pero Git proporciona un editor de texto integrado que se puede utilizar para modificar el archivo de configuración.

## Tareas

En este ejemplo, usaremos el repositorio de Git con el nombre `https://github.com/labex-labs/git-playground` en el directorio.

1. Abra la terminal y navegue hasta el directorio del repositorio de Git.
2. Abra el archivo de configuración de Git en el editor de texto de Git.
3. Cambie la configuración para que el nombre de usuario sea `labex_git` y el correo electrónico del usuario sea `labex_git@example.com`.
4. Una vez que haya realizado los cambios necesarios, presione <kbd>Esc</kbd> y escriba el comando <kbd>:wq</kbd>, luego presione <kbd>Enter</kbd> para guardar los cambios y salir del editor.

Este es el resultado una vez finalizado:

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
