# Slices

Le problème à résoudre dans ce laboratoire est de créer et de manipuler des slices en Go. Vous devrez créer un slice vide avec une longueur non nulle, définir et obtenir des valeurs dans le slice, utiliser la fonction `len` pour obtenir la longueur du slice, utiliser la fonction `append` pour ajouter de nouvelles valeurs au slice, utiliser la fonction `copy` pour copier un slice et utiliser l'opérateur de slice pour obtenir un slice d'éléments à partir d'un slice existant.

Pour terminer ce laboratoire, vous devrez avoir une compréhension de base de la syntaxe Go et du type de données slice. Vous devrez également être familier avec les fonctions `make`, `append` et `copy`, ainsi que l'opérateur de slice.

```sh
# Notez que bien que les slices soient de différents types que les tableaux,
# ils sont affichés de manière similaire par `fmt.Println`.
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Consultez ce [super article de blog](https://go.dev/blog/slices-intro)
# de l'équipe Go pour plus de détails sur la conception et
# l'implémentation des slices en Go.

# Maintenant que nous avons vu les tableaux et les slices, nous allons examiner
# la principale structure de données intégrée d'autres clés de Go: les cartes.
```

Voici le code complet ci-dessous:

```go
// Les _Slices_ sont un type de données important en Go, donnant
// une interface plus puissante pour les séquences que les tableaux.

package main

import "fmt"

func main() {

	// Contrairement aux tableaux, les slices sont typés seulement par les
	// éléments qu'ils contiennent (et non par le nombre d'éléments).
	// Pour créer un slice vide avec une longueur non nulle, utilisez
	// la fonction intégrée `make`. Ici, nous créons un slice de
	// `string`s de longueur `3` (initialement avec des valeurs par défaut).
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// Nous pouvons définir et obtenir des valeurs tout comme avec les tableaux.
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` renvoie la longueur du slice comme prévu.
	fmt.Println("len:", len(s))

	// En plus de ces opérations de base, les slices
	// prennent en charge plusieurs autres opérations qui les rendent plus riches que
	// les tableaux. L'une d'entre elles est la fonction intégrée `append`, qui
	// renvoie un slice contenant une ou plusieurs nouvelles valeurs.
	// Notez que nous devons accepter une valeur de retour de
	// `append` car nous pouvons obtenir une nouvelle valeur de slice.
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// Les slices peuvent également être `copy`'s. Ici, nous créons un
	// slice vide `c` de la même longueur que `s` et copions
	// dans `c` à partir de `s`.
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Les slices prennent en charge un opérateur de "slice" avec la syntaxe
	// `slice[low:high]`. Par exemple, cela obtient un slice
	// des éléments `s[2]`, `s[3]` et `s[4]`.
	l := s[2:5]
	fmt.Println("sl1:", l)

	// Cela extrait jusqu'à (mais sans inclure) `s[5]`.
	l = s[:5]
	fmt.Println("sl2:", l)

	// Et cela extrait à partir de (et y compris) `s[2]`.
	l = s[2:]
	fmt.Println("sl3:", l)

	// Nous pouvons également déclarer et initialiser une variable pour un slice
	// en une seule ligne.
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Les slices peuvent être composés en structures de données multi-dimensionnelles.
	// La longueur des slices internes peut varier, contrairement aux tableaux multi-dimensionnels.
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
