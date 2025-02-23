# URL-Analyse

Das Labor erfordert die Analyse einer Beispiel-URL, die ein Schema, Authentifizierungsinformationen, Host, Port, Pfad, Abfrageparameter und Abfragefragment enthält. Die analysierte URL sollte verwendet werden, um die einzelnen Komponenten der URL zu extrahieren.

- Die Pakete `url` und `net` sollten importiert werden.
- Die Beispiel-URL sollte analysiert und auf Fehler überprüft werden.
- Das Schema, die Authentifizierungsinformationen, der Host, der Port, der Pfad, die Abfrageparameter und das Abfragefragment sollten aus der analysierten URL extrahiert werden.
- Die Funktion `SplitHostPort` sollte verwendet werden, um den Hostnamen und den Port aus dem Feld `Host` zu extrahieren.
- Die Funktion `ParseQuery` sollte verwendet werden, um die Abfrageparameter in eine Map zu analysieren.

```sh
# Wenn wir unser URL-Analyse-Programm ausführen, werden alle
# verschiedenen Teile angezeigt, die wir extrahiert haben.
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```

Hier ist der vollständige Code:

```go
// URLs bieten eine einheitliche Möglichkeit, Ressourcen zu lokalisieren (https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Hier ist, wie man URLs in Go analysiert.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// Wir werden diese Beispiel-URL analysieren, die ein
	// Schema, Authentifizierungsinformationen, Host, Port,
	// Pfad, Abfrageparameter und Abfragefragment enthält.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// Analysieren Sie die URL und stellen Sie sicher, dass keine
	// Fehler auftreten.
	u, err := url.Parse(s)
	if err!= nil {
		panic(err)
	}

	// Das Zugreifen auf das Schema ist unkompliziert.
	fmt.Println(u.Scheme)

	// `User` enthält alle Authentifizierungsinformationen; rufen
	// Sie `Username` und `Password` auf, um einzelne
	// Werte zu erhalten.
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// Das `Host` enthält sowohl den Hostnamen als auch den Port,
	// sofern vorhanden. Verwenden Sie `SplitHostPort`, um sie
	// zu extrahieren.
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// Hier extrahieren wir den `Pfad` und das Fragment nach
	// dem `#`.
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// Um Abfrageparameter im Format `k=v` als Zeichenfolge zu
	// erhalten, verwenden Sie `RawQuery`. Sie können auch
	// Abfrageparameter in eine Map analysieren. Die analysierten
	// Abfrageparametermaps gehen von Zeichenfolgen zu
	// Zeichenfolgen-Slices, so indexieren Sie in `[0]`, wenn
	// Sie nur den ersten Wert möchten.
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```
