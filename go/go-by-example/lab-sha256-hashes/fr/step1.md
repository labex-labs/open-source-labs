# SHA256 Hashes

Étant donné une chaîne de caractères, calculez son hachage SHA256.

- Le programme doit importer les packages `crypto/sha256` et `fmt`.
- Le programme doit utiliser la fonction `sha256.New()` pour créer un nouveau hachage.
- Le programme doit utiliser la fonction `Write` pour écrire les octets de la chaîne de caractères dans le hachage.
- Le programme doit utiliser la fonction `Sum` pour obtenir le résultat final du hachage sous forme de tableau d'octets.
- Le programme doit afficher la chaîne de caractères originale et le résultat du hachage au format hexadécimal.

```sh
# L'exécution du programme calcule le hachage et l'affiche
# au format hexadécimal lisible par l'homme.
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Vous pouvez calculer d'autres hachages en utilisant un modèle similaire
# à celui présenté ci-dessus. Par exemple, pour calculer
# les hachages SHA512, importez `crypto/sha512` et utilisez
# `sha512.New()`.

# Notez que si vous avez besoin de hachages cryptographiquement sûrs,
# vous devriez effectuer des recherches approfondies
# sur [la force des hachages](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```

Voici le code complet ci-dessous :

```go
// [_Hachages SHA256_](https://en.wikipedia.org/wiki/SHA-2) sont
// fréquemment utilisés pour calculer de courtes identités pour des blocs binaires
// ou de texte. Par exemple, les certificats TLS/SSL utilisent SHA256
// pour calculer la signature d'un certificat. Voici comment calculer
// les hachages SHA256 en Go.

package main

// Go implémente plusieurs fonctions de hachage dans divers
// packages `crypto/*`.
import (
	"crypto/sha256"
	"fmt"
)

func main() {
	s := "sha256 this string"

	// Ici, nous commençons avec un nouveau hachage.
	h := sha256.New()

	// `Write` attend des octets. Si vous avez une chaîne de caractères `s`,
	// utilisez `[]byte(s)` pour la convertir en octets.
	h.Write([]byte(s))

	// Cela obtient le résultat final du hachage sous forme de tableau d'octets.
	// L'argument de `Sum` peut être utilisé pour ajouter à un tableau d'octets existant :
	// il n'est généralement pas nécessaire.
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}

```
