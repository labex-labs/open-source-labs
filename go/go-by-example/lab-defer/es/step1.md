# Defer

En este laboratorio, debes utilizar `defer` para crear un archivo, escribir en él y luego cerrarlo cuando hayas terminado.

- La función `createFile` debe crear un archivo con la ruta dada y devolver un puntero al archivo.
- La función `writeFile` debe escribir la cadena "data" en el archivo.
- La función `closeFile` debe cerrar el archivo y comprobar si hay errores.

```sh
# Ejecutar el programa confirma que el archivo se cierra
# después de ser escrito.
$ go run defer.go
creando
escribiendo
cerrando
```

A continuación está el código completo:

```go
// _Defer_ se utiliza para garantizar que una llamada a una función se
// realice más tarde en la ejecución de un programa, por lo general con
// fines de limpieza. `defer` se utiliza a menudo en donde, por ejemplo,
// `ensure` y `finally` se utilizarían en otros lenguajes.

package main

import (
	"fmt"
	"os"
)

// Supongamos que queremos crear un archivo, escribir en él
// y luego cerrarlo cuando hayamos terminado. Aquí está cómo podríamos
// hacerlo con `defer`.
func main() {

	// Inmediatamente después de obtener un objeto de archivo con
	// `createFile`, diferimos el cierre de ese archivo con
	// `closeFile`. Esto se ejecutará al final de la función envolvente (`main`), después
	// de que `writeFile` haya terminado.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creando")
	f, err := os.Create(p)
	if err!= nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("escribiendo")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("cerrando")
	err := f.Close()
	// Es importante comprobar si hay errores al cerrar un
	// archivo, incluso en una función diferida.
	if err!= nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

```
