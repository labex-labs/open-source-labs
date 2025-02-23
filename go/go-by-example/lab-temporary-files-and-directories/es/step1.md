# Archivos y directorios temporales

En este laboratorio, debes crear archivos y directorios temporales en Go.

- Utiliza `os.CreateTemp` para crear un archivo temporal.
- Utiliza `os.MkdirTemp` para crear un directorio temporal.
- Utiliza `os.RemoveAll` para eliminar el directorio temporal.
- Utiliza `os.WriteFile` para escribir datos en un archivo.

```sh
$ go run temporary-files-and-directories.go
Nombre del archivo temporal: /tmp/sample610887201
Nombre del directorio temporal: /tmp/sampledir898854668
```

A continuación está el código completo:

```go
// A lo largo de la ejecución del programa, a menudo queremos crear
// datos que ya no son necesarios una vez que el programa finaliza.
// Los *archivos y directorios temporales* son útiles para este
// propósito ya que no contaminan el sistema de archivos con el tiempo.

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

	// La forma más fácil de crear un archivo temporal es llamando a
	// `os.CreateTemp`. Crea un archivo *y* lo abre para lectura y escritura.
	// Proporcionamos `""` como primer argumento, por lo que `os.CreateTemp`
	// creará el archivo en la ubicación predeterminada de nuestro sistema operativo.
	f, err := os.CreateTemp("", "sample")
	check(err)

	// Muestra el nombre del archivo temporal. En los sistemas operativos
	// basados en Unix, el directorio probablemente será `/tmp`. El nombre
	// del archivo comienza con el prefijo dado como segundo argumento a
	// `os.CreateTemp` y el resto se elige automáticamente para garantizar
	// que las llamadas concurrentes siempre crearán nombres de archivo diferentes.
	fmt.Println("Nombre del archivo temporal:", f.Name())

	// Limpia el archivo una vez que hayas terminado. Es probable que el
	// sistema operativo limpie los archivos temporales por sí solo después
	// de un tiempo, pero es buena práctica hacerlo explícitamente.
	defer os.Remove(f.Name())

	// Podemos escribir algunos datos en el archivo.
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// Si pretendemos escribir muchos archivos temporales, es posible que
	// prefiramos crear un *directorio* temporal. Los argumentos de
	// `os.MkdirTemp` son los mismos que los de `CreateTemp`, pero devuelve
	// un *nombre de directorio* en lugar de un archivo abierto.
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Nombre del directorio temporal:", dname)

	defer os.RemoveAll(dname)

	// Ahora podemos sintetizar nombres de archivos temporales prefijándolos
	// con nuestro directorio temporal.
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}

```
