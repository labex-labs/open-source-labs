# Serveur HTTP

Vous êtes requis d'écrire un serveur HTTP simple capable de gérer deux itinéraires : `/hello` et `/headers`. La route `/hello` devrait renvoyer une réponse simple "hello", tandis que la route `/headers` devrait renvoyer tous les en-têtes de requête HTTP.

- Le serveur devrait utiliser le package `net/http`.
- La route `/hello` devrait renvoyer une réponse "hello".
- La route `/headers` devrait renvoyer tous les en-têtes de requête HTTP.
- Le serveur devrait écouter sur le port `8090`.

```sh
# Exécutez le serveur en arrière-plan.
$ go run http-servers.go &

# Accédez à la route `/hello`.
$ curl localhost:8090/hello
hello
```

Voici le code complet ci-dessous :

```go
// Écrire un serveur HTTP de base est facile en utilisant le
// package `net/http`.
package main

import (
	"fmt"
	"net/http"
)

// Un concept fondamental dans les serveurs `net/http` est
// les *handlers*. Un handler est un objet implémentant l'interface
// `http.Handler`. Une manière commune d'écrire
// un handler est d'utiliser l'adaptateur `http.HandlerFunc`
// sur des fonctions avec la signature appropriée.
func hello(w http.ResponseWriter, req *http.Request) {

	// Les fonctions servant de handlers prennent un
	// `http.ResponseWriter` et un `http.Request` en
	// arguments. Le writer de réponse est utilisé pour remplir la
	// réponse HTTP. Ici, notre réponse simple est juste
	// "hello\n".
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// Ce handler fait quelque chose un peu plus
	// sophistiqué en lisant tous les en-têtes de requête HTTP
	// et en les renvoyant dans le corps de la réponse.
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// Nous enregistrons nos handlers sur les itinéraires du serveur en utilisant la
	// fonction pratique `http.HandleFunc`. Elle configure
	// le *routeur par défaut* dans le package `net/http` et
	// prend une fonction en argument.
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// Enfin, nous appelons `ListenAndServe` avec le port
	// et un handler. `nil` lui indique d'utiliser le routeur par défaut
	// que nous venons de configurer.
	http.ListenAndServe(":8090", nil)
}

```
