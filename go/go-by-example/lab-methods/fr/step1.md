# Méthodes

Le code fourni définit un type de structure appelé `rect` avec deux champs, `width` et `height`. Deux méthodes sont définies pour ce type de structure, `area` et `perim`. La méthode `area` calcule l'aire du rectangle, et la méthode `perim` calcule le périmètre du rectangle. La fonction principale appelle ces deux méthodes et imprime leurs résultats.

- La méthode `area` devrait avoir un type de récepteur de `*rect`.
- La méthode `perim` devrait avoir un type de récepteur de `rect`.
- La méthode `area` devrait renvoyer l'aire du rectangle.
- La méthode `perim` devrait renvoyer le périmètre du rectangle.
- La fonction `main` devrait appeler les deux méthodes et imprimer leurs résultats.

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Ensuite, nous examinerons le mécanisme de Go pour regrouper et
# nommer des ensembles de méthodes apparentées : les interfaces.
```

Voici le code complet ci-dessous :

```go
// Go prend en charge les _méthodes_ définies sur les types de structure.

package main

import "fmt"

type rect struct {
	width, height int
}

// Cette méthode `area` a un _type de récepteur_ de `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Les méthodes peuvent être définies pour des types de récepteur
// de pointeur ou de valeur. Voici un exemple d'un récepteur de valeur.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Ici, nous appelons les 2 méthodes définies pour notre structure.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go gère automatiquement la conversion entre les valeurs
	// et les pointeurs pour les appels de méthode. Vous pouvez vouloir utiliser
	// un type de récepteur de pointeur pour éviter la copie lors des appels de méthode
	// ou pour permettre à la méthode de modifier la
	// structure reçue.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}

```
