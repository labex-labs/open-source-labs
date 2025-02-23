# Extraer los últimos cambios desde el remoto

Estás trabajando en un proyecto con un equipo de desarrolladores y necesitas asegurarte de que tu copia local de la base de código esté actualizada con los últimos cambios realizados por tus compañeros de equipo. Para hacer esto, debes extraer los últimos cambios del repositorio remoto.

Para este laboratorio, usaremos el repositorio de Git llamado `https://github.com/labex-labs/git-playground`. Sigue los pasos siguientes para completar el laboratorio:

1. Cambia al directorio del repositorio clonado:

```shell
cd git-playground
```

2. Extrae los últimos cambios de la rama `master` del repositorio remoto:

```shell
git pull origin master
```

Después de ejecutar el comando `git pull`, deberías ver un mensaje que indique que tu copia local del repositorio está actualizada con el repositorio remoto.

Este es el resultado después de extraer:

![git pull command output](../assets/challenge-pull-changes-step1-1.png)
