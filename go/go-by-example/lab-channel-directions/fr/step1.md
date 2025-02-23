# Directions des canaux

Le problème à résoudre dans ce laboratoire est de modifier le code donné pour s'assurer que les canaux utilisés comme paramètres de fonction sont spécifiés pour n'envoyer ou recevoir que des valeurs.

- Connaissance de base de Golang
- Compréhension des canaux et de leur utilisation en Golang

```sh
$ go run channel-directions.go
message transmis
```

Voici le code complet ci-dessous :

```go
// Lorsque l'on utilise des canaux comme paramètres de fonction, on peut
// spécifier si un canal est destiné à n'envoyer ou recevoir que des
// valeurs. Cette spécificité augmente la sécurité typée du
// programme.

package main

import "fmt"

// Cette fonction `ping` ne reçoit que un canal pour envoyer
// des valeurs. Il y aurait une erreur de compilation à essayer
// de recevoir sur ce canal.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// La fonction `pong` reçoit un canal pour recevoir
// (`pings`) et un deuxième pour envoyer (`pongs`).
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "message transmis")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

```
