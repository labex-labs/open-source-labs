# Directorios

Cree un programa de Go que cree un nuevo subdirectorio en el directorio de trabajo actual, cree una jerarquía de directorios, incluyendo padres, liste el contenido del directorio, cambie el directorio de trabajo actual y visite un directorio de forma recursiva.

- Cree un nuevo subdirectorio en el directorio de trabajo actual.
- Cuando se crean directorios temporales, es buena práctica `deferir` su eliminación. `os.RemoveAll` eliminará todo un árbol de directorios (similar a `rm -rf`).
- Cree una jerarquía de directorios, incluyendo padres con `MkdirAll`. Esto es similar al comando de línea `mkdir -p`.
- `ReadDir` lista el contenido del directorio, devolviendo una slice de objetos `os.DirEntry`.
- `Chdir` nos permite cambiar el directorio de trabajo actual, similar a `cd`.
- Visite un directorio de forma recursiva, incluyendo todos sus subdirectorios. `Walk` acepta una función de devolución de llamada para manejar cada archivo o directorio visitado.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

A continuación está el código completo:

```go
// Go tiene varias funciones útiles para trabajar con
// *directorios* en el sistema de archivos.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Cree un nuevo subdirectorio en el directorio de trabajo
	// actual.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// Cuando se crean directorios temporales, es buena
	// práctica `deferir` su eliminación. `os.RemoveAll`
	// eliminará todo un árbol de directorios (similar a
	// `rm -rf`).
	defer os.RemoveAll("subdir")

	// Función auxiliar para crear un nuevo archivo vacío.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// Podemos crear una jerarquía de directorios, incluyendo
	// padres con `MkdirAll`. Esto es similar al
	// comando de línea `mkdir -p`.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` lista el contenido del directorio, devolviendo una
	// slice de objetos `os.DirEntry`.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` nos permite cambiar el directorio de trabajo actual,
	// similar a `cd`.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// Ahora veremos el contenido de `subdir/parent/child`
	// al listar el *directorio actual*.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` de vuelta a donde comenzamos.
	err = os.Chdir("../../..")
	check(err)

	// También podemos visitar un directorio *recursivamente*,
	// incluyendo todos sus subdirectorios. `Walk` acepta
	// una función de devolución de llamada para manejar cada archivo o
	// directorio visitado.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` se llama para cada archivo o directorio encontrado
// recursivamente por `filepath.Walk`.
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```
