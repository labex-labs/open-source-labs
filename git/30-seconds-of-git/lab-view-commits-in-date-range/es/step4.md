# Usar fechas relativas y opciones de formato

Git también admite fechas relativas, lo cual puede ser muy conveniente para ver rápidamente la actividad reciente.

Veamos todos los commits de las últimas 12 semanas:

```bash
git log --since='12 weeks ago'
```

Dependiendo de cuándo se ejecute este comando, es posible que vea todos los commits o solo algunos de ellos si se encuentran dentro de ese período de tiempo.

Otros formatos de fechas relativas útiles incluyen:

- `"X days ago"` (hace X días)
- `"X months ago"` (hace X meses)
- `"yesterday"` (ayer)
- `"last week"` (la semana pasada)

Intentemos ver los commits del último año:

```bash
git log --since='1 year ago'
```

Este comando mostrará todos los commits realizados durante el último año.

## Opciones de formato adicionales

El comando `git log` proporciona varias opciones de formato para personalizar la salida. Aquí hay algunas útiles:

1. Para mostrar un registro más conciso con cada commit en una sola línea:

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

La salida se verá así:

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. Para ver los archivos que se cambiaron en cada commit:

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

Este comando muestra el estado de los archivos que se modificaron en cada commit, lo cual puede ser útil para entender qué se cambió.

Estas opciones de formato se pueden combinar con filtros de fecha para crear consultas poderosas que le ayuden a entender mejor la historia de un proyecto.
