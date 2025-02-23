# Types de valeurs

Votre tâche consiste à compléter la fonction `calculate` qui prend deux entiers en entrée et renvoie leur somme et leur produit.

- La fonction `calculate` devrait prendre deux entiers en paramètres.
- La fonction `calculate` devrait renvoyer deux entiers, la somme et le produit des paramètres d'entrée.

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

Voici le code complet ci-dessous :

```go
// Go a différents types de valeurs, y compris les chaînes de caractères,
// les entiers, les flottants, les booléens, etc. Voici quelques
// exemples de base.

package main

import "fmt"

func main() {

	// Les chaînes de caractères, qui peuvent être additionnées avec `+`.
	fmt.Println("go" + "lang")

	// Les entiers et les flottants.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// Les booléens, avec les opérateurs booléens tels que prévu.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
