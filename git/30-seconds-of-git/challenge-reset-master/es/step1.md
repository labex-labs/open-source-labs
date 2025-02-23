# Restablecer la rama local master para que coincida con la remota

Has estado trabajando en un proyecto y has realizado cambios en la rama local `master`. Sin embargo, te das cuenta de que la rama remota `master` ha sido actualizada con nuevos cambios que no tienes en tu rama local. Necesitas restablecer la rama local `master` para que coincida con la de la remota.

## Tareas

1. Cambiar a la rama `master`.
2. Recuperar las últimas actualizaciones desde la rama remota.
3. Ver el historial de commits de la rama actual.
4. Restablecer la rama local `master` para que coincida con la de la remota.
5. Verificar que la rama local `master` está ahora actualizada con la rama remota `master`.

Este es el resultado final:

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
