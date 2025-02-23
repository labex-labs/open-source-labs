# Génériques

Le problème à résoudre dans ce laboratoire est de comprendre comment définir et utiliser des fonctions et des types génériques en Golang.

- Comprendre le concept de génériques en Golang.
- Savoir comment définir des fonctions génériques avec des paramètres de type et des contraintes.
- Savoir comment définir des types génériques avec des paramètres de type.
- Comprendre comment définir des méthodes sur des types génériques.
- Savoir comment invoquer des fonctions génériques avec une déduction de type.

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

Voici le code complet ci-dessous :

```go
// À partir de la version 1.18, Go a ajouté la prise en charge des
// _génériques_, également appelés _paramètres de type_.

package main

import "fmt"

// En tant qu'exemple de fonction générique, `MapKeys` prend
// une carte de n'importe quel type et renvoie une slice de ses clés.
// Cette fonction a deux paramètres de type - `K` et `V` ;
// `K` a la contrainte `comparable`, ce qui signifie que
// nous pouvons comparer les valeurs de ce type avec les opérateurs `==` et
// `!=`. Cela est nécessaire pour les clés de carte en Go.
// `V` a la contrainte `any`, ce qui signifie qu'elle n'est pas
// restreinte d'aucune manière (`any` est un alias pour `interface{}`).
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// En tant qu'exemple de type générique, `List` est une
// liste chaînée simple avec des valeurs de n'importe quel type.
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// Nous pouvons définir des méthodes sur des types génériques tout comme nous
// le faisons sur des types normaux, mais nous devons conserver les
// paramètres de type en place. Le type est `List[T]`, pas `List`.
func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

func (lst *List[T]) GetAll() []T {
	var elems []T
	for e := lst.head; e!= nil; e = e.next {
		elems = append(elems, e.val)
	}
	return elems
}

func main() {
	var m = map[int]string{1: "2", 2: "4", 4: "8"}

	// Lors de l'invocation de fonctions génériques, nous pouvons souvent compter
	// sur la _déduction de type_. Notez que nous n'avons pas besoin
	// de spécifier les types pour `K` et `V` lors de l'appel de `MapKeys` - le compilateur les déduit
	// automatiquement.
	fmt.Println("keys:", MapKeys(m))

	//... bien que nous puissions également les spécifier explicitement.
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}

```
