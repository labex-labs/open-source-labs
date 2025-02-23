# Interfaces

Le problème est d'implémenter une interface en Go, il suffit d'implémenter toutes les méthodes de l'interface. Ici, nous implémentons `geometry` sur des `rect` et des `circle`.

- Implémenter une interface en Go.
- Implémenter toutes les méthodes de l'interface.
- Utiliser une fonction générique `measure` pour travailler sur n'importe quelle `geometry`.
- Utiliser des instances de structs `circle` et `rect` comme arguments pour `measure`.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Pour en savoir plus sur les interfaces de Go, consultez ce
# [super article de blog](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```

Voici le code complet ci-dessous :

```go
// Les _Interfaces_ sont des collections nommées de signatures de méthodes.

package main

import (
	"fmt"
	"math"
)

// Voici une interface de base pour les formes géométriques.
type geometry interface {
	area() float64
	perim() float64
}

// Pour notre exemple, nous allons implémenter cette interface sur
// les types `rect` et `circle`.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Pour implémenter une interface en Go, il suffit d'implémenter
// toutes les méthodes de l'interface. Ici, nous implémentons
// `geometry` sur les `rect`.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// L'implémentation pour les `circle`.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// Si une variable a un type d'interface, alors nous pouvons appeler
// les méthodes qui sont dans l'interface nommée. Voici une
// fonction générique `measure` qui profite de cela pour travailler
// sur n'importe quelle `geometry`.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Les types de structs `circle` et `rect` implémentent tous les deux
	// l'interface `geometry`, donc nous pouvons utiliser des instances
	// de ces structs comme arguments pour `measure`.
	measure(r)
	measure(c)
}

```
