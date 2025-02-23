# Umgebungsvariablen

In diesem Lab müssen Sie Umgebungsvariablen setzen, abrufen und auflisten.

- Verwenden Sie `os.Setenv`, um ein Schlüssel-Wert-Paar zu setzen.
- Verwenden Sie `os.Getenv`, um einen Wert für einen Schlüssel abzurufen.
- Verwenden Sie `os.Environ`, um alle Schlüssel-Wert-Paare in der Umgebung aufzulisten.
- Verwenden Sie `strings.SplitN`, um den Schlüssel und den Wert aufzuteilen.

```sh
# Wenn wir das Programm ausführen, sehen wir, dass wir den Wert
# für `FOO` erhalten, den wir im Programm gesetzt haben, aber dass
# `BAR` leer ist.
$ go run environment-variables.go
FOO: 1
BAR:

# Die Liste der Schlüssel in der Umgebung hängt von Ihrem
# bestimmten Computer ab.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Wenn wir `BAR` zunächst in der Umgebung setzen, erhält das
# ausgeführte Programm diesen Wert.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

Das vollständige Codebeispiel finden Sie hier unten:

```go
// [Umgebungsvariablen](https://en.wikipedia.org/wiki/Environment_variable)
// sind ein universelles Mechanismus, um [Konfigurationsinformationen
// an Unix-Programme zu übermitteln](https://www.12factor.net/config).
// Schauen wir uns an, wie man Umgebungsvariablen setzt, abruft und auflistet.

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// Um ein Schlüssel-Wert-Paar zu setzen, verwenden Sie `os.Setenv`. Um einen
	// Wert für einen Schlüssel abzurufen, verwenden Sie `os.Getenv`. Dies wird
	// einen leeren String zurückgeben, wenn der Schlüssel in der Umgebung
	// nicht vorhanden ist.
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// Verwenden Sie `os.Environ`, um alle Schlüssel-Wert-Paare in der
	// Umgebung aufzulisten. Dies gibt ein Slice von Strings im Format
	// `KEY=value` zurück. Sie können sie mit `strings.SplitN` aufteilen, um
	// den Schlüssel und den Wert zu erhalten. Hier drucken wir alle Schlüssel.
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}

```
