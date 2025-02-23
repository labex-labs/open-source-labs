# Goroutines

Le problème à résoudre dans ce laboratoire est de créer et d'exécuter des goroutines pour exécuter des fonctions de manière concurrente.

- La fonction `f` devrait afficher sa chaîne d'entrée et une variable compteur trois fois.
- La fonction `main` devrait appeler la fonction `f` de manière synchrone et afficher "direct" et une variable compteur trois fois.
- La fonction `main` devrait appeler la fonction `f` de manière asynchrone en utilisant une goroutine et afficher "goroutine" et une variable compteur trois fois.
- La fonction `main` devrait démarrer une goroutine pour exécuter une fonction anonyme qui affiche un message.
- La fonction `main` devrait attendre que les goroutines aient fini d'exécuter avant d'afficher "fait".

```sh
# Lorsque nous exécutons ce programme, nous voyons d'abord la sortie
# de l'appel bloquant, puis la sortie des deux
# goroutines. La sortie des goroutines peut être intercalée,
# car les goroutines sont exécutées de manière concurrente par
# le runtime Go.
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
fait

# Ensuite, nous examinerons un complément aux goroutines dans
# les programmes Go concurrentiels : les canaux.
```

Voici le code complet ci-dessous :

```go
// Une _goroutine_ est un fil léger d'exécution.

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Supposons qu'on ait un appel de fonction `f(s)`. Voici comment
	// on l'appellerait de la manière habituelle, en l'exécutant
	// de manière synchrone.
	f("direct")

	// Pour invoquer cette fonction dans une goroutine, utilisez
	// `go f(s)`. Cette nouvelle goroutine exécutera
	// de manière concurrente avec celle qui appelle.
	go f("goroutine")

	// Vous pouvez également démarrer une goroutine pour un appel
	// de fonction anonyme.
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Nos deux appels de fonction sont maintenant exécutés de manière
	// asynchrone dans des goroutines distinctes. Attendez qu'ils
	// aient fini (pour une approche plus robuste, utilisez un [WaitGroup](waitgroups)).
	time.Sleep(time.Second)
	fmt.Println("fait")
}

```
