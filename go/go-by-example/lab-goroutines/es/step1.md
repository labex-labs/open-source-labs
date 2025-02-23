# Gorutinas

El problema que se debe resolver en esta práctica es crear y ejecutar gorutinas para ejecutar funciones de manera concurrente.

- La función `f` debe imprimir su cadena de entrada y una variable contador tres veces.
- La función `main` debe llamar a la función `f` de manera síncrona e imprimir "directo" y una variable contador tres veces.
- La función `main` debe llamar a la función `f` de manera asíncrona utilizando una gorutina e imprimir "gorutina" y una variable contador tres veces.
- La función `main` debe iniciar una gorutina para ejecutar una función anónima que imprima un mensaje.
- La función `main` debe esperar a que las gorutinas terminen de ejecutarse antes de imprimir "hecho".

```sh
# Cuando ejecutamos este programa, primero vemos la salida
# de la llamada bloqueante, luego la salida de las dos
# gorutinas. La salida de las gorutinas puede estar
# intercalada, porque las gorutinas se están ejecutando
# concurrentemente por la ejecución en tiempo real de Go.
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
hecho

# A continuación, veremos un complemento a las gorutinas en
# los programas concurrentes de Go: los canales.
```

A continuación está el código completo:

```go
// Una _gorutina_ es un hilo liviano de ejecución.

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Supongamos que tenemos una llamada a una función `f(s)`. Aquí está cómo
	// llamaríamos a eso de la manera habitual, ejecutándola
	// de manera síncrona.
	f("directo")

	// Para invocar esta función en una gorutina, use
	// `go f(s)`. Esta nueva gorutina se ejecutará
	// concurrentemente con la que la llama.
	go f("gorutina")

	// También puede iniciar una gorutina para una llamada a una
	// función anónima.
	go func(msg string) {
		fmt.Println(msg)
	}("yendo")

	// Nuestras dos llamadas a funciones ahora se están ejecutando de manera asíncrona en
	// gorutinas separadas. Espere a que terminen
	// (para un enfoque más robusto, use un [WaitGroup](waitgroups)).
	time.Sleep(time.Second)
	fmt.Println("hecho")
}

```
