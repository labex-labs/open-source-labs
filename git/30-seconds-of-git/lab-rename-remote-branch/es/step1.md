# Renombrar una rama remota

Para completar este laboratorio, utilizarás el repositorio Git `git-playground` de tu cuenta de GitHub, que proviene de un fork de `https://github.com/labex-labs/git-playground.git`. Por favor, desmarca "Copiar solo la rama master" al hacer el fork.

Tienes un repositorio Git llamado `https://github.com/your-username/git-playground`. Has creado una rama llamada `feature-branch` y la has empujado al remoto. Ahora quieres renombrar la rama a `new-feature-1` tanto localmente como en el remoto.

1. Clona el repositorio, navega hasta el directorio y configura la identidad:
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Cambia a la rama llamada `feature-branch`:
   ```shell
   git checkout feature-branch
   ```
3. Renombra la rama tanto localmente como en el remoto:
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Verifica que la rama haya sido renombrada:
   ```shell
   git branch -a
   ```

Este es el resultado de ejecutar `git branch -a`:

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
