# HTTP-Client

Sie müssen ein Programm schreiben, das einen HTTP GET-Anfrage an einen Server sendet und den HTTP-Antwortstatus sowie die ersten 5 Zeilen des Antwortkörpers ausgibt.

- Das Programm sollte das `net/http`-Paket verwenden, um eine HTTP GET-Anfrage zu senden.
- Das Programm sollte den HTTP-Antwortstatus ausgeben.
- Das Programm sollte die ersten 5 Zeilen des Antwortkörpers ausgeben.
- Das Programm sollte Fehler 优雅地 behandeln.

```sh
$ go run http-clients.go
Antwortstatus: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

Hier ist der vollständige Code:

```go
// Die Go-Standardbibliothek bietet ausgezeichnete Unterstützung
// für HTTP-Clients und -Server im `net/http`-
// Paket. In diesem Beispiel verwenden wir es, um einfache
// HTTP-Anfragen zu senden.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Sende eine HTTP GET-Anfrage an einen Server. `http.Get` ist ein
	// bequemer Kurzweg um ein `http.Client`-
	// Objekt zu erstellen und seine `Get`-Methode aufzurufen; es verwendet das
	// `http.DefaultClient`-Objekt, das nützliche Standard-
	// Einstellungen hat.
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Gib den HTTP-Antwortstatus aus.
	fmt.Println("Antwortstatus:", resp.Status)

	// Gib die ersten 5 Zeilen des Antwortkörpers aus.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
