# Recover

La fonction `mayPanic` dans le code fourni provoquera un `panic` lorsqu'elle sera appelée. Votre tâche consiste à modifier la fonction `main` pour récupérer du `panic` et afficher le message d'erreur.

- Utilisez la fonction `recover` pour gérer le `panic` dans la fonction `mayPanic`.
- Affichez le message d'erreur lorsqu'un `panic` se produit.

```sh
$ go run recover.go
Recovered. Error:
a problem
```

Voici le code complet ci-dessous :

```go
// Go permet de _récupérer_ d'un `panic`, en utilisant
// la fonction intégrée `recover`. Un `recover` peut
// empêcher un `panic` d'arrêter le programme et le laisser
// continuer l'exécution à la place.

// Un exemple où cela peut être utile : un serveur
// ne veut pas planter si l'une des connexions clientes
// présente une erreur critique. Au lieu de cela, le serveur
// voudrait fermer cette connexion et continuer à servir
// les autres clients. En fait, c'est ce que fait par défaut
// Go's `net/http` pour les serveurs HTTP.

package main

import "fmt"

// Cette fonction provoque un `panic`.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` doit être appelé dans une fonction différée.
	// Lorsque la fonction englobante provoque un `panic`, le
	// différé sera activé et un appel à `recover` à l'intérieur
	// de celui-ci capturera le `panic`.
	defer func() {
		if r := recover(); r!= nil {
			// La valeur de retour de `recover` est l'erreur levée dans
			// l'appel à `panic`.
			fmt.Println("Recovered. Error:\n", r)
		}
	}()

	mayPanic()

	// Ce code ne sera pas exécuté, car `mayPanic` provoque un `panic`.
	// L'exécution de `main` s'arrête au moment du `panic` et
	// reprend dans la fermeture différée.
	fmt.Println("After mayPanic()")
}

```
