# Bufferización de canales

Por defecto, los canales en Golang son no bufferizados, lo que significa que solo aceptan envíos (`chan <-`) si hay una recepción correspondiente (`<- chan`) lista para recibir el valor enviado. Sin embargo, los canales bufferizados aceptan un número limitado de valores sin un receptor correspondiente para esos valores. En este laboratorio, se te pide crear un canal bufferizado y enviar valores al canal sin una recepción concurrente correspondiente.

- Conocimientos básicos de los canales de Golang
- Comprensión de los canales bufferizados

```sh
$ go run channel-buffering.go
buffered
channel
```

A continuación está el código completo:

```go
// Por defecto, los canales son _no bufferizados_, lo que significa que
// solo aceptarán envíos (`chan <-`) si hay una
// recepción correspondiente (`<- chan`) lista para recibir el
// valor enviado. Los _canales bufferizados_ aceptan un número limitado
// de valores sin un receptor correspondiente para esos valores.

package main

import "fmt"

func main() {

	// Aquí `hacemos` un canal de cadenas con un buffer de hasta
	// 2 valores.
	mensajes := make(chan string, 2)

	// Debido a que este canal está bufferizado, podemos enviar estos
	// valores al canal sin una recepción concurrente correspondiente.
	mensajes <- "buffered"
	mensajes <- "channel"

	// Más tarde podemos recibir estos dos valores como de costumbre.
	fmt.Println(<-mensajes)
	fmt.Println(<-mensajes)
}

```
