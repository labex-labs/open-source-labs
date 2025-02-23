# Closures

Vous devez créer une fonction qui renvoie une autre fonction. La fonction renvoyée devrait incrémenter d'une unité une variable à chaque fois qu'elle est appelée. La variable devrait être unique pour chaque fonction renvoyée.

- La fonction `intSeq` devrait renvoyer une autre fonction.
- La fonction renvoyée devrait incrémenter d'une unité une variable à chaque fois qu'elle est appelée.
- La variable devrait être unique pour chaque fonction renvoyée.

```sh
$ go run closures.go
1
2
3
1

# La dernière caractéristique des fonctions que nous allons examiner pour l'instant est
# la récursion.
```

Voici le code complet ci-dessous :

```go
// Go prend en charge les [_fonctions anonymes_](https://en.wikipedia.org/wiki/Anonymous_function),
// qui peuvent former des <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>fermetures</em></a>.
// Les fonctions anonymes sont utiles lorsque vous voulez définir
// une fonction en ligne sans avoir à lui donner un nom.

package main

import "fmt"

// Cette fonction `intSeq` renvoie une autre fonction, que
// nous définissons anonymement dans le corps de `intSeq`. La
// fonction renvoyée _ferme sur_ la variable `i` pour
// former une fermeture.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// Nous appelons `intSeq`, en assignant le résultat (une fonction)
	// à `nextInt`. Cette valeur de fonction capture sa
	// propre valeur de `i`, qui sera mise à jour chaque fois
	// que nous appelons `nextInt`.
	nextInt := intSeq()

	// Voir l'effet de la fermeture en appelant `nextInt`
	// plusieurs fois.
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// Pour confirmer que l'état est unique à cette
	// fonction particulière, créer et tester une nouvelle.
	newInts := intSeq()
	fmt.Println(newInts())
}

```
