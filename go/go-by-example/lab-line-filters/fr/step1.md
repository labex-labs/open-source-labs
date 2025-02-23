# Filtres de ligne

Le problème à résoudre dans ce laboratoire est d'écrire un programme Go qui lit le texte d'entrée à partir de stdin, met en majuscules toutes les lettres du texte puis imprime le texte modifié sur stdout.

- Le programme doit lire le texte d'entrée à partir de stdin.
- Le programme doit mettre en majuscules toutes les lettres du texte d'entrée.
- Le programme doit imprimer le texte modifié sur stdout.

```sh
# Pour tester notre filtre de ligne, commençons par créer
# un fichier avec quelques lignes en minuscules.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Ensuite, utilisez le filtre de ligne pour obtenir les
# lignes en majuscules.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

Voici le code complet ci-dessous :

```go
// Un _filtre de ligne_ est un type commun de programme qui lit
// l'entrée sur stdin, la traite puis imprime un résultat
// dérivé sur stdout. `grep` et `sed` sont des filtres de
// ligne courants.

// Voici un exemple de filtre de ligne en Go qui écrit une
// version en majuscules de tout le texte d'entrée. Vous
// pouvez utiliser ce modèle pour écrire vos propres filtres
// de ligne en Go.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// Enveloppant `os.Stdin` non bufferisé avec un
	// scanner bufferisé nous donne une méthode `Scan` pratique
	// qui avance le scanner au prochain jeton ; qui est la
	// prochaine ligne dans le scanner par défaut.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` renvoie le jeton actuel, ici la prochaine ligne,
		// de l'entrée.
		ucl := strings.ToUpper(scanner.Text())

		// Écrivez la ligne en majuscules.
		fmt.Println(ucl)
	}

	// Vérifiez s'il y a des erreurs pendant `Scan`. La fin
	// de fichier est attendue et n'est pas signalée par `Scan`
	// comme une erreur.
	if err := scanner.Err(); err!= nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
