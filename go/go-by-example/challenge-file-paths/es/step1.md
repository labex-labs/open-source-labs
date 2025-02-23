# Rutas de Archivo

En este desafío, debes utilizar el paquete `filepath` para realizar diversas operaciones en rutas de archivo, como construir rutas de manera portable, dividir una ruta en componentes de directorio y archivo, comprobar si una ruta es absoluta, encontrar la extensión de un archivo y encontrar una ruta relativa entre dos rutas.

## Requisitos

- Utiliza `Join` para construir rutas de manera portable.
- Utiliza `Dir` y `Base` para dividir una ruta en componentes de directorio y archivo.
- Utiliza `IsAbs` para comprobar si una ruta es absoluta.
- Utiliza `Ext` para encontrar la extensión de un archivo.
- Utiliza `TrimSuffix` para quitar la extensión de un nombre de archivo.
- Utiliza `Rel` para encontrar una ruta relativa entre dos rutas.

## Ejemplo

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```
