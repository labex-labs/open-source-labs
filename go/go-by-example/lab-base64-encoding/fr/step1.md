# Encodage Base64

Vous êtes requis d'écrire un programme Golang qui encode et décode une chaîne donnée en utilisant l'encodage Base64 standard et compatible URL.

- Le programme devrait importer le package `encoding/base64` avec le nom `b64` au lieu du nom par défaut `base64`.
- Le programme devrait encoder la chaîne donnée en utilisant l'encodage Base64 standard et compatible URL.
- Le programme devrait décoder la chaîne encodée en utilisant le décodage Base64 standard et compatible URL.
- Le programme devrait afficher les chaînes encodées et décodées dans la console.

```sh
# La chaîne s'encode en valeurs légèrement différentes avec les
# encodeurs Base64 standard et URL (dernier caractère `+` vs `-`)
# mais elles se décodent toutes les deux en chaîne d'origine comme souhaité.
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```

Voici le code complet ci-dessous :

```go
// Go fournit une prise en charge intégrée de l'[encodage/décodage
// Base64](https://en.wikipedia.org/wiki/Base64).

package main

// Cette syntaxe importe le package `encoding/base64` avec
// le nom `b64` au lieu du nom par défaut `base64`. Cela nous
// économisera de l'espace ci-dessous.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// Voici la `string` que nous allons encoder/décoder.
	data := "abc123!?$*&()'-=@~"

	// Go prend en charge à la fois l'encodage Base64 standard et
	// compatible URL. Voici comment encoder en utilisant l'encodeur
	// standard. L'encodeur nécessite un `[]byte` donc nous
	// convertissons notre `string` en ce type.
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// Le décodage peut retourner une erreur, que vous pouvez vérifier
	// si vous ne savez pas déjà que l'entrée est correctement formée.
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// Cela encode/décode en utilisant un format Base64 compatible URL.
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```
