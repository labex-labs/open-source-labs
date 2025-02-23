# Cronómetros y Tickers

En esta práctica, debes crear un ticker que marque cada 500 ms hasta que lo detengamos. Utilizarás un canal para esperar los valores a medida que llegan.

- Utiliza el paquete `time` para crear un ticker.
- Utiliza un canal para esperar los valores a medida que llegan.
- Utiliza la declaración `select` para recibir valores del canal.
- Detén el ticker después de 1600 ms.

```sh
# Cuando ejecutamos este programa, el ticker debería marcar 3 veces
# antes de detenerlo.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

A continuación está el código completo:

```go
// [Cronómetros](timers) son para cuando quieres hacer
// algo una vez en el futuro - los _tickers_ son para cuando
// quieres hacer algo repetidamente a intervalos regulares.
// Aquí hay un ejemplo de un ticker que marca periódicamente
// hasta que lo detenemos.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Los tickers utilizan un mecanismo similar a los cronómetros:
	// un canal que se le envía valores. Aquí usaremos la
	// declaración `select` interna en el canal para esperar
	// los valores a medida que llegan cada 500 ms.
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// Los tickers se pueden detener como los cronómetros. Una vez
	// que se detiene un ticker, no recibirá más valores en su
	// canal. Lo detendremos después de 1600 ms.
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}

```
