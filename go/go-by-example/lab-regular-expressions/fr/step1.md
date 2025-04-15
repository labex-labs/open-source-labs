# Expressions régulières

Le laboratoire vous demande de compléter le code pour effectuer diverses tâches liées aux expressions régulières en Golang.

- Utilisez le package `regexp` pour effectuer des tâches liées aux expressions régulières.
- Utilisez `MatchString` pour tester si un motif correspond à une chaîne de caractères.
- Utilisez `Compile` pour optimiser une structure `Regexp`.
- Utilisez `MatchString` pour tester une correspondance comme `Compile`.
- Utilisez `FindString` pour trouver la correspondance pour l'expression régulière.
- Utilisez `FindStringIndex` pour trouver la première correspondance et retourner les index de début et de fin de la correspondance au lieu du texte correspondant.
- Utilisez `FindStringSubmatch` pour retourner des informations pour à la fois `p([a-z]+)ch` et `([a-z]+)`.
- Utilisez `FindStringSubmatchIndex` pour retourner des informations sur les index des correspondances et des sous-correspondances.
- Utilisez `FindAllString` pour trouver toutes les correspondances pour une expression régulière.
- Utilisez `FindAllStringSubmatchIndex` pour appliquer à toutes les correspondances dans l'entrée, pas seulement à la première.
- Utilisez `Match` pour tester une correspondance avec des arguments `[]byte` et supprimer `String` du nom de la fonction.
- Utilisez `MustCompile` pour créer des variables globales avec des expressions régulières.
- Utilisez `ReplaceAllString` pour remplacer des sous-ensembles de chaînes de caractères avec d'autres valeurs.
- Utilisez `ReplaceAllFunc` pour transformer le texte correspondant avec une fonction donnée.

```sh
# Pour une référence complète sur les expressions régulières en Go, consultez
# la documentation du package [`regexp`](https://pkg.go.dev/regexp).
```

Voici le code complet ci-dessous :

```go
// Go offre une prise en charge intégrée des [expressions régulières](https://en.wikipedia.org/wiki/Regular_expression).
// Voici quelques exemples de tâches courantes liées aux expressions régulières
// en Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// Cela teste si un motif correspond à une chaîne de caractères.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// Plus haut, nous avons utilisé directement un motif sous forme de chaîne, mais pour
	// d'autres tâches liées aux expressions régulières, vous devrez `Compiler` une
	// structure `Regexp` optimisée.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// De nombreuses méthodes sont disponibles sur ces structures. Voici
	// un test de correspondance comme nous l'avons vu plus tôt.
	fmt.Println(r.MatchString("peach"))

	// Cela trouve la correspondance pour l'expression régulière.
	fmt.Println(r.FindString("peach punch"))

	// Cela trouve également la première correspondance mais retourne les
	// index de début et de fin de la correspondance au lieu du
	// texte correspondant.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// Les variantes `Submatch` incluent des informations à la fois sur
	// les correspondances du motif complet et les sous-correspondances
	// à l'intérieur de ces correspondances. Par exemple, cela retournera
	// des informations pour à la fois `p([a-z]+)ch` et `([a-z]+)`.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// De même, cela retournera des informations sur les index des correspondances et des sous-correspondances.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// Les variantes `All` de ces fonctions s'appliquent à toutes les
	// correspondances dans l'entrée, pas seulement à la première. Par
	// exemple, pour trouver toutes les correspondances pour une expression régulière.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// Ces variantes `All` sont également disponibles pour les autres
	// fonctions que nous avons vues ci-dessus.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// Fournir un entier non négatif en tant que deuxième
	// argument à ces fonctions limitera le nombre de correspondances.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// Nos exemples ci-dessus avaient des arguments de chaîne de caractères et utilisaient
	// des noms comme `MatchString`. Nous pouvons également fournir
	// des arguments `[]byte` et supprimer `String` du nom de la fonction.
	fmt.Println(r.Match([]byte("peach")))

	// Lors de la création de variables globales avec des expressions régulières, vous pouvez utiliser la variante
	// `MustCompile` de `Compile`. `MustCompile` provoque une panique au lieu de
	// retourner une erreur, ce qui la rend plus sûre à utiliser pour les
	// variables globales.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// Le package `regexp` peut également être utilisé pour remplacer
	// des sous-ensembles de chaînes de caractères avec d'autres valeurs.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// La variante `Func` vous permet de transformer le texte correspondant avec une fonction donnée.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
