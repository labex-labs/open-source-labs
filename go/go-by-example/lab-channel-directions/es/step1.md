# Direcciones de los canales

El problema que se debe resolver en este laboratorio es modificar el código dado para asegurarse de que los canales utilizados como parámetros de función se especifiquen para solo enviar o recibir valores.

- Conocimientos básicos de Golang
- Comprensión de los canales y su uso en Golang

```sh
$ go run channel-directions.go
mensaje pasado
```

A continuación está el código completo:

```go
// Cuando se utilizan canales como parámetros de función, se puede
// especificar si un canal está destinado a solo enviar o recibir
// valores. Esta especificidad aumenta la seguridad tipográfica
// del programa.

package main

import "fmt"

// Esta función `ping` solo acepta un canal para enviar
// valores. Sería un error de compilación intentar
// recibir en este canal.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// La función `pong` acepta un canal para recibir
// (`pings`) y otro para enviar (`pongs`).
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "mensaje pasado")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

```
