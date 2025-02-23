# Defer

Dans ce laboratoire, vous devez utiliser `defer` pour créer un fichier, y écrire et le fermer une fois que vous avez fini.

- La fonction `createFile` devrait créer un fichier avec le chemin donné et retourner un pointeur vers le fichier.
- La fonction `writeFile` devrait écrire la chaîne de caractères "data" dans le fichier.
- La fonction `closeFile` devrait fermer le fichier et vérifier s'il y a des erreurs.

```sh
# Exécution du programme confirme que le fichier est fermé
# après avoir été écrit.
$ go run defer.go
creating
writing
closing
```

Voici le code complet ci-dessous :

```go
// _Defer_ est utilisé pour s'assurer qu'un appel de fonction est
// effectué plus tard dans l'exécution d'un programme, généralement pour
// des fins de nettoyage. `defer` est souvent utilisé là où par exemple
// `ensure` et `finally` seraient utilisés dans d'autres langages.

package main

import (
	"fmt"
	"os"
)

// Supposons que nous voulions créer un fichier, y écrire,
// puis le fermer une fois que nous avons fini. Voici comment nous pourrions
// le faire avec `defer`.
func main() {

	// Immédiatement après avoir obtenu un objet de fichier avec
	// `createFile`, nous différons la fermeture de ce fichier
	// avec `closeFile`. Cela sera exécuté à la fin
	// de la fonction englobante (`main`), après
	// que `writeFile` ait fini.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err!= nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	// Il est important de vérifier s'il y a des erreurs lors de la fermeture d'un
	// fichier, même dans une fonction différée.
	if err!= nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

```
