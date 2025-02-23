# Operaciones no bloqueantes de canales

El problema que se debe resolver en este laboratorio es implementar operaciones no bloqueantes de canales utilizando la instrucción `select` con una cláusula `default`.

- Implementar una recepción no bloqueante en un canal utilizando la instrucción `select` con una cláusula `default`.
- Implementar un envío no bloqueante en un canal utilizando la instrucción `select` con una cláusula `default`.
- Implementar una selección no bloqueante multi-vía utilizando la instrucción `select` con múltiples cláusulas `case` y una cláusula `default`.

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```

A continuación está el código completo:

```go
// Las envíos y recepciones básicas en canales son bloqueantes.
// Sin embargo, podemos utilizar `select` con una cláusula `default` para
// implementar envíos, recepciones _no bloqueantes_ e incluso
// selecciones multi-vía no bloqueantes.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// Aquí hay una recepción no bloqueante. Si un valor está
	// disponible en `messages` entonces `select` tomará
	// el caso `<-messages` con ese valor. Si no, inmediatamente
	// tomará el caso `default`.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// Un envío no bloqueante funciona de manera similar. Aquí `msg`
	// no puede ser enviado al canal `messages`, porque
	// el canal no tiene búfer y no hay receptor.
	// Por lo tanto, se selecciona el caso `default`.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// Podemos utilizar múltiples casos arriba de la cláusula `default`
	// para implementar una selección no bloqueante multi-vía.
	// Aquí intentamos recepciones no bloqueantes
	// tanto en `messages` como en `signals`.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}

```
