# Canales

En este laboratorio, se le pide que cree un nuevo canal y envíe un valor a través de él desde una nueva gorutina. Luego recibirá el valor del canal y lo imprimirá.

- Debe utilizar la sintaxis `make(chan val-type)` para crear un nuevo canal.
- El canal debe ser tipado por los valores que transporta.
- Debe utilizar la sintaxis `channel <-` para enviar un valor al canal.
- Debe utilizar la sintaxis `<-channel` para recibir un valor del canal.
- Debe utilizar una nueva gorutina para enviar el valor al canal.

```sh
# Cuando ejecutamos el programa, el mensaje `"ping"` se
# pasa con éxito de una gorutina a otra a través de
# nuestro canal.
$ go run channels.go
ping

# Por defecto, los envíos y recepciones se bloquean hasta
# que tanto el emisor como el receptor estén listos. Esta
# propiedad nos permite esperar al final de nuestro
# programa el mensaje `"ping"` sin tener que utilizar ninguna
# otra sincronización.
```

A continuación está el código completo:

```go
// Los _Canales_ son las tuberías que conectan gorutinas
// concurrentes. Puede enviar valores a través de canales
// desde una gorutina y recibir esos valores en otra
// gorutina.

package main

import "fmt"

func main() {

	// Crea un nuevo canal con `make(chan val-type)`.
	// Los canales son tipados por los valores que transportan.
	messages := make(chan string)

	// _Envía_ un valor a un canal utilizando la sintaxis
	// `channel <-`. Aquí enviamos `"ping"` al canal
	// `messages` que creamos anteriormente, desde una nueva
	// gorutina.
	go func() { messages <- "ping" }()

	// La sintaxis `<-channel` _recibe_ un valor del canal.
	// Aquí recibiremos el mensaje `"ping"` que enviamos
	// anteriormente y lo imprimiremos.
	msg := <-messages
	fmt.Println(msg)
}

```
