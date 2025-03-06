# Explorar el comando básico `git log`

Ahora que hemos clonado nuestro repositorio, aprendamos cómo ver el historial de commits (confirmaciones) utilizando el comando `git log`.

El comando `git log` muestra una lista de todos los commits en el repositorio, comenzando por el más reciente. Cada entrada de commit incluye:

- Un hash (identificador) de commit único
- Información del autor
- Fecha y hora del commit
- Mensaje del commit

Veamos el historial básico de commits:

```bash
git log
```

Debería ver una salida similar a la siguiente:

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

Si la salida es larga, puede navegar por ella utilizando:

- Presione `Space` para avanzar
- Presione `b` para retroceder
- Presione `q` para salir de la vista del log

Tenga en cuenta que cada commit tiene un identificador único (la larga cadena hexadecimal), la información del autor, la fecha y hora del commit y un mensaje que describe los cambios realizados.
