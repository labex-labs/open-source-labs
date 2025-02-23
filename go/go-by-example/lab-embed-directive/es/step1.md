# Directiva de incrustación

Su tarea es modificar el código dado para incrustar archivos y carpetas en el binario de Go e imprimir su contenido.

- Debe usar el paquete `embed` para incrustar archivos y carpetas.
- Debe usar los tipos `string` y `[]byte` para almacenar el contenido de los archivos incrustados.
- Debe usar el tipo `embed.FS` para incrustar múltiples archivos o carpetas con comodines.
- Debe imprimir el contenido de los archivos incrustados.

```sh
# Use estos comandos para ejecutar el ejemplo.
# (Nota: debido a la limitación en el playground de Go,
# este ejemplo solo se puede ejecutar en su máquina local.)
$ mkdir -p carpeta
$ echo "hola go" > carpeta/archivo_simple.txt
$ echo "123" > carpeta/archivo1.hash
$ echo "456" > carpeta/archivo2.hash

$ go run incrustar-directiva.go
hola go
hola go
123
456
```

A continuación está el código completo:

```go
// `//go:embed` es una [directiva del compilador](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives) que
// permite que los programas incluyan archivos y carpetas arbitrarios en el binario de Go en
// tiempo de compilación. Lea más sobre la directiva de incrustación
// [aquí](https://pkg.go.dev/incrustación).
package principal

// Importe el paquete `embed`; si no utiliza ningún identificador exportado
// de este paquete, puede hacer una importación en blanco con `_ "embed"`.
import (
	"incrustación"
)

// Las directivas `embed` aceptan rutas relativas al directorio que contiene el
// archivo fuente de Go. Esta directiva incrusta el contenido del archivo en la
// variable `string` que le sigue inmediatamente.
//
//go:embed carpeta/archivo_simple.txt
var archivoCadena string

// O incrusta el contenido del archivo en un `[]byte`.
//
//go:embed carpeta/archivo_simple.txt
var archivoByte []byte

// También podemos incrustar múltiples archivos o incluso carpetas con comodines. Esto utiliza
// una variable del tipo [embed.FS](https://pkg.go.dev/incrustación#FS), que
// implementa un sistema de archivos virtual simple.
//
//go:embed carpeta/archivo_simple.txt
//go:embed carpeta/*.hash
var carpeta incrustación.FS

func principal() {

	// Imprima el contenido de `archivo_simple.txt`.
	imprimir(archivoCadena)
	imprimir(string(archivoByte))

	// Recupere algunos archivos de la carpeta incrustada.
	contenido1, _ := carpeta.LeerArchivo("carpeta/archivo1.hash")
	imprimir(string(contenido1))

	contenido2, _ := carpeta.LeerArchivo("carpeta/archivo2.hash")
	imprimir(string(contenido2))
}

```
