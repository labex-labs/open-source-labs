# `for`

Le code ci-dessous contient différents types de boucles `for`. Cependant, certaines parties du code sont incomplètes, et vous devrez compléter les espaces vides pour que le code fonctionne correctement.

- Connaissance de base de la syntaxe Golang
- Familiarité avec les boucles `for` en Golang

```sh
$ go run for.go
1
2
3
7
8
9
boucle
1
3
5

# Nous verrons d'autres formes de `for` plus tard lorsque nous examinerons
# les instructions `range`, les canaux et d'autres structures de données.
```

Voici le code complet :

```go
// `for` est la seule structure de boucle en Go. Voici
// quelques types de base de boucles `for`.

package main

import "fmt"

func main() {

	// Le type le plus simple, avec une seule condition.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Une boucle `for` classique avec initialisation/condition/après.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` sans condition bouclera indéfiniment
	// jusqu'à ce que vous sortiez de la boucle avec `break` ou
	// que vous retourniez de la fonction englobante avec `return`.
	for {
		fmt.Println("boucle")
		break
	}

	// Vous pouvez également passer à l'itération suivante
	// de la boucle avec `continue`.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
