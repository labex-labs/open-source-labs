# Directive d'insertion

Votre tâche consiste à modifier le code donné pour insérer des fichiers et des dossiers dans le binaire Go et à afficher leur contenu.

- Vous devez utiliser le package `embed` pour insérer des fichiers et des dossiers.
- Vous devez utiliser les types `string` et `[]byte` pour stocker le contenu des fichiers insérés.
- Vous devez utiliser le type `embed.FS` pour insérer plusieurs fichiers ou dossiers avec des caractères génériques.
- Vous devez afficher le contenu des fichiers insérés.

```sh
# Utilisez ces commandes pour exécuter l'exemple.
# (Note: en raison des limitations de la plateforme de démonstration Go,
# cet exemple ne peut être exécuté que sur votre ordinateur local.)
$ mkdir -p dossier
$ echo "bonjour go" > dossier/fichier_unique.txt
$ echo "123" > dossier/fichier1.hash
$ echo "456" > dossier/fichier2.hash

$ go run embed-directive.go
bonjour go
bonjour go
123
456
```

Voici le code complet :

```go
// `//go:embed` est une [directive de compilateur](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives) qui
// permet aux programmes d'inclure des fichiers et des dossiers arbitraires dans le binaire Go au moment de la compilation. En savoir plus sur la directive d'insertion
// [ici](https://pkg.go.dev/embed).
package main

// Importez le package `embed` ; si vous n'utilisez aucun identifiant exporté
// de ce package, vous pouvez effectuer une importation vide avec `_ "embed"`.
import (
	"embed"
)

// Les directives `embed` acceptent des chemins relatifs au répertoire contenant le
// fichier source Go. Cette directive insère le contenu du fichier dans la
// variable `string` qui le suit immédiatement.
//
//go:embed dossier/fichier_unique.txt
var chaineFichier string

// Ou insérez le contenu du fichier dans un `[]byte`.
//
//go:embed dossier/fichier_unique.txt
var octetsFichier []byte

// Nous pouvons également insérer plusieurs fichiers ou même des dossiers avec des caractères génériques. Cela utilise
// une variable du type [embed.FS](https://pkg.go.dev/embed#FS), qui
// implémente un système de fichiers virtuel simple.
//
//go:embed dossier/fichier_unique.txt
//go:embed dossier/*.hash
var dossier embed.FS

func main() {

	// Affichez le contenu de `fichier_unique.txt`.
	print(chaineFichier)
	print(string(octetsFichier))

	// Récupérez quelques fichiers du dossier inséré.
	contenu1, _ := dossier.ReadFile("dossier/fichier1.hash")
	print(string(contenu1))

	contenu2, _ := dossier.ReadFile("dossier/fichier2.hash")
	print(string(contenu2))
}

```
