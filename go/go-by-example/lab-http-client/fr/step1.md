# Client HTTP

Vous êtes requis d'écrire un programme qui envoie une requête HTTP GET à un serveur et imprime le statut de la réponse HTTP et les 5 premières lignes du corps de la réponse.

- Le programme doit utiliser le package `net/http` pour émettre une requête HTTP GET.
- Le programme doit imprimer le statut de la réponse HTTP.
- Le programme doit imprimer les 5 premières lignes du corps de la réponse.
- Le programme doit gérer les erreurs de manière appropriée.

```sh
$ go run http-clients.go
Statut de la réponse : 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

Voici le code complet ci-dessous :

```go
// La bibliothèque standard Go offre un excellent support
// pour les clients et les serveurs HTTP dans le package
// `net/http`. Dans cet exemple, nous allons l'utiliser pour
// émettre des requêtes HTTP simples.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Émettez une requête HTTP GET à un serveur. `http.Get` est
	// un raccourci pratique pour créer un objet `http.Client`
	// et appeler sa méthode `Get` ; il utilise l'objet
	// `http.DefaultClient` qui a des paramètres par défaut
	// utiles.
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Imprimez le statut de la réponse HTTP.
	fmt.Println("Statut de la réponse :", resp.Status)

	// Imprimez les 5 premières lignes du corps de la réponse.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
