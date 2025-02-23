# Directorios

Crea un programa en Go que cree un nuevo subdirectorio en el directorio de trabajo actual, cree una jerarquía de directorios, incluyendo los padres, liste el contenido del directorio, cambie el directorio de trabajo actual y visite un directorio de forma recursiva.

## Requisitos

- Crea un nuevo subdirectorio en el directorio de trabajo actual.
- Cuando se crean directorios temporales, es buena práctica `deferir` su eliminación. `os.RemoveAll` eliminará todo un árbol de directorios (similar a `rm -rf`).
- Crea una jerarquía de directorios, incluyendo los padres con `MkdirAll`. Esto es similar al comando de línea `mkdir -p`.
- `ReadDir` lista el contenido del directorio, devolviendo una slice de objetos `os.DirEntry`.
- `Chdir` nos permite cambiar el directorio de trabajo actual, similar a `cd`.
- Visita un directorio de forma recursiva, incluyendo todos sus subdirectorios. `Walk` acepta una función de devolución de llamada para manejar cada archivo o directorio visitado.

## Ejemplo

```sh
$ go run directories.go
Listando subdir/parent
child true
file2 false
file3 false
Listando subdir/parent/child
file4 false
Visitando subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
