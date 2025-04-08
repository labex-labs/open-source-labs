# Restablecer la rama local master para que coincida con la remota

Has estado trabajando en un proyecto y has realizado cambios en la rama local `master`. Sin embargo, te das cuenta de que la rama remota `master` ha sido actualizada con nuevos cambios que no tienes en tu rama local. Necesitas restablecer la rama local `master` para que coincida con la de la rama remota.

1. Cambia a la rama `master`:
   ```shell
   git checkout master
   ```
2. Recupera las últimas actualizaciones de la rama remota:
   ```shell
   git fetch origin
   ```
3. Muestra el historial de commits de la rama actual:
   ```shell
   git log
   ```
4. Restablece la rama local `master` para que coincida con la de la rama remota:
   ```shell
   git reset --hard origin/master
   ```
5. Verifica que la rama local `master` esté ahora actualizada con la rama remota `master`:
   ```shell
   git log
   ```

Este es el resultado final:

```shell

```
