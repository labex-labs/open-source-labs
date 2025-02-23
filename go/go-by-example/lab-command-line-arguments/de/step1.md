# Befehlszeilenargumente

Das Programm druckt derzeit die übergebenen rohen Befehlszeilenargumente aus. Es muss jedoch so geändert werden, dass bestimmte Argumente anhand ihres Index ausgegeben werden.

- Grundkenntnisse von Golang
- Vertrautheit mit Befehlszeilenargumenten

```sh
# Um mit Befehlszeilenargumenten zu experimentieren, ist es am besten,
# zunächst eine Binärdatei mit `go build` zu erstellen.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Als nächstes betrachten wir die fortgeschrittene Befehlszeilenverarbeitung
# mit Flags.
```

Hier ist der vollständige Code:

```go
// [_Command-line arguments_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// sind eine übliche Möglichkeit, die Ausführung von Programmen zu parametrisieren.
// Beispielsweise verwendet `go run hello.go` die Argumente `run` und
// `hello.go` für das `go`-Programm.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` bietet den Zugang zu den rohen Befehlszeilenargumenten.
	// Beachten Sie, dass der erste Wert in diesem Slice der Pfad zum Programm ist
	// und `os.Args[1:]` die Argumente für das Programm enthält.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// Sie können einzelne Argumente mit normalem Indexzugriff abrufen.
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}

```
