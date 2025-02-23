# Répertoires

Créez un programme Go qui crée un nouveau sous-répertoire dans le répertoire de travail actuel, crée une hiérarchie de répertoires, y compris les parents, liste le contenu d'un répertoire, change le répertoire de travail actuel et visite un répertoire de manière récursive.

- Créez un nouveau sous-répertoire dans le répertoire de travail actuel.
- Lors de la création de répertoires temporaires, il est recommandé de `déférer` leur suppression. `os.RemoveAll` supprimera tout l'arbre de répertoires (de manière similaire à `rm -rf`).
- Créez une hiérarchie de répertoires, y compris les parents avec `MkdirAll`. Cela est similaire à la commande de ligne `mkdir -p`.
- `ReadDir` liste le contenu d'un répertoire, renvoyant une slice d'objets `os.DirEntry`.
- `Chdir` permet de changer le répertoire de travail actuel, de manière similaire à `cd`.
- Visitez un répertoire de manière récursive, y compris tous ses sous-répertoires. `Walk` accepte une fonction de rappel pour traiter chaque fichier ou répertoire visité.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

Voici le code complet ci-dessous :

```go
// Go a plusieurs fonctions utiles pour travailler avec
// *les répertoires* dans le système de fichiers.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Créez un nouveau sous-répertoire dans le répertoire de travail
	// actuel.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// Lors de la création de répertoires temporaires, il est recommandé
	// de `déférer` leur suppression. `os.RemoveAll`
	// supprimera tout l'arbre de répertoires (de manière similaire à
	// `rm -rf`).
	defer os.RemoveAll("subdir")

	// Fonction d'aide pour créer un nouveau fichier vide.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// Nous pouvons créer une hiérarchie de répertoires, y compris
	// les parents avec `MkdirAll`. Cela est similaire à la
	// commande de ligne `mkdir -p`.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` liste le contenu d'un répertoire, renvoyant une
	// slice d'objets `os.DirEntry`.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` permet de changer le répertoire de travail actuel,
	// de manière similaire à `cd`.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// Maintenant, nous verrons le contenu de `subdir/parent/child`
	// lorsque nous listerons le *répertoire actuel*.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` retour à l'endroit où nous sommes partis.
	err = os.Chdir("../../..")
	check(err)

	// Nous pouvons également visiter un répertoire *de manière
	// récursive*, y compris tous ses sous-répertoires. `Walk`
	// accepte une fonction de rappel pour traiter chaque fichier ou
	// répertoire visité.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` est appelée pour chaque fichier ou répertoire trouvé
// de manière récursive par `filepath.Walk`.
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```
