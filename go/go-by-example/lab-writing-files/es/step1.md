# Escribiendo archivos

Necesitas escribir un programa en Go que escriba una cadena y bytes en un archivo y utilice escritores con búfer.

- El programa debe escribir una cadena y bytes en un archivo.
- El programa debe utilizar escritores con búfer.

```sh
# Intenta ejecutar el código de escritura de archivos.
$ go run writing-files.go
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes

# Luego, revisa el contenido de los archivos escritos.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# A continuación, veremos cómo aplicar algunas de las ideas
# de E/S de archivos que acabamos de ver a los flujos
# `stdin` y `stdout`.
```

A continuación está el código completo:

```go
// Escribir archivos en Go sigue patrones similares a los
// que vimos anteriormente para la lectura.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Para comenzar, aquí está cómo escribir una cadena (o simplemente
	// bytes) en un archivo.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// Para escrituras más detalladas, abre un archivo para escribir.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// Es habitual deferir un `Close` inmediatamente
	// después de abrir un archivo.
	defer f.Close()

	// Puedes `Escribir` slices de bytes como se esperaría.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// También está disponible un `WriteString`.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// Emitir un `Sync` para vaciar las escrituras en el almacenamiento estable.
	f.Sync()

	// `bufio` proporciona escritores con búfer además
	// de los lectores con búfer que vimos anteriormente.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// Utiliza `Flush` para asegurarte de que todas las operaciones
	// con búfer se hayan aplicado al escritor subyacente.
	w.Flush()

}

```
