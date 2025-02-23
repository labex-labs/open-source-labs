# Cartes

Dans ce laboratoire, vous devrez créer une carte qui stocke le nombre de fois où chaque mot apparaît dans une chaîne de caractères donnée. Vous devrez diviser la chaîne en mots, puis itérer sur chaque mot, l'ajoutant à la carte s'il n'existe pas déjà, ou incrémentant son compte s'il existe déjà.

- Vous devez utiliser une carte pour stocker les comptes de mots.
- Vous devez diviser la chaîne d'entrée en mots.
- Vous devez itérer sur chaque mot dans la chaîne d'entrée.
- Vous devez ajouter chaque mot à la carte s'il n'existe pas déjà, ou incrémenter son compte s'il existe déjà.

```sh
# Notez que les cartes apparaissent sous la forme `map[k:v k:v]` lorsqu'elles sont imprimées avec `fmt.Println`.
$ go run maps.go
carte : map[k1:7 k2:13]
v1 : 7
v3 : 0
longueur : 2
carte : map[k1:7]
prs : faux
carte : map[bar:2 foo:1]
```

Voici le code complet ci-dessous :

```go
// Les _cartes_ sont le type de données associatif intégré de Go
// (quelquefois appelé _hashtable_ ou _dictionnaire_ dans d'autres langages).

package main

import "fmt"

func main() {

	// Pour créer une carte vide, utilisez la fonction intégrée `make` :
	// `make(map[type-de-clé]type-de-valeur)`.
	m := make(map[string]int)

	// Définissez des paires clé/valeur en utilisant la syntaxe `nom[clé] = valeur` classique.
	m["k1"] = 7
	m["k2"] = 13

	// Imprimer une carte avec par exemple `fmt.Println` affichera toutes ses paires clé/valeur.
	fmt.Println("carte :", m)

	// Obtenez une valeur pour une clé avec `nom[clé]`.
	v1 := m["k1"]
	fmt.Println("v1 :", v1)

	// Si la clé n'existe pas, la [valeur par défaut](https://go.dev/ref/spec#The_zero_value) du type de valeur est renvoyée.
	v3 := m["k3"]
	fmt.Println("v3 :", v3)

	// La fonction intégrée `len` renvoie le nombre de paires clé/valeur lorsqu'elle est appelée sur une carte.
	fmt.Println("longueur :", len(m))

	// La fonction intégrée `delete` supprime des paires clé/valeur d'une carte.
	delete(m, "k2")
	fmt.Println("carte :", m)

	// La deuxième valeur de retour optionnelle lorsqu'on obtient une valeur à partir d'une carte indique si la clé était présente dans la carte. Cela peut être utilisé pour distinguer entre des clés manquantes et des clés avec des valeurs par défaut comme `0` ou `""`. Ici, nous n'avions pas besoin de la valeur elle-même, donc nous l'avons ignorée avec l'_identificateur vide_ `_`.
	_, prs := m["k2"]
	fmt.Println("prs :", prs)

	// Vous pouvez également déclarer et initialiser une nouvelle carte sur la même ligne avec cette syntaxe.
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("carte :", n)
}

```
