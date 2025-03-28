# Clonar submódulos faltantes

Estás trabajando en un proyecto que contiene submódulos. Cuando clonas el proyecto, los submódulos no se clonan automáticamente. Esto causa problemas al intentar construir o ejecutar el proyecto. Necesitas clonar los submódulos faltantes y hacer checkout de los commits correctos.

## Tareas

Para este desafío, usaremos el repositorio Git denominado `https://github.com/git/git`. Este repositorio contiene submódulos que no se clonan automáticamente cuando se clona el repositorio.

Para clonar los submódulos faltantes y hacer checkout de los commits correctos, sigue estos pasos:

1. Cambia al directorio del repositorio.
2. Inicializa los submódulos.
3. Haz checkout a el commit correcto del submódulo, es decir, a la rama `master`.

Aquí está el resultado final:

```shell
Submodule'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
