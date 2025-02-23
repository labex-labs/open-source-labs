# Range

Le problème à résoudre dans ce laboratoire est de démontrer comment utiliser `range` avec des slices, des tableaux, des maps et des chaînes de caractères.

Pour terminer ce laboratoire, vous aurez besoin de :

- Connaissances de base sur la syntaxe Golang
- Golang installé sur votre machine

```sh
$ go run range.go
sum: 9
index: 1
a - > apple
b - > banana
key: a
key: b
0 103
1 111
```

Voici le code complet ci-dessous :

```go
// _range_ itère sur les éléments dans diverses structures de données.
// Voyons comment utiliser `range` avec certaines des structures de données
// que nous avons déjà apprises.

package main

import "fmt"

func main() {

	// Ici, nous utilisons `range` pour additionner les nombres dans un slice.
	// Les tableaux fonctionnent de la même manière.
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// `range` sur les tableaux et les slices fournit à la fois
	// l'index et la valeur pour chaque entrée. Plus haut, nous n'avions
	// pas besoin de l'index, donc nous l'avons ignoré avec
	// l'identificateur vide `_`. Parfois, nous avons réellement besoin
	// des index.
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// `range` sur une map itère sur les paires clé/valeur.
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` peut également itérer seulement sur les clés d'une map.
	for k := range kvs {
		fmt.Println("key:", k)
	}

	// `range` sur les chaînes de caractères itère sur les points de code Unicode.
	// La première valeur est l'index d'octet de départ du `rune` et la seconde
	// le `rune` lui-même. Consultez [Strings and Runes](strings-and-runes)
	// pour plus de détails.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}

```
