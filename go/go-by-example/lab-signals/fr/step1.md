# Signaux

Dans certains cas, nous souhaitons que nos programmes Go gèrent intelligemment les signaux Unix. Par exemple, nous pourrions vouloir qu'un serveur s'arrête proprement lorsqu'il reçoit un `SIGTERM`, ou qu'un outil de ligne de commande arrête de traiter l'entrée s'il reçoit un `SIGINT`.

- Créez un canal tamponné pour recevoir des notifications `os.Signal`.
- Enregistrez le canal pour recevoir des notifications de signaux spécifiés à l'aide de `signal.Notify`.
- Créez une goroutine pour exécuter une réception bloquante de signaux.
- Affichez le signal reçu et avertissez le programme qu'il peut se terminer.
- Attendez le signal attendu puis quittez.

```sh
# Lorsque nous exécutons ce programme, il bloquera en attendant un
# signal. En appuyant sur `ctrl-C` (que le
# terminal affiche comme `^C`), nous pouvons envoyer un signal `SIGINT`,
# faisant en sorte que le programme affiche `interrupt` puis quitte.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

Voici le code complet ci-dessous :

```go
// Parfois, nous voudrions que nos programmes Go gèrent
// intelligemment les [signaux Unix](https://en.wikipedia.org/wiki/Unix_signal).
// Par exemple, nous pourrions vouloir qu'un serveur s'arrête proprement
// lorsqu'il reçoit un `SIGTERM`, ou qu'un outil de ligne de commande
// arrête de traiter l'entrée s'il reçoit un `SIGINT`.
// Voici comment gérer les signaux en Go avec des canaux.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// La notification de signaux Go fonctionne en envoyant des valeurs `os.Signal`
	// sur un canal. Nous allons créer un canal pour
	// recevoir ces notifications. Notez que ce canal
	// devrait être tamponné.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` enregistre le canal donné pour
	// recevoir des notifications des signaux spécifiés.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// Nous pourrions recevoir de `sigs` ici dans la fonction principale,
	// mais voyons comment cela pourrait également être
	// fait dans une goroutine séparée, pour démontrer
	// un scénario plus réaliste d'arrêt propre.
	done := make(chan bool, 1)

	go func() {
		// Cette goroutine exécute une réception bloquante de
		// signaux. Lorsqu'elle en reçoit un, elle l'affichera
		// puis avertira le programme qu'il peut se terminer.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// Le programme attendra ici jusqu'à ce qu'il obtienne le
	// signal attendu (comme indiqué par la goroutine
	// ci-dessus en envoyant une valeur sur `done`) puis il quittera.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
