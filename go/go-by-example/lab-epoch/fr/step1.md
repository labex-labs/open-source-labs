# Epoch

Le problème à résoudre dans ce laboratoire est d'écrire un programme Golang capable de calculer le nombre de secondes, de millisecondes ou de nanosecondes depuis l'époque Unix.

Pour terminer ce laboratoire, vous devez avoir une compréhension de base de Golang et répondre aux exigences suivantes :

- Être familier avec le package `time` en Golang.
- Savoir utiliser les fonctions `Unix`, `UnixMilli` et `UnixNano` du package `time`.

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# Ensuite, nous examinerons une autre tâche liée au temps :
# l'analyse et la mise en forme du temps.
```

Voici le code complet ci-dessous :

```go
// Une exigence commune dans les programmes est de
// obtenir le nombre de secondes, de millisecondes ou
// de nanosecondes depuis l'[époque Unix](https://en.wikipedia.org/wiki/Unix_time).
// Voici comment le faire en Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Utilisez `time.Now` avec `Unix`, `UnixMilli` ou `UnixNano`
	// pour obtenir le temps écoulé depuis l'époque Unix en
	// secondes, millisecondes ou nanosecondes respectivement.
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// Vous pouvez également convertir les secondes ou les
	// nanosecondes entières depuis l'époque en le
	// `time` correspondant.
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}

```
