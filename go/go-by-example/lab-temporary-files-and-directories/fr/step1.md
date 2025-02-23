# Fichiers et répertoires temporaires

Dans ce laboratoire, vous devez créer des fichiers et des répertoires temporaires en Go.

- Utilisez `os.CreateTemp` pour créer un fichier temporaire.
- Utilisez `os.MkdirTemp` pour créer un répertoire temporaire.
- Utilisez `os.RemoveAll` pour supprimer le répertoire temporaire.
- Utilisez `os.WriteFile` pour écrire des données dans un fichier.

```sh
$ go run temporary-files-and-directories.go
Nom du fichier temporaire : /tmp/sample610887201
Nom du répertoire temporaire : /tmp/sampledir898854668
```

Voici le code complet ci-dessous :

```go
// Au cours de l'exécution du programme, nous avons souvent besoin de créer
// des données qui ne sont plus nécessaires une fois le programme terminé.
// Les *fichiers et répertoires temporaires* sont utiles à cette fin car ils
// ne polluent pas le système de fichiers au fil du temps.

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

	// La manière la plus simple de créer un fichier temporaire est d'appeler
	// `os.CreateTemp`. Cela crée un fichier *et* l'ouvre pour la lecture et
	// l'écriture. Nous fournissons `""` comme premier argument, de sorte que
	// `os.CreateTemp` créera le fichier dans le emplacement par défaut de
	// notre système d'exploitation.
	f, err := os.CreateTemp("", "sample")
	check(err)

	// Affichez le nom du fichier temporaire. Sur les systèmes d'exploitation
	// basés sur Unix, le répertoire sera probablement `/tmp`. Le nom du fichier
	// commence par le préfixe donné en tant que deuxième argument à
	// `os.CreateTemp` et le reste est choisi automatiquement pour s'assurer
	// que les appels simultanés créeront toujours des noms de fichiers
	// différents.
	fmt.Println("Nom du fichier temporaire :", f.Name())

	// Nettoyez le fichier une fois que vous avez fini. Il est probable que
	// le système d'exploitation nettoie automatiquement les fichiers
	// temporaires après un certain temps, mais il est bon de le faire
	// explicitement.
	defer os.Remove(f.Name())

	// Nous pouvons écrire quelques données dans le fichier.
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// Si nous avons l'intention d'écrire de nombreux fichiers temporaires,
	// nous préférerions peut-être créer un *répertoire* temporaire. Les
	// arguments de `os.MkdirTemp` sont les mêmes que ceux de `CreateTemp`,
	// mais il renvoie un *nom de répertoire* plutôt qu'un fichier ouvert.
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Nom du répertoire temporaire :", dname)

	defer os.RemoveAll(dname)

	// Maintenant, nous pouvons synthétiser des noms de fichiers temporaires en
	// les préfixant avec notre répertoire temporaire.
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}

```
