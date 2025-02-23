# Tableaux

Vous devrez créer un tableau d'entiers d'une longueur de 5. Vous devrez ensuite définir une valeur à un index spécifique et récupérer une valeur à partir d'un index spécifique. Vous devrez également trouver la longueur du tableau et déclarer et initialiser un tableau en une seule ligne. Enfin, vous créerez un tableau à deux dimensions et le initialiserez avec des valeurs.

- Créez un tableau d'entiers d'une longueur de 5
- Définissez une valeur à un index spécifique et récupérez une valeur à partir d'un index spécifique
- Trouvez la longueur du tableau
- Déclarez et initialisez un tableau en une seule ligne
- Créez un tableau à deux dimensions et initialisez-le avec des valeurs

```sh
# Notez que les tableaux apparaissent sous la forme `[v1 v2 v3...]`
# lorsqu'ils sont imprimés avec `fmt.Println`.
$ go run arrays.go
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d: [[0 1 2] [1 2 3]]
```

Voici le code complet ci-dessous :

```go
// En Go, un _tableau_ est une séquence numérotée d'éléments d'un
// type spécifique et d'une longueur spécifique. Dans le code Go
// habituel, les [slices](slices) sont beaucoup plus courants ;
// les tableaux sont utiles dans certains cas particuliers.

package main

import "fmt"

func main() {

	// Ici, nous créons un tableau `a` qui peut stocker exactement
	// 5 `int`. Le type des éléments et la longueur font partie
	// du type du tableau. Par défaut, un tableau est
	// initialisé avec des valeurs zéro, ce qui signifie `0` pour
	// les `int`.
	var a [5]int
	fmt.Println("emp:", a)

	// Nous pouvons définir une valeur à un index en utilisant
	// la syntaxe `array[index] = value`, et récupérer une valeur
	// avec `array[index]`.
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// La fonction intégrée `len` renvoie la longueur d'un tableau.
	fmt.Println("len:", len(a))

	// Utilisez cette syntaxe pour déclarer et initialiser un tableau
	// en une seule ligne.
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Les types de tableaux sont unidimensionnels, mais vous pouvez
	// composer des types pour construire des structures de données
	// multidimensionnelles.
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
