# Fonctions variadiques

Dans ce laboratoire, vous devez implémenter une fonction nommée `max` qui prend un nombre arbitraire d'entiers en arguments et renvoie la valeur maximale.

- La fonction `max` devrait prendre un nombre arbitraire d'entiers en arguments.
- La fonction `max` devrait renvoyer la valeur maximale des entiers passés en arguments.

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Un autre aspect clé des fonctions en Go est leur capacité
# à former des fermetures, que nous examinerons ensuite.
```

Voici le code complet ci-dessous :

```go
// [_Variadic functions_](https://en.wikipedia.org/wiki/Variadic_function)
// peuvent être appelées avec un nombre quelconque d'arguments de fin.
// Par exemple, `fmt.Println` est une fonction variadique commune.

package main

import "fmt"

// Voici une fonction qui prendra un nombre arbitraire
// d'`int` en arguments.
func sum(nums...int) {
	fmt.Print(nums, " ")
	total := 0
	// Dans la fonction, le type de `nums` est
	// équivalent à `[]int`. Nous pouvons appeler `len(nums)`,
	// l'itérer avec `range`, etc.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Les fonctions variadiques peuvent être appelées de la manière habituelle
	// avec des arguments individuels.
	sum(1, 2)
	sum(1, 2, 3)

	// Si vous avez déjà plusieurs arguments dans un slice,
	// appliquez-les à une fonction variadique en utilisant
	// `func(slice...)` comme ceci.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```
