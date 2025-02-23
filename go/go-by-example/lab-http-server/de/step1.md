# HTTP-Server

Sie müssen einen einfachen HTTP-Server schreiben, der zwei Routen verarbeiten kann: `/hello` und `/headers`. Die `/hello`-Route sollte eine einfache "hello"-Antwort zurückgeben, während die `/headers`-Route alle HTTP-Anfrageheader zurückgeben sollte.

- Der Server sollte das Paket `net/http` verwenden.
- Die `/hello`-Route sollte eine "hello"-Antwort zurückgeben.
- Die `/headers`-Route sollte alle HTTP-Anfrageheader zurückgeben.
- Der Server sollte auf Port `8090` lauschen.

```sh
# Führen Sie den Server im Hintergrund aus.
$ go run http-servers.go &

# Greifen Sie auf die `/hello`-Route zu.
$ curl localhost:8090/hello
hello
```

Hier ist der vollständige Code:

```go
// Ein einfacher HTTP-Server lässt sich leicht mit dem
// Paket `net/http` schreiben.
package main

import (
	"fmt"
	"net/http"
)

// Ein grundlegendes Konzept bei `net/http`-Servern ist
// *Handler*. Ein Handler ist ein Objekt, das das
// `http.Handler`-Interface implementiert. Ein häufiger
// Weg, einen Handler zu schreiben, besteht darin, die
// `http.HandlerFunc`-Adapter auf Funktionen mit der
// passenden Signatur zu verwenden.
func hello(w http.ResponseWriter, req *http.Request) {

	// Als Handler dienende Funktionen erhalten einen
	// `http.ResponseWriter` und einen `http.Request` als
	// Argumente. Der Antwortschreiber wird verwendet, um
	// die HTTP-Antwort auszufüllen. Unsere einfache
	// Antwort ist hier einfach "hello\n".
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// Dieser Handler macht etwas etwas Komplexeres, indem
	// er alle HTTP-Anfrageheader liest und sie in den
	// Antwortkörper zurückgibt.
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// Wir registrieren unsere Handler auf den Serverrouten
	// mit der Hilfsfunktion `http.HandleFunc`. Sie
	// konfiguriert den *Standardrouter* im Paket
	// `net/http` und nimmt eine Funktion als Argument.
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// Schließlich rufen wir `ListenAndServe` mit dem Port
	// und einem Handler auf. `nil` veranlasst es, den
	// Standardrouter zu verwenden, den wir gerade
	// eingerichtet haben.
	http.ListenAndServe(":8090", nil)
}

```
