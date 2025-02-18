# Mise en forme de chaînes de caractères

Vous devez formater différents types de données en utilisant divers verbes de formatage en Golang.

- Vous devez utiliser le package `fmt` pour formater les données.
- Vous devez utiliser le bon verbe de formatage pour chaque type de données.
- Vous devez être capable de formater des entiers, des nombres à virgule flottante, des chaînes de caractères et des structures.
- Vous devez être capable de contrôler la largeur et la précision de la sortie.
- Vous devez être capable d'aligner la sortie à gauche ou à droite.

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char:!
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```

Voici le code complet ci-dessous :

```go
// Go offre un excellent support pour la mise en forme de chaînes de caractères
// dans la tradition de `printf`. Voici quelques exemples de tâches courantes
// de mise en forme de chaînes de caractères.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go propose plusieurs "verbes" d'impression conçus pour
	// formater des valeurs Go générales. Par exemple, ceci imprime
	// une instance de notre structure `point`.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// Si la valeur est une structure, la variante `%+v` inclura
	// les noms des champs de la structure.
	fmt.Printf("struct2: %+v\n", p)

	// La variante `%#v` imprime une représentation syntaxique Go
	// de la valeur, c'est-à-dire le extrait de code source qui
	// produirait cette valeur.
	fmt.Printf("struct3: %#v\n", p)

	// Pour imprimer le type d'une valeur, utilisez `%T`.
	fmt.Printf("type: %T\n", p)

	// La mise en forme des booléens est simple.
	fmt.Printf("bool: %t\n", true)

	// Il existe de nombreuses options pour la mise en forme des entiers.
	// Utilisez `%d` pour la mise en forme standard en base 10.
	fmt.Printf("int: %d\n", 123)

	// Ceci imprime une représentation binaire.
	fmt.Printf("bin: %b\n", 14)

	// Ceci imprime le caractère correspondant à l'entier donné.
	fmt.Printf("char: %c\n", 33)

	// `%x` fournit un encodage hexadécimal.
	fmt.Printf("hex: %x\n", 456)

	// Il existe également plusieurs options de mise en forme pour
	// les nombres à virgule flottante. Pour une mise en forme décimale de base, utilisez `%f`.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` et `%E` formatent le nombre à virgule flottante en notation scientifique
	// (avec des versions légèrement différentes).
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// Pour l'impression de base de chaînes de caractères, utilisez `%s`.
	fmt.Printf("str1: %s\n", "\"string\"")

	// Pour citer des chaînes de caractères entre guillemets doubles comme dans le code source Go, utilisez `%q`.
	fmt.Printf("str2: %q\n", "\"string\"")

	// Comme pour les entiers vus précédemment, `%x` rend la chaîne de caractères
	// en base 16, avec deux caractères de sortie par octet d'entrée.
	fmt.Printf("str3: %x\n", "hex this")

	// Pour imprimer une représentation d'un pointeur, utilisez `%p`.
	fmt.Printf("pointer: %p\n", &p)

	// Lors de la mise en forme de nombres, vous aurez souvent envie de
	// contrôler la largeur et la précision du résultat. Pour spécifier la largeur d'un entier, utilisez un
	// nombre après le `%` dans le verbe. Par défaut, le résultat sera aligné à droite et complété avec
	// des espaces.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// Vous pouvez également spécifier la largeur des nombres à virgule flottante imprimés,
	// bien que vous voudrez généralement également limiter la précision décimale en même temps
	// avec la syntaxe largeur.précision.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// Pour aligner à gauche, utilisez le drapeau `-`.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// Vous voudrez peut-être également contrôler la largeur lors de la mise en forme
	// des chaînes de caractères, en particulier pour vous assurer qu'elles s'alignent
	// dans une sortie de type tableau. Pour une largeur alignée à droite de base.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// Pour aligner à gauche, utilisez le drapeau `-` comme pour les nombres.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// Jusqu'à présent, nous avons vu `Printf`, qui imprime la chaîne de caractères formatée
	// sur `os.Stdout`. `Sprintf` formate et renvoie une chaîne de caractères sans l'imprimer nulle part.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// Vous pouvez formater et imprimer sur des `io.Writers` autres que
	// `os.Stdout` en utilisant `Fprintf`.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}

```
