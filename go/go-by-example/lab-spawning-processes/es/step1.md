# Creación de Procesos

El laboratorio requiere la implementación de un programa de Go que cree procesos externos y recopile su salida.

- El programa debe ser capaz de crear procesos externos.
- El programa debe ser capaz de recopilar la salida de los procesos externos.
- El programa debe manejar los errores que pueden surgir durante la ejecución de los procesos externos.

```sh
# Los programas creados devuelven una salida que es la misma
# que si los hubiéramos ejecutado directamente desde la línea de comandos.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date no tiene una bandera `-x` por lo que saldrá con
# un mensaje de error y un código de retorno no nulo.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

A continuación se muestra el código completo:

```go
// A veces nuestros programas de Go necesitan crear otros procesos no-Go
// procesos.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// Comenzaremos con un comando simple que no toma
	// argumentos o entrada y solo imprime algo en
	// stdout. El ayudante `exec.Command` crea un objeto
	// para representar este proceso externo.
	dateCmd := exec.Command("date")

	// El método `Output` ejecuta el comando, espera a que
	// termine y recopila su salida estándar.
	//  Si no hubo errores, `dateOut` contendrá bytes
	// con la información de la fecha.
	dateOut, err := dateCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` y otros métodos de `Command` devolverán
	// `*exec.Error` si hubo un problema al ejecutar el
	// comando (por ejemplo, ruta incorrecta), y `*exec.ExitError`
	// si el comando se ejecutó pero salió con un código de retorno no nulo.
	_, err = exec.Command("date", "-x").Output()
	if err!= nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("failed executing:", err)
		case *exec.ExitError:
			fmt.Println("command exit rc =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// A continuación veremos un caso un poco más complejo
	// donde enviamos datos al proceso externo a través de su
	// `stdin` y recopilamos los resultados de su `stdout`.
	grepCmd := exec.Command("grep", "hello")

	// Aquí explicitamente capturamos los tubos de entrada/salida, iniciamos
	// el proceso, escribimos alguna entrada en él, leemos la
	// salida resultante y finalmente esperamos a que el proceso
	// salga.
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// Omitimos las verificaciones de errores en el ejemplo anterior, pero
	// podrías usar el patrón habitual `if err!= nil` para todos ellos. También solo recopilamos los
	// resultados del `StdoutPipe`, pero podrías recopilar el `StderrPipe`
	// exactamente de la misma manera.
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// Tenga en cuenta que cuando se crean comandos, debemos
	// proporcionar una matriz de comandos y argumentos delineados explícitamente, en lugar de poder solo pasar
	// una cadena de línea de comandos. Si desea crear un comando completo
	// con una cadena, puede usar la opción `-c` de `bash`:
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}

```
