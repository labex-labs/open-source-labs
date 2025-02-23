# if-else

Vous êtes requis de compléter la fonction `checkNumber` qui prend un entier en entrée et renvoie une chaîne de caractères. Si le nombre est pair, renvoyez "pair", sinon renvoyez "impair".

- La fonction doit s'appeler `checkNumber`.
- La fonction doit prendre un entier en entrée.
- La fonction doit renvoyer une chaîne de caractères.
- Si le nombre est pair, renvoyez "pair".
- Si le nombre est impair, renvoyez "impair".

```sh
$ go run if-else.go
7 est impair
8 est divisible par 4
9 a 1 chiffre

# Il n'y a pas de [condition ternaire](https://en.wikipedia.org/wiki/%3F:)
# en Go, donc vous devrez utiliser une instruction `if` complète même
# pour les conditions de base.
```

Voici le code complet ci-dessous :

```go
// La branchement avec `if` et `else` en Go est
// simple.

package main

import "fmt"

func main() {

	// Voici un exemple de base.
	if 7%2 == 0 {
		fmt.Println("7 est pair")
	} else {
		fmt.Println("7 est impair")
	}

	// Vous pouvez avoir une instruction `if` sans `else`.
	if 8%4 == 0 {
		fmt.Println("8 est divisible par 4")
	}

	// Une instruction peut précéder les conditionnels ; toutes les variables
	// déclarées dans cette instruction sont disponibles dans la branche actuelle
	// et dans toutes les branches suivantes.
	if num := 9; num < 0 {
		fmt.Println(num, "est négatif")
	} else if num < 10 {
		fmt.Println(num, "a 1 chiffre")
	} else {
		fmt.Println(num, "a plusieurs chiffres")
	}
}

// Notez que vous n'avez pas besoin de parenthèses autour des conditions
// en Go, mais que les accolades sont obligatoires.

```
