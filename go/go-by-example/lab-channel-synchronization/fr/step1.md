# Synchronisation par canal

Le problème à résoudre dans ce laboratoire est de créer une goroutine qui effectue un certain travail et qui avertit une autre goroutine lorsqu'elle a terminé, en utilisant un canal.

Pour terminer ce laboratoire, vous devrez :

- Créer une fonction nommée `worker` qui prend en paramètre un canal de type `bool`.
- Dans la fonction `worker`, effectuer un certain travail puis envoyer une valeur au canal pour signaler que le travail est terminé.
- Dans la fonction `main`, créer un canal de type `bool` avec une taille de tampon de 1.
- Démarrer une goroutine qui appelle la fonction `worker` et passe le canal en paramètre.
- Bloquer la fonction `main` jusqu'à ce qu'une valeur soit reçue du canal.

```sh
$ go run channel-synchronization.go
working...done

# Si vous avez supprimé la ligne `<- done` de ce programme, le
# programme se terminerait avant que le `worker` ne
# démarre même.
```

Voici le code complet ci-dessous :

```go
// Nous pouvons utiliser des canaux pour synchroniser l'exécution
// entre des goroutines. Voici un exemple d'utilisation d'une
// réception bloquante pour attendre qu'une goroutine se termine.
// Lorsque vous attendez que plusieurs goroutines se terminent,
// vous pouvez préférer utiliser un [WaitGroup](waitgroups).

package main

import (
	"fmt"
	"time"
)

// Cette est la fonction que nous exécuterons dans une goroutine. Le
// canal `done` sera utilisé pour avertir une autre
// goroutine que le travail de cette fonction est terminé.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Envoyez une valeur pour signaler que nous avons fini.
	done <- true
}

func main() {

	// Démarrez une goroutine de travail, en lui donnant le canal pour
	// avertir.
	done := make(chan bool, 1)
	go worker(done)

	// Bloquez jusqu'à ce que nous recevions une notification du
	// travailleur sur le canal.
	<-done
}

```
