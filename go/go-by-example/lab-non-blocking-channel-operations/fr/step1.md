# Opérations non bloquantes sur les canaux

Le problème à résoudre dans ce laboratoire est d'implémenter des opérations non bloquantes sur les canaux en utilisant l'instruction `select` avec une clause `default`.

- Implémentez une réception non bloquante sur un canal en utilisant l'instruction `select` avec une clause `default`.
- Implémentez un envoi non bloquante sur un canal en utilisant l'instruction `select` avec une clause `default`.
- Implémentez une sélection multi-voie non bloquante en utilisant l'instruction `select` avec plusieurs clauses `case` et une clause `default`.

```sh
$ go run non-blocking-channel-operations.go
aucun message reçu
aucun message envoyé
aucune activité
```

Voici le code complet ci-dessous :

```go
// Les envois et les réceptions de base sur les canaux sont bloquants.
// Cependant, nous pouvons utiliser `select` avec une clause `default` pour
// implémenter des envois, des réceptions _non bloquants_ et même
// des sélections multi-voies `select` non bloquantes.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// Voici une réception non bloquante. Si une valeur est
	// disponible sur `messages`, alors `select` prendra
	// la clause `<-messages` avec cette valeur. Sinon
	// il prendra immédiatement la clause `default`.
	select {
	case msg := <-messages:
		fmt.Println("reçu message", msg)
	default:
		fmt.Println("aucun message reçu")
	}

	// Un envoi non bloquant fonctionne de manière similaire. Ici `msg`
	// ne peut pas être envoyé au canal `messages`, car
	// le canal n'a pas de tampon et il n'y a pas de récepteur.
	// Par conséquent, la clause `default` est sélectionnée.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("envoyé message", msg)
	default:
		fmt.Println("aucun message envoyé")
	}

	// Nous pouvons utiliser plusieurs clauses `case` au-dessus de la
	// clause `default` pour implémenter une sélection multi-voie non bloquante.
	// Ici, nous tentons des réceptions non bloquantes
	// sur `messages` et `signals`.
	select {
	case msg := <-messages:
		fmt.Println("reçu message", msg)
	case sig := <-signals:
		fmt.Println("reçu signal", sig)
	default:
		fmt.Println("aucune activité")
	}
}

```
