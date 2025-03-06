# Ver commits en un rango de fechas específico

Ahora aprenderemos cómo filtrar commits basados en fechas específicas. Git proporciona dos opciones útiles para este propósito:

- `--since` o `--after`: Muestra los commits más recientes que una fecha específica
- `--until` o `--before`: Muestra los commits más antiguos que una fecha específica

Cuando combinamos estas opciones, podemos ver los commits dentro de un rango de fechas específico.

Veamos todos los commits que ocurrieron entre el 25 de abril de 2023 y el 27 de abril de 2023:

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

Este comando mostrará todos los commits que se hicieron entre el 25 y el 27 de abril de 2023. La salida debería verse así:

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

Git acepta muchos formatos de fecha, incluyendo:

- `"YYYY-MM-DD"` (por ejemplo, `2023-04-25`)
- `"Month DD YYYY"` (por ejemplo, `Apr 25 2023`)
- `"DD Month YYYY"` (por ejemplo, `25 Apr 2023`)

Pruebe otro formato de fecha para ver si hay algún commit dentro de un rango diferente:

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

Es posible que este comando no devuelva ningún resultado si no hubo commits durante ese período, lo cual es perfectamente normal.
