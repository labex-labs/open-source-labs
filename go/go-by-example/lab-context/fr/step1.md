# Context

La fonction `hello` simule un certain travail effectué par le serveur en attendant quelques secondes avant d'envoyer une réponse au client. Pendant le travail, surveillez le canal `Done()` du contexte pour un signal indiquant que nous devrions annuler le travail et retourner le plus rapidement possible.

- Version de Golang 1.13 ou ultérieure.

```sh
# Lancez le serveur en arrière-plan.
$ go run context-in-http-servers.go &

# Simulez une requête client à `/hello`, appuyez sur
# Ctrl+C peu de temps après le lancement pour signaler
# l'annulation.
$ curl localhost:8090/hello
serveur: hello handler démarré
^C
serveur: contexte annulé
serveur: hello handler terminé
```

Voici le code complet ci-dessous :

```go
// Dans l'exemple précédent, nous avons vu comment configurer un serveur
// [HTTP simple](http-servers). Les serveurs HTTP sont utiles pour
// démontrer l'utilisation de `context.Context` pour
// contrôler l'annulation. Un `Context` transporte des délais,
// des signaux d'annulation et d'autres valeurs liées à la requête
// entre les limites d'API et les goroutines.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// Un `context.Context` est créé pour chaque requête par
	// la machinerie `net/http`, et est disponible via
	// la méthode `Context()`.
	ctx := req.Context()
	fmt.Println("serveur: hello handler démarré")
	defer fmt.Println("serveur: hello handler terminé")

	// Attendez quelques secondes avant d'envoyer une réponse au
	// client. Cela pourrait simuler un certain travail effectué par le
	// serveur. Pendant le travail, surveillez le canal `Done()` du
	// contexte pour un signal indiquant que nous devrions annuler
	// le travail et retourner le plus rapidement possible.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// La méthode `Err()` du contexte renvoie une erreur
		// qui explique pourquoi le canal `Done()` a été
		// fermé.
		err := ctx.Err()
		fmt.Println("serveur:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// Comme précédemment, nous enregistrons notre gestionnaire sur
	// la route "/hello", et commençons à servir.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
