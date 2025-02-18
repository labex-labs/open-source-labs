# Ver commits (confirmaciones) en un rango de fechas específico

Tu tarea es ver todos los commits (confirmaciones) en un rango de fechas específico utilizando Git. Necesitarás utilizar el comando `git log` con las opciones `--since` y `--until` para especificar el rango de fechas. Puedes utilizar una fecha específica o una fecha relativa (por ejemplo, "hace 12 semanas").

Para completar este reto, necesitarás utilizar el repositorio `https://github.com/labex-labs/git-playground`. Sigue estos pasos:

1. Clona el repositorio en tu máquina local utilizando el comando `git clone https://github.com/labex-labs/git-playground`.
2. Navega al directorio del repositorio utilizando el comando `cd git-playground`.
3. Utiliza el comando `git log --since='Apr 25 2023' --until='Apr 27 2023'` para ver todos los commits (confirmaciones) entre el 25 de abril de 2023 y el 27 de abril de 2023.
4. Utiliza el comando `git log --since='12 weeks ago'` para ver todos los commits (confirmaciones) realizados en las últimas doce semanas.

Este es el resultado final:

```
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
