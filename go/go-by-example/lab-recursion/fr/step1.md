# Récursion

La fonction `sum` prend un slice d'entiers et renvoie la somme de tous les entiers du slice. Cependant, la fonction est incomplète et doit être implémentée en utilisant la récursion.

- La fonction `sum` doit être implémentée en utilisant la récursion.
- La fonction doit prendre un slice d'entiers en entrée.
- La fonction doit renvoyer la somme de tous les entiers du slice.

```sh
$ go run recursion.go
5040
13
```

Voici le code complet ci-dessous :

```go
// Go prend en charge
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>les fonctions récursives</em></a>.
// Voici un exemple classique.

package main

import "fmt"

// Cette fonction `fact` s'appelle elle-même jusqu'à atteindre
// le cas de base de `fact(0)`.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// Les closures peuvent également être récursives, mais cela nécessite
	// que la closure soit déclarée avec un `var` typé explicitement
	// avant d'être définie.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// Comme `fib` a été précédemment déclarée dans `main`, Go
		// sait quelle fonction appeler avec `fib` ici.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```
