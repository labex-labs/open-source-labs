# Fonctions

Dans le code donné, nous avons deux fonctions `plus` et `plusPlus`. La fonction `plus` prend deux entiers en arguments et renvoie leur somme. La fonction `plusPlus` prend trois entiers en arguments et renvoie leur somme. Votre tâche est de compléter la fonction `plusPlus` en ajoutant le troisième entier à la somme des deux premiers entiers.

- La fonction `plus` devrait prendre deux entiers en arguments et renvoyer leur somme sous forme d'un entier.
- La fonction `plusPlus` devrait prendre trois entiers en arguments et renvoyer leur somme sous forme d'un entier.
- La fonction `plusPlus` devrait utiliser la fonction `plus` pour calculer la somme des deux premiers entiers.

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Il existe plusieurs autres fonctionnalités des fonctions Go. L'une d'entre elles est
# les valeurs de retour multiples, que nous examinerons ensuite.
```

Voici le code complet ci-dessous :

```go
// Les _fonctions_ sont centrales en Go. Nous allons apprendre
// les fonctions avec quelques exemples différents.

package main

import "fmt"

// Voici une fonction qui prend deux `int` et renvoie
// leur somme sous forme d'un `int`.
func plus(a int, b int) int {

	// Go nécessite des retours explicites, c'est-à-dire qu'il ne
	// renverra pas automatiquement la valeur de la dernière
	// expression.
	return a + b
}

// Lorsque vous avez plusieurs paramètres consécutifs
// du même type, vous pouvez omettre le nom de type pour les
// paramètres de même type jusqu'au dernier paramètre qui
// déclare le type.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// Appelez une fonction comme vous l'attendez, avec
	// `name(args)`.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}

```
