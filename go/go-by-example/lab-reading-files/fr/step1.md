# Lecture de fichiers

Vous devez lire des fichiers dans votre programme Go et effectuer différentes opérations sur les données du fichier.

- Vous devriez être familier avec les concepts de base de la programmation Go.
- Vous devriez avoir Go installé sur votre ordinateur.

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Ensuite, nous examinerons l'écriture de fichiers.
```

Voici le code complet ci-dessous :

```go
// La lecture et l'écriture de fichiers sont des tâches de base nécessaires pour
// de nombreux programmes Go. Tout d'abord, nous examinerons quelques exemples de
// lecture de fichiers.

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// La lecture de fichiers nécessite de vérifier la plupart des appels pour des erreurs.
// Cette fonction d'aide simplifiera nos vérifications d'erreur ci-dessous.
func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Peut-être la tâche de lecture de fichier la plus basique est
	// de lire le contenu entier d'un fichier en mémoire.
	dat, err := os.ReadFile("/tmp/dat")
	check(err)
	fmt.Print(string(dat))

	// Vous voudrez souvent plus de contrôle sur la manière dont et les parties de
	// un fichier sont lues. Pour ces tâches, commencer par `Open` un fichier pour obtenir une valeur `os.File`.
	f, err := os.Open("/tmp/dat")
	check(err)

	// Lisez quelques octets au début du fichier.
	// Autorisez jusqu'à 5 à être lus mais notez également combien
	// ont effectivement été lus.
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// Vous pouvez également `Seek` à un emplacement connu dans le fichier
	// et `Read` à partir de là.
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n", string(b2[:n2]))

	// Le package `io` fournit quelques fonctions qui peuvent
	// être utiles pour la lecture de fichiers. Par exemple, des lectures
	// comme celles ci-dessus peuvent être plus robustement
	// implémentées avec `ReadAtLeast`.
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// Il n'y a pas de rembobinage intégré, mais `Seek(0, 0)`
	// y parvient.
	_, err = f.Seek(0, 0)
	check(err)

	// Le package `bufio` implémente un lecteur tamponné
	// qui peut être utile à la fois pour son efficacité
	// avec de nombreuses petites lectures et en raison des méthodes de lecture supplémentaires
	// qu'il fournit.
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))

	// Fermez le fichier lorsque vous avez fini (généralement, cela serait
	// planifié immédiatement après `Open` avec `defer`).
	f.Close()
}

```
