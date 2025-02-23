# Écrire dans des fichiers

Vous devez écrire un programme Go qui écrit une chaîne de caractères et des octets dans un fichier et utilise des écrivains tamponnés.

- Le programme devrait écrire une chaîne de caractères et des octets dans un fichier.
- Le programme devrait utiliser des écrivains tamponnés.

```sh
# Essayez d'exécuter le code d'écriture dans un fichier.
$ go run writing-files.go
a écrit 5 octets
a écrit 7 octets
a écrit 9 octets

# Vérifiez ensuite le contenu des fichiers écrits.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# Ensuite, nous allons voir comment appliquer certaines des idées
# d'entrée/sortie de fichiers que nous venons de voir aux flux
# `stdin` et `stdout`.
```

Voici le code complet ci-dessous :

```go
// Écrire dans des fichiers en Go suit des modèles similaires à ceux
// que nous avons vus précédemment pour la lecture.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Pour commencer, voici comment écrire une chaîne de caractères (ou simplement
	// des octets) dans un fichier.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// Pour des écritures plus granuleuses, ouvrez un fichier en écriture.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// Il est courant de déferrer une `Close` immédiatement
	// après avoir ouvert un fichier.
	defer f.Close()

	// Vous pouvez `Write` des tranches d'octets comme vous le souhaitez.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("a écrit %d octets\n", n2)

	// Une `WriteString` est également disponible.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("a écrit %d octets\n", n3)

	// Émettez un `Sync` pour vider les écritures dans le stockage stable.
	f.Sync()

	// `bufio` fournit des écrivains tamponnés en plus
	// des lecteurs tamponnés que nous avons vus précédemment.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("a écrit %d octets\n", n4)

	// Utilisez `Flush` pour vous assurer que toutes les opérations tamponnées ont
	// été appliquées à l'écrivain sous-jacent.
	w.Flush()

}

```
