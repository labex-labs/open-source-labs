# Fonctions de chaîne de caractères

Complétez le code ci-dessous pour afficher la sortie de diverses fonctions de chaîne de caractères fournies par le package `strings`.

- Utilisez le package `strings` pour compléter le laboratoire.
- Utilisez la fonction `fmt.Println` pour afficher la sortie.
- Ne modifiez pas le nom de la fonction ou les paramètres.

```sh
$ go run string-functions.go
Contient : vrai
Compte : 2
Commence par : vrai
Finit par : vrai
Index : 1
Joindre : a-b
Répéter : aaaaa
Remplacer : f00
Remplacer : f0o
Diviser : [a b c d e]
Mettre en minuscules : test
Mettre en majuscules : TEST
```

Voici le code complet ci-dessous :

```go
// Le package `strings` de la bibliothèque standard fournit de nombreuses
// fonctions utiles liées aux chaînes de caractères. Voici quelques exemples
// pour vous donner une idée du package.

package main

import (
	"fmt"
	s "strings"
)

// Nous aliasons `fmt.Println` pour un nom plus court car nous l'utiliserons
// beaucoup ci-dessous.
var p = fmt.Println

func main() {

	// Voici un exemple des fonctions disponibles dans
	// `strings`. Comme ce sont des fonctions du
	// package, et non des méthodes sur l'objet chaîne de caractères lui-même,
	// nous devons passer la chaîne de caractères concernée en tant que premier
	// argument à la fonction. Vous pouvez trouver plus
	// de fonctions dans la documentation du package [`strings`](https://pkg.go.dev/strings).
	p("Contient :  ", s.Contains("test", "es"))
	p("Compte :     ", s.Count("test", "t"))
	p("Commence par : ", s.HasPrefix("test", "te"))
	p("Finit par : ", s.HasSuffix("test", "st"))
	p("Index :     ", s.Index("test", "e"))
	p("Joindre :      ", s.Join([]string{"a", "b"}, "-"))
	p("Répéter :    ", s.Repeat("a", 5))
	p("Remplacer :   ", s.Replace("foo", "o", "0", -1))
	p("Remplacer :   ", s.Replace("foo", "o", "0", 1))
	p("Diviser :     ", s.Split("a-b-c-d-e", "-"))
	p("Mettre en minuscules :   ", s.ToLower("TEST"))
	p("Mettre en majuscules :   ", s.ToUpper("test"))
}

```
