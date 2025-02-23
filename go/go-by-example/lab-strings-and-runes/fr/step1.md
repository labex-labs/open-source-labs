# Chaînes de caractères et runes

Le problème à résoudre dans ce laboratoire est de comprendre comment travailler avec les chaînes de caractères et les runes en Go. Plus précisément, le laboratoire couvrira la manière d'obtenir la longueur d'une chaîne de caractères, d'accéder à un index dans une chaîne de caractères, de compter le nombre de runes dans une chaîne de caractères et d'itérer sur les runes d'une chaîne de caractères.

Pour terminer ce laboratoire, vous devrez :

- Avoir une compréhension de base de la syntaxe Go
- Connaître les chaînes de caractères et les runes en Go
- La bibliothèque standard Go

```sh
$ go run strings-and-runes.go
Longueur : 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Nombre de runes : 6
U+0E2A 'ส' commence à 0
U+0E27 'ว' commence à 3
U+0E31 'ั' commence à 6
U+0E2A 'ส' commence à 9
U+0E14 'ด' commence à 12
U+0E35 'ี' commence à 15

En utilisant DecodeRuneInString
U+0E2A 'ส' commence à 0
trouvé so sua
U+0E27 'ว' commence à 3
U+0E31 'ั' commence à 6
U+0E2A 'ส' commence à 9
trouvé so sua
U+0E14 'ด' commence à 12
U+0E35 'ี' commence à 15
```

Voici le code complet ci-dessous :

```go
// Une chaîne de caractères Go est une tranche de bytes en lecture seule. Le langage
// et la bibliothèque standard traitent les chaînes de caractères de manière spéciale - comme
// des conteneurs de texte encodé en [UTF-8](https://en.wikipedia.org/wiki/UTF-8).
// Dans d'autres langages, les chaînes de caractères sont composées de "caractères".
// En Go, le concept de caractère est appelé `rune` - c'est
// un entier qui représente un point de code Unicode.
// [Ce billet de blog Go](https://go.dev/blog/strings) est une bonne
// introduction au sujet.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` est une `chaîne de caractères` affectée d'une valeur littérale
	// représentant le mot "bonjour" en langue thaï. Les littéraux de chaîne de caractères Go sont du texte encodé en UTF-8.
	const s = "สวัสดี"

	// Étant donné que les chaînes de caractères sont équivalentes à `[]byte`, cela
	// produira la longueur des bytes bruts stockés à l'intérieur.
	fmt.Println("Longueur :", len(s))

	// L'indexation dans une chaîne de caractères produit les valeurs de byte brutes à
	// chaque index. Cette boucle génère les valeurs hexadécimales de tous
	// les bytes qui constituent les points de code dans `s`.
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// Pour compter combien de _runes_ sont dans une chaîne de caractères, nous pouvons utiliser
	// le package `utf8`. Notez que la durée d'exécution de
	// `RuneCountInString` dépend de la taille de la chaîne de caractères,
	// car elle doit décoder chaque rune UTF-8 séquentiellement.
	// Certains caractères thaï sont représentés par plusieurs points de code UTF-8
	// donc le résultat de ce comptage peut être surprenant.
	fmt.Println("Nombre de runes :", utf8.RuneCountInString(s))

	// Une boucle `range` traite les chaînes de caractères de manière spéciale et décode
	// chaque `rune` ainsi que son décalage dans la chaîne de caractères.
	for idx, runeValue := range s {
		fmt.Printf("%#U commence à %d\n", runeValue, idx)
	}

	// Nous pouvons obtenir la même itération en utilisant explicitement la
	// fonction `utf8.DecodeRuneInString`.
	fmt.Println("\nEn utilisant DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U commence à %d\n", runeValue, i)
		w = width

		// Cela démontre le passage d'une valeur de `rune` à une fonction.
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// Les valeurs entourées de guillemets simples sont des _littéraux de rune_. Nous
	// pouvons comparer une valeur de `rune` à un littéral de rune directement.
	if r == 't' {
		fmt.Println("trouvé tee")
	} else if r == 'ส' {
		fmt.Println("trouvé so sua")
	}
}

```
