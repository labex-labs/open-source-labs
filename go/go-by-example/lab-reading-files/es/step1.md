# Lectura de Archivos

Necesitas leer archivos en tu programa de Go y realizar diferentes operaciones en los datos del archivo.

- Debes estar familiarizado con los conceptos básicos de programación en Go.
- Debes tener Go instalado en tu computadora.

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# A continuación veremos cómo escribir archivos.
```

A continuación está el código completo:

```go
// La lectura y escritura de archivos son tareas básicas necesarias para
// muchos programas de Go. Primero veremos algunos ejemplos de
// lectura de archivos.

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// La lectura de archivos requiere verificar la mayoría de las llamadas en busca de errores.
// Esta función auxiliar simplificará nuestras verificaciones de errores a continuación.
func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Quizás la tarea de lectura de archivos más básica es
	// leer todo el contenido de un archivo en la memoria.
	dat, err := os.ReadFile("/tmp/dat")
	check(err)
	fmt.Print(string(dat))

	// A menudo querrás tener más control sobre cómo y qué
	// partes de un archivo se leen. Para estas tareas, comienza
	// abriendo un archivo para obtener un valor de `os.File`.
	f, err := os.Open("/tmp/dat")
	check(err)

	// Lee algunos bytes desde el principio del archivo.
	// Permite leer hasta 5 pero también anota cuántos
	// se leyeron en realidad.
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// También puedes buscar a una ubicación conocida en el archivo
	// y leer a partir de ahí.
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n", string(b2[:n2]))

	// El paquete `io` proporciona algunas funciones que pueden
	// ser útiles para la lectura de archivos. Por ejemplo, las lecturas
	// como las anteriores se pueden implementar de manera más robusta
	// con `ReadAtLeast`.
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// No hay retroceso integrado, pero `Seek(0, 0)`
	// logra esto.
	_, err = f.Seek(0, 0)
	check(err)

	// El paquete `bufio` implementa un lector bufferizado
	// que puede ser útil tanto por su eficiencia
	// con muchas lecturas pequeñas como por los métodos adicionales
	// de lectura que proporciona.
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))

	// Cierra el archivo cuando hayas terminado (por lo general, esto se
	// programaría inmediatamente después de abrir con `defer`).
	f.Close()
}

```
