# Nombres aléatoires

Vous êtes requis d'écrire un programme qui génère des entiers et des flottants aléatoires dans une plage spécifiée. Le programme devrait également être capable de produire des séquences de nombres variables en changeant la graine.

- Le programme devrait utiliser le package `math/rand` pour générer des nombres aléatoires.
- Le programme devrait générer des entiers aléatoires dans une plage spécifiée.
- Le programme devrait générer des flottants aléatoires dans une plage spécifiée.
- Le programme devrait être capable de produire des séquences de nombres variables en changeant la graine.

```sh
# Selon où vous exécutez cet exemple, certains des
# nombres générés peuvent être différents. Notez que sur
# le terrain de jeu Go, le positionnement avec `time.Now()`
# produit toujours des résultats déterministes en raison
# de la manière dont le terrain de jeu est implémenté.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Consultez la documentation du package [`math/rand`](https://pkg.go.dev/math/rand)
# pour des références sur d'autres quantités aléatoires
# que Go peut fournir.
```

Voici le code complet ci-dessous :

```go
// Le package `math/rand` de Go fournit
// la génération de [nombres pseudo-aléatoires](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// Par exemple, `rand.Intn` renvoie un `int` aléatoire n,
	// `0 <= n < 100`.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` renvoie un `float64` `f`,
	// `0.0 <= f < 1.0`.
	fmt.Println(rand.Float64())

	// Cela peut être utilisé pour générer des flottants aléatoires dans
	// d'autres plages, par exemple `5.0 <= f' < 10.0`.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// Le générateur de nombres par défaut est déterministe, donc il produira
	// la même séquence de nombres à chaque fois par défaut.
	// Pour produire des séquences variables, donnez-lui une graine qui change.
	// Notez que cela n'est pas sécuritaire à utiliser pour des nombres aléatoires
	// que vous souhaitez être secrets ; utilisez `crypto/rand` pour ceux-ci.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// Appelez le `rand.Rand` résultant tout comme les
	// fonctions du package `rand`.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// Si vous positionnez une source avec le même nombre, elle
	// produit la même séquence de nombres aléatoires.
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```
