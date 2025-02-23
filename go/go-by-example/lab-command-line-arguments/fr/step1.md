# Arguments de ligne de commande

Le programme affiche actuellement les arguments de ligne de commande bruts passés à celui-ci. Cependant, il doit être modifié pour afficher des arguments spécifiques en fonction de leur index.

- Connaissance de base de Golang
- Familiarité avec les arguments de ligne de commande

```sh
# Pour tester les arguments de ligne de commande, il est
# préférable de construire un binaire avec `go build` d'abord.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Ensuite, nous examinerons le traitement plus avancé
# des arguments de ligne de commande avec des drapeaux.
```

Voici le code complet ci-dessous :

```go
// [_Arguments de ligne de commande_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// sont un moyen courant de paramétrer l'exécution de programmes.
// Par exemple, `go run hello.go` utilise les arguments `run` et
// `hello.go` pour le programme `go`.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` permet d'accéder aux arguments de ligne de commande bruts.
	// Notez que la première valeur de ce slice est le chemin vers le programme,
	// et `os.Args[1:]` contient les arguments du programme.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// Vous pouvez obtenir des arguments individuels avec une indexation normale.
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}

```
