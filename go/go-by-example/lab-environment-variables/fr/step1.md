# Variables d'environnement

Dans ce laboratoire, vous devrez définir, obtenir et lister les variables d'environnement.

- Utilisez `os.Setenv` pour définir une paire clé/valeur.
- Utilisez `os.Getenv` pour obtenir une valeur pour une clé.
- Utilisez `os.Environ` pour lister toutes les paires clé/valeur de l'environnement.
- Utilisez `strings.SplitN` pour séparer la clé et la valeur.

```sh
# En exécutant le programme, on voit que l'on récupère la valeur
# de `FOO` que l'on a définie dans le programme, mais que
# `BAR` est vide.
$ go run environment-variables.go
FOO: 1
BAR:

# La liste des clés de l'environnement dépendra de votre
# machine spécifique.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Si on définit `BAR` dans l'environnement d'abord, le programme
# exécuté récupère cette valeur.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

Voici le code complet ci-dessous :

```go
// [Variables d'environnement](https://en.wikipedia.org/wiki/Environment_variable)
// sont un mécanisme universel pour [transmettre des informations
// de configuration aux programmes Unix](https://www.12factor.net/config).
// Voyons comment définir, obtenir et lister les variables d'environnement.

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// Pour définir une paire clé/valeur, utilisez `os.Setenv`. Pour obtenir
	// une valeur pour une clé, utilisez `os.Getenv`. Cela renverra
	// une chaîne de caractères vide si la clé n'est pas présente
	// dans l'environnement.
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// Utilisez `os.Environ` pour lister toutes les paires clé/valeur
	// de l'environnement. Cela renvoie un slice de chaînes de caractères
	// au format `KEY=value`. Vous pouvez les `strings.SplitN` pour
	// obtenir la clé et la valeur. Ici, on imprime toutes les clés.
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}

```
