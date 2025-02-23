# Sortie

Le problème à résoudre dans ce labo est de quitter un programme Go avec un code de statut spécifique en utilisant la fonction `os.Exit`.

Pour terminer ce labo, vous devriez avoir une compréhension de base de la programmation Go et du package `os`.

```sh
# Si vous exécutez `exit.go` avec `go run`, la sortie
# sera capturée par `go` et affichée.
$ go run exit.go
statut de sortie 3

# En construisant et en exécutant un binaire, vous pouvez voir
# le statut dans le terminal.
$ go build exit.go
$./exit
$ echo $?
3

# Notez que le `!` de notre programme n'a jamais été imprimé.
```

Voici le code complet ci-dessous :

```go
// Utilise `os.Exit` pour quitter immédiatement avec un statut donné.

package main

import (
	"fmt"
	"os"
)

func main() {

	// Les `defer` ne seront _pas_ exécutés lorsqu'on utilise `os.Exit`, donc
	// cet `fmt.Println` ne sera jamais appelé.
	defer fmt.Println("!")

	// Sortie avec le statut 3.
	os.Exit(3)
}

// Notez que contrairement par exemple à C, Go n'utilise pas une valeur de retour
// entière de `main` pour indiquer le statut de sortie. Si vous voulez quitter
// avec un statut non nul, vous devriez utiliser `os.Exit`.

```
