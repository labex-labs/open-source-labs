# Zeilenfilter

Das Problem, das in diesem Lab gelöst werden soll, ist es, ein Go-Programm zu schreiben, das Eingabetexte von der Standardeingabe (stdin) liest, alle Buchstaben im Text in Großbuchstaben umwandelt und dann den modifizierten Text auf die Standardausgabe (stdout) ausgibt.

- Das Programm muss Eingabetexte von der Standardeingabe lesen.
- Das Programm muss alle Buchstaben im Eingabetext in Großbuchstaben umwandeln.
- Das Programm muss den modifizierten Text auf die Standardausgabe ausgeben.

```sh
# Um unseren Zeilenfilter zu testen, erstellen wir zunächst eine Datei
# mit einigen Kleinbuchstabenzeilen.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Anschließend verwenden wir den Zeilenfilter, um Großbuchstabenzeilen zu erhalten.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

Hier ist der vollständige Code:

```go
// Ein _Zeilenfilter_ ist ein üblicher Programmtyp, der Eingaben
// von der Standardeingabe liest, verarbeitet und dann einige
// abgeleitete Ergebnisse auf die Standardausgabe ausgibt. `grep` und `sed`
// sind häufige Zeilenfilter.

// Hier ist ein Beispiel für einen Zeilenfilter in Go, der eine
// großgeschriebene Version des gesamten Eingabetexts ausgibt.
// Sie können dieses Muster verwenden, um Ihre eigenen Go-Zeilenfilter zu schreiben.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// Das Umhüllen der unbufferten `os.Stdin` mit einem gepufferten
	// Scanner gibt uns eine bequeme `Scan`-Methode, die den Scanner
	// zum nächsten Token vorwärts bewegt; was in der Standardimplementierung
	// der nächste Zeile ist.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` gibt das aktuelle Token, hier die nächste Zeile,
		// aus der Eingabe zurück.
		ucl := strings.ToUpper(scanner.Text())

		// Schreibt die großgeschriebene Zeile aus.
		fmt.Println(ucl)
	}

	// Überprüft auf Fehler während `Scan`. Dateiende wird
	// erwartet und von `Scan` als Fehler nicht gemeldet.
	if err := scanner.Err(); err!= nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
