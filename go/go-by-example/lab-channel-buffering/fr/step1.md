# Channel Buffering

Par défaut, les canaux en Golang sont non tamponnés, ce qui signifie qu'ils n'acceptent des envois (`chan <-`) que s'il existe une réception correspondante (`<- chan`) prête à recevoir la valeur envoyée. Cependant, les canaux tamponnés acceptent un nombre limité de valeurs sans récepteur correspondant pour ces valeurs. Dans ce laboratoire, vous êtes requis de créer un canal tamponné et d'envoyer des valeurs dans le canal sans réception concurrente correspondante.

- Connaissance de base des canaux en Golang
- Compréhension des canaux tamponnés

```sh
$ go run channel-buffering.go
buffered
channel
```

Voici le code complet ci-dessous :

```go
// Par défaut, les canaux sont _non tamponnés_, ce qui signifie qu'ils
// accepteront seulement des envois (`chan <-`) s'il existe une
// réception correspondante (`<- chan`) prête à recevoir la
// valeur envoyée. Les _canaux tamponnés_ acceptent un nombre limité
// de valeurs sans récepteur correspondant pour ces valeurs.

package main

import "fmt"

func main() {

	// Ici, nous `créons` un canal de chaînes de caractères avec un
	// tampon de 2 valeurs.
	messages := make(chan string, 2)

	// Étant donné que ce canal est tamponné, nous pouvons envoyer
	// ces valeurs dans le canal sans réception concurrente
	// correspondante.
	messages <- "buffered"
	messages <- "channel"

	// Plus tard, nous pouvons recevoir ces deux valeurs comme d'habitude.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

```
