# Enviar Cambios Locales al Repositorio Remoto

Como desarrollador, es posible que necesites enviar tus cambios locales a un repositorio remoto para compartir tu trabajo con otros miembros del equipo o para desplegar tu código en un entorno de producción. El comando `git push` se utiliza para enviar los últimos cambios desde la rama local al repositorio remoto. Sin embargo, antes de enviar los cambios, debes asegurarte de que tu rama local esté actualizada con la rama remota. Si hay conflictos entre las ramas local y remota, debes resolverlos antes de enviar los cambios.

Para completar este laboratorio, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de una bifurcación de `https://github.com/labex-labs/git-playground.git`. Has realizado algunos cambios en la rama `master` y quieres enviarlos al repositorio remoto. Estos son los pasos que debes seguir:

1. Clona el repositorio en tu máquina local y navega hacia el directorio ejecutando los siguientes comandos:

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. Asegúrate de que tu rama local esté actualizada con la rama remota ejecutando el siguiente comando:

```shell
git pull origin master
```

3. Una vez que hayas extraído los últimos cambios de la rama remota, puedes realizar tus cambios en la rama local:

```shell
echo "hello,world" >> file1.txt
```

4. Después de realizar los cambios, preparalos utilizando el comando `git add`:

```shell
git add.
```

5. Confirma los cambios utilizando el comando `git commit`:

```shell
git commit -m "Added new feature"
```

6. Finalmente, envía los cambios al repositorio remoto utilizando el comando `git push`:

```shell
git push origin master
```

Este es el resultado de ejecutar `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
