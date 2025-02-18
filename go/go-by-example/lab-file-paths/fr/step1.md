# Chemins de fichiers

Dans ce laboratoire (lab), vous devez utiliser le package `filepath` pour effectuer diverses opérations sur les chemins de fichiers, telles que la construction de chemins de manière portable, la division d'un chemin en composants répertoire et fichier, la vérification si un chemin est absolu, la recherche de l'extension d'un fichier et la recherche d'un chemin relatif entre deux chemins.

- Utilisez `Join` pour construire des chemins de manière portable.
- Utilisez `Dir` et `Base` pour diviser un chemin en composants répertoire et fichier.
- Utilisez `IsAbs` pour vérifier si un chemin est absolu.
- Utilisez `Ext` pour trouver l'extension d'un fichier.
- Utilisez `TrimSuffix` pour supprimer l'extension d'un nom de fichier.
- Utilisez `Rel` pour trouver un chemin relatif entre deux chemins.

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

Voici le code complet ci-dessous :

```go
// Le package `filepath` fournit des fonctions pour analyser
// et construire des *chemins de fichiers* de manière portable
// entre les systèmes d'exploitation ; par exemple, `dir/file` sur Linux
// et `dir\file` sur Windows.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` devrait être utilisé pour construire des chemins
	// de manière portable. Il prend un nombre arbitraire d'arguments
	// et construit un chemin hiérarchique à partir d'eux.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// Vous devriez toujours utiliser `Join` au lieu de concaténer
	// manuellement des `/` ou des `\`. En plus de garantir la portabilité,
	// `Join` normalisera également les chemins en supprimant les séparateurs
	// superflus et les changements de répertoire.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` et `Base` peuvent être utilisés pour diviser un chemin
	// en répertoire et fichier. Alternativement, `Split` retournera
	// les deux dans un seul appel.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// Nous pouvons vérifier si un chemin est absolu.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// Certains noms de fichiers ont des extensions après un point.
	// Nous pouvons extraire l'extension de tels noms avec `Ext`.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// Pour trouver le nom du fichier sans l'extension,
	// utilisez `strings.TrimSuffix`.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` trouve un chemin relatif entre une *base* et une
	// *cible*. Il retourne une erreur si la cible ne peut pas
	// être rendue relative à la base.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)
}

```
