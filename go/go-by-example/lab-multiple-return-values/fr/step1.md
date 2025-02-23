# Retours multiples

Complétez la fonction `swap` pour renvoyer deux paramètres d'entrée dans l'ordre inverse.

- La fonction `swap` devrait prendre deux entiers comme paramètres d'entrée.
- La fonction `swap` devrait renvoyer deux entiers dans l'ordre inverse.

```sh
$ go run multiple-return-values.go
3
7
7

# Accepter un nombre variable d'arguments est une autre bonne
# fonctionnalité des fonctions Go ; nous y reviendrons ensuite.
```

Voici le code complet ci-dessous :

```go
// Go prend en charge nativement les _retours multiples_.
// Cette fonctionnalité est souvent utilisée dans le Go idéal, par exemple
// pour renvoyer à la fois un résultat et une valeur d'erreur à partir d'une fonction.

package main

import "fmt"

// Le `(int, int)` dans cette signature de fonction indique que
// la fonction renvoie 2 `int`.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Ici, nous utilisons les 2 différentes valeurs de retour du
	// appel avec une _affectation multiple_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Si vous ne voulez que sous-ensemble des valeurs renvoyées,
	// utilisez l'identificateur vide `_`.
	_, c := vals()
	fmt.Println(c)
}

```
