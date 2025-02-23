# Establecer el nombre predeterminado de la rama de empuje

Cuando se empujan cambios a un repositorio remoto, Git utilizará el nombre de la rama local actual como el nombre predeterminado para la rama remota. Sin embargo, a veces es posible que desees empujar tus cambios a una rama diferente. En este caso, tendrías que especificar el nombre de la rama remota explícitamente cada vez que empujes tus cambios. Esto puede ser tedioso y propenso a errores, especialmente si estás trabajando con múltiples ramas.

Para completar este laboratorio, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de una bifurcación de `https://github.com/labex-labs/git-playground.git`. Siga los pasos siguientes para establecer el nombre predeterminado de la rama de empuje:

1. Clona el repositorio utilizando el siguiente comando:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Cambia al directorio del repositorio:
   ```
   cd git-playground
   ```
3. Establece el nombre predeterminado de la rama de empuje como el nombre de la rama local actual:
   ```
   git config push.default current
   ```
4. Crea una nueva rama y cambia a ella:
   ```
   git checkout -b my-branch
   ```
5. Haz algunos cambios en el repositorio y confímalos:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Empuja tus cambios al repositorio remoto:
   ```
   git push -u
   ```
   Git empujará tus cambios a una rama llamada `my-branch` en el repositorio remoto.

Este es el resultado de ejecutar `git log`:

```shell
commit 1f1949959887a1549f1bb5286d3d0a2b993f87e0 (HEAD -> my-branch, origin/my-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add hello.txt
```
