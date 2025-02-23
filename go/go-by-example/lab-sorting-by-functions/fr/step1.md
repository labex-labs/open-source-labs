# Tri par fonctions

Le problème à résoudre dans ce laboratoire est d'implémenter une fonction de tri personnalisée en Go qui trie un slice de chaînes de caractères par leur longueur.

- Le type `byLength` devrait être créé comme un alias pour le type `[]string`.
- L'interface `sort.Interface` devrait être implémentée sur le type `byLength`.
- Les fonctions `Len` et `Swap` devraient être implémentées sur le type `byLength`.
- La fonction `Less` devrait être implémentée sur le type `byLength` pour contenir la logique de tri personnalisée réelle.
- La fonction `main` devrait convertir le slice original `fruits` en `byLength`, puis utiliser `sort.Sort` sur ce slice typé.

```sh
# En exécutant notre programme, on obtient une liste triée
# par la longueur des chaînes, comme souhaité.
$ go run sorting-by-functions.go
[kiwi peach banana]

# En suivant ce même modèle de création d'un type
# personnalisé, d'implémentation des trois méthodes
# `Interface` sur ce type, puis d'appel de `sort.Sort`
# sur une collection de ce type personnalisé, on peut
# trier les slices Go par des fonctions arbitraires.
```

Voici le code complet ci-dessous :

```go
// Parfois, on voudra trier une collection autrement que
// dans son ordre naturel. Par exemple, supposons que
// l'on veuille trier les chaînes de caractères par leur
// longueur plutôt que par ordre alphabétique. Voici un
// exemple de tris personnalisés en Go.

package main

import (
	"fmt"
	"sort"
)

// Pour trier par une fonction personnalisée en Go, on a
// besoin d'un type correspondant. Ici, on a créé un type
// `byLength` qui n'est qu'un alias pour le type
// intégrée `[]string`.
type byLength []string

// On implémente l'interface `sort.Interface` - `Len`,
// `Less` et `Swap` - sur notre type pour pouvoir utiliser
// la fonction générique `Sort` du package `sort`. `Len`
// et `Swap` seront généralement similaires pour les
// différents types et `Less` contiendra la logique de tri
// personnalisée réelle. Dans notre cas, on veut trier
// dans l'ordre croissant de la longueur des chaînes,
// donc on utilise `len(s[i])` et `len(s[j])` ici.
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// Avec tout cela en place, on peut maintenant implémenter
// notre tri personnalisé en convertissant le slice
// original `fruits` en `byLength`, puis en utilisant
// `sort.Sort` sur ce slice typé.
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}

```
