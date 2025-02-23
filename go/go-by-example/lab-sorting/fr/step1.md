# Tri

Le problème à résoudre dans ce laboratoire est de trier des slices de chaînes de caractères et d'entiers à l'aide du package `sort`.

- Le package `sort` doit être importé.
- La fonction `sort.Strings()` doit être utilisée pour trier un slice de chaînes de caractères.
- La fonction `sort.Ints()` doit être utilisée pour trier un slice d'entiers.
- La fonction `sort.IntsAreSorted()` doit être utilisée pour vérifier si un slice d'entiers est déjà trié.

```sh
# Exécuter notre programme affiche les slices de chaînes de caractères et d'entiers triés
# et `true` comme résultat de notre test `AreSorted`.
$ go run sorting.go
Chaînes de caractères : [a b c]
Entiers : [2 4 7]
Trié : true
```

Voici le code complet ci-dessous :

```go
// Le package `sort` de Go implémente le tri pour les types intégrés
// et les types définis par l'utilisateur. Nous allons d'abord examiner le tri pour
// les types intégrés.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// Les méthodes de tri sont spécifiques au type intégré ;
	// voici un exemple pour les chaînes de caractères. Notez que le tri est
	// in-place, donc il modifie le slice donné et ne renvoie pas un nouveau.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Chaînes de caractères :", strs)

	// Un exemple de tri d'`int`.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Entiers :   ", ints)

	// Nous pouvons également utiliser `sort` pour vérifier si un slice est
	// déjà trié.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Trié : ", s)
}

```
