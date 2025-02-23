# Variables

Vous êtes requis de compléter le code pour déclarer et initialiser des variables de différents types en Golang.

- Connaissance de base de la syntaxe Golang
- Familiarité avec la déclaration et l'initialisation de variables en Golang

```sh
$ go run variables.go
initial
1 2
true
0
apple
```

Voici le code complet ci-dessous :

```go
// En Go, les _variables_ sont explicitement déclarées et utilisées par
// le compilateur pour par exemple vérifier la cohérence du type des
// appels de fonction.

package main

import "fmt"

func main() {

	// `var` déclare une ou plusieurs variables.
	var a = "initial"
	fmt.Println(a)

	// Vous pouvez déclarer plusieurs variables d'un coup.
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go déduira le type des variables initialisées.
	var d = true
	fmt.Println(d)

	// Les variables déclarées sans initialisation correspondante
	// sont initialisées avec leur _valeur par défaut_. Par exemple,
	// la valeur par défaut d'un `int` est `0`.
	var e int
	fmt.Println(e)

	// La syntaxe `:=` est un raccourci pour déclarer et
	// initialiser une variable, par exemple pour
	// `var f string = "apple"` dans ce cas.
	// Cette syntaxe n'est disponible que dans les fonctions.
	f := "apple"
	fmt.Println(f)
}

```
