# Ver un resumen corto de los commits

Como desarrollador, estás trabajando en un proyecto con múltiples colaboradores. Necesitas ver un resumen de todos los commits realizados en el proyecto para entender los cambios que se han hecho y para identificar cualquier problema potencial. Sin embargo, no quieres pasar mucho tiempo buscando entre todos los mensajes de commit para encontrar la información que necesitas.

Para ver un resumen corto de todos los commits realizados en un repositorio de Git, puedes usar el comando `git log --oneline`. Por ejemplo, supongamos que estás trabajando en un proyecto alojado en GitHub llamado `git-playground`.

1. Puedes clonar el repositorio en tu máquina local usando el siguiente comando:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Una vez que hayas clonado el repositorio, navega hasta el directorio del proyecto y ejecuta el siguiente comando para ver un resumen corto de todos los commits:

```shell
cd git-playground
git log --oneline
```

Esto generará una lista de todos los commits realizados en el repositorio, junto con un resumen corto de cada mensaje de commit. Por ejemplo:

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
