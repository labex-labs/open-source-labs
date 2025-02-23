# Canaux

Dans ce laboratoire, vous devez créer un nouveau canal et y envoyer une valeur à partir d'une nouvelle goroutine. Vous devrez ensuite recevoir la valeur du canal et l'afficher.

- Vous devez utiliser la syntaxe `make(chan val-type)` pour créer un nouveau canal.
- Le canal doit être typé par les valeurs qu'il transporte.
- Vous devez utiliser la syntaxe `channel <-` pour envoyer une valeur dans le canal.
- Vous devez utiliser la syntaxe `<-channel` pour recevoir une valeur du canal.
- Vous devez utiliser une nouvelle goroutine pour envoyer la valeur dans le canal.

```sh
# Lorsque nous exécutons le programme, le message `"ping"` est
# correctement transmis d'une goroutine à l'autre via
# notre canal.
$ go run channels.go
ping

# Par défaut, les envois et les réceptions bloquent jusqu'à ce que
# l'expéditeur et le destinataire soient prêts. Cette propriété nous a
# permis d'attendre à la fin de notre programme le message `"ping"`
# sans avoir à utiliser d'autres méthodes de synchronisation.
```

Voici le code complet ci-dessous :

```go
// Les _Canaux_ sont les tuyaux qui relient des goroutines
// concourantes. Vous pouvez envoyer des valeurs dans des canaux à partir
// d'une goroutine et recevoir ces valeurs dans une autre goroutine.

package main

import "fmt"

func main() {

	// Créez un nouveau canal avec `make(chan val-type)`.
	// Les canaux sont typés par les valeurs qu'ils transportent.
	messages := make(chan string)

	// _Envoyez_ une valeur dans un canal à l'aide de la syntaxe `channel <-`.
	// Ici, nous envoyons `"ping"` au canal `messages` que nous avons créé
	// ci-dessus, à partir d'une nouvelle goroutine.
	go func() { messages <- "ping" }()

	// La syntaxe `<-channel` _reçoit_ une valeur du canal.
	// Ici, nous allons recevoir le message `"ping"` que nous avons envoyé
	// ci-dessus et l'afficher.
	msg := <-messages
	fmt.Println(msg)
}

```
