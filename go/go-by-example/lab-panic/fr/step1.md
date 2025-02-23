# Panic

Le laboratoire vous demande d'utiliser la fonction `panic` pour échouer rapidement en cas d'erreurs qui ne devraient pas se produire pendant le fonctionnement normal ou que vous n'êtes pas préparé à gérer de manière gracieuse.

- Connaissance de base du langage de programmation Golang.
- Familiarité avec la gestion des erreurs en Golang.
- Compréhension de la fonction `panic` en Golang.

```sh
# Exécuter ce programme provoquera une panique, imprimera
# un message d'erreur et des traces de goroutine, et sortira
# avec un statut non nul.

# Lorsque la première panique dans `main` se déclenche, le programme sort
# sans atteindre le reste du code. Si vous voulez voir le programme
# essayer de créer un fichier temporaire, commentez la première panique.
$ go run panic.go
panic: un problème

goroutine 1 [en cours d'exécution] :
main.main() /.../panic.go:12 +0x47
...
statut de sortie 2

# Notez que contrairement à certains langages qui utilisent des exceptions
# pour la gestion de nombreuses erreurs, en Go il est courant
# d'utiliser des valeurs de retour indiquant une erreur dès que possible.
```

Voici le code complet ci-dessous :

```go
// Une `panic` signifie généralement qu'il s'est produit quelque chose
// d'inattendu et de mal. Dans la plupart des cas, nous l'utilisons pour échouer rapidement
// en cas d'erreurs qui ne devraient pas se produire pendant le fonctionnement normal,
// ou que nous ne sommes pas préparé à gérer de manière gracieuse.

package main

import "os"

func main() {

	// Nous utiliserons `panic` tout au long de ce site pour vérifier les
	// erreurs inattendues. C'est le seul programme du site conçu pour provoquer une panique.
	panic("un problème")

	// Un usage courant de `panic` est d'annuler si une fonction
	// renvoie une valeur d'erreur que nous ne savons pas comment
	// (ou ne voulons pas) gérer. Voici un exemple de
	// `panic` si nous obtenons une erreur inattendue lors de la création d'un nouveau fichier.
	_, err := os.Create("/tmp/file")
	if err!= nil {
		panic(err)
	}
}

```
