# Select

En este laboratorio, se le dan dos canales, `c1` y `c2`, que recibirán un valor después de cierto tiempo. Su tarea es usar `select` para esperar simultáneamente ambos valores, imprimiendo cada uno a medida que llega.

- Debe usar la instrucción `select` para esperar en ambos canales.
- Debe imprimir el valor recibido de cada canal a medida que llega.

```sh
# Recibimos los valores `"uno"` y luego `"dos"` como
# se esperaba.
$ time go run select.go
recibido uno
recibido dos

# Tenga en cuenta que el tiempo total de ejecución es solo ~2 segundos
# ya que las dos `Sleeps` de 1 y 2 segundos se ejecutan
# concurrentemente.
real 0m2.245s
```

A continuación está el código completo:

```go
// La _select_ de Go le permite esperar en múltiples operaciones de canal.
// Combinar gorutinas y canales con
// select es una característica poderosa de Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Para nuestro ejemplo, seleccionaremos entre dos canales.
	c1 := make(chan string)
	c2 := make(chan string)

	// Cada canal recibirá un valor después de cierto tiempo, para simular, por ejemplo,
	// operaciones RPC bloqueantes que se ejecutan en gorutinas concurrentes.
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "uno"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "dos"
	}()

	// Usaremos `select` para esperar simultáneamente ambos valores
	// e imprimir cada uno a medida que llega.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("recibido", msg1)
		case msg2 := <-c2:
			fmt.Println("recibido", msg2)
		}
	}
}

```
