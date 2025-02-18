# Rutas de archivos

En este laboratorio (lab), necesitas utilizar el paquete `filepath` para realizar diversas operaciones en rutas de archivos, como construir rutas de manera portable, dividir una ruta en componentes de directorio y archivo, verificar si una ruta es absoluta, encontrar la extensión de un archivo y encontrar una ruta relativa entre dos rutas.

- Utiliza `Join` para construir rutas de manera portable.
- Utiliza `Dir` y `Base` para dividir una ruta en componentes de directorio y archivo.
- Utiliza `IsAbs` para verificar si una ruta es absoluta.
- Utiliza `Ext` para encontrar la extensión de un archivo.
- Utiliza `TrimSuffix` para eliminar la extensión de un nombre de archivo.
- Utiliza `Rel` para encontrar una ruta relativa entre dos rutas.

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

A continuación, se muestra el código completo:

```go
// El paquete `filepath` proporciona funciones para analizar
// y construir *rutas de archivos* de una manera que sea portable
// entre sistemas operativos; `dir/file` en Linux vs.
// `dir\file` en Windows, por ejemplo.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` debe utilizarse para construir rutas de manera
	// portable. Toma cualquier número de argumentos
	// y construye una ruta jerárquica a partir de ellos.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// Siempre debes utilizar `Join` en lugar de
	// concatenar `/` o `\` manualmente. Además de
	// proporcionar portabilidad, `Join` también
	// normalizará las rutas eliminando separadores
	// superfluos y cambios de directorio.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` y `Base` se pueden utilizar para dividir una ruta en el
	// directorio y el archivo. Alternativamente, `Split` devolverá
	// ambos en una misma llamada.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// Podemos verificar si una ruta es absoluta.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// Algunos nombres de archivo tienen extensiones después de un punto. Podemos
	// separar la extensión de estos nombres con `Ext`.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// Para encontrar el nombre del archivo sin la extensión,
	// utiliza `strings.TrimSuffix`.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` encuentra una ruta relativa entre una *base* y un
	// *destino*. Devuelve un error si el destino no se puede
	// hacer relativo a la base.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)
}

```
