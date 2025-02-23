# Limitation de débit

Le problème est de limiter la gestion des requêtes entrantes pour maintenir la qualité de service et contrôler l'utilisation des ressources.

- Langage de programmation Go
- Compréhension de base des goroutines, des canaux et des décompteurs

```sh
# Lorsque nous exécutons notre programme, nous voyons que la première
# série de requêtes est traitée une fois toutes les ~200 millisecondes,
# comme prévu.
$ go run rate-limiting.go
requête 1 2012-10-19 00:38:18.687438 +0000 UTC
requête 2 2012-10-19 00:38:18.887471 +0000 UTC
requête 3 2012-10-19 00:38:19.087238 +0000 UTC
requête 4 2012-10-19 00:38:19.287338 +0000 UTC
requête 5 2012-10-19 00:38:19.487331 +0000 UTC

# Pour la deuxième série de requêtes, nous traitons les 3 premières
# immédiatement en raison de la limitation de débit pouvant supporter
# des pics, puis nous traitons les 2 restantes avec un retard d'environ
# 200 ms chacun.
requête 1 2012-10-19 00:38:20.487578 +0000 UTC
requête 2 2012-10-19 00:38:20.487645 +0000 UTC
requête 3 2012-10-19 00:38:20.487676 +0000 UTC
requête 4 2012-10-19 00:38:20.687483 +0000 UTC
requête 5 2012-10-19 00:38:20.887542 +0000 UTC
```

Voici le code complet ci-dessous :

```go
// [_Limitation de débit_](https://en.wikipedia.org/wiki/Rate_limiting)
// est un mécanisme important pour contrôler l'utilisation des ressources
// et maintenir la qualité de service. Go prend en charge
// élégamment la limitation de débit avec des goroutines,
// des canaux et des [décompteurs](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Tout d'abord, nous allons examiner la limitation de débit de base.
	// Supposons que nous voulions limiter la gestion de nos requêtes
	// entrantes. Nous allons traiter ces requêtes à partir d'un canal
	// du même nom.
	requêtes := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requêtes <- i
	}
	close(requêtes)

	// Ce canal `limiteur` recevra une valeur toutes les 200 millisecondes.
	// C'est le régulateur de notre schéma de limitation de débit.
	limiteur := time.Tick(200 * time.Millisecond)

	// En bloquant la réception d'un message du canal `limiteur`
	// avant de traiter chaque requête, nous nous limitons à 1 requête
	// toutes les 200 millisecondes.
	for req := range requêtes {
		<-limiteur
		fmt.Println("requête", req, time.Now())
	}

	// Nous pouvons vouloir autoriser de courts pics de requêtes dans
	// notre schéma de limitation de débit tout en conservant la limite
	// de débit globale. Nous pouvons le faire en mettant en mémoire
	// tampon notre canal limiteur. Ce canal `limiteur à pics` permettra
	// des pics de jusqu'à 3 événements.
	limiteurAPics := make(chan time.Time, 3)

	// Remplissons le canal pour représenter le pic autorisé.
	for i := 0; i < 3; i++ {
		limiteurAPics <- time.Now()
	}

	// Toutes les 200 millisecondes, nous allons essayer d'ajouter une
	// nouvelle valeur à `limiteurAPics`, jusqu'à sa limite de 3.
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			limiteurAPics <- t
		}
	}()

	// Maintenant, simulons 5 nouvelles requêtes entrantes. Les 3 premières
	// bénéficieront de la capacité de pic de `limiteurAPics`.
	requêtesAPics := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requêtesAPics <- i
	}
	close(requêtesAPics)
	for req := range requêtesAPics {
		<-limiteurAPics
		fmt.Println("requête", req, time.Now())
	}
}

```
