# Range Over Channels

Vous êtes requis d'écrire une fonction qui prend un canal d'entiers et renvoie la somme de tous les entiers reçus à partir du canal.

- La fonction doit s'appeler `sumInts`.
- La fonction doit prendre un seul paramètre de type `chan int`.
- La fonction doit renvoyer une seule valeur entière.
- Vous n'êtes pas autorisé à utiliser de boucles ou de récursion à l'intérieur du corps de la fonction.
- Vous n'êtes pas autorisé à utiliser de packages externes.

```sh
$ go run range-over-channels.go
one
two

# Cet exemple a également montré qu'il est possible de fermer
# un canal non vide mais de recevoir encore les valeurs restantes.
```

Voici le code complet ci-dessous :

```go
// Dans un [exemple précédent](range), nous avons vu comment `for` et
// `range` permettent d'itérer sur des structures de données de base.
// Nous pouvons également utiliser cette syntaxe pour itérer sur
// les valeurs reçues à partir d'un canal.

package main

import "fmt"

func main() {

	// Nous allons itérer sur 2 valeurs dans le canal `queue`.
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// Cette `range` itère sur chaque élément au fur et à mesure qu'il est
	// reçu à partir de `queue`. Comme nous avons `fermé` le
	// canal ci-dessus, l'itération se termine après
	// avoir reçu les 2 éléments.
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
