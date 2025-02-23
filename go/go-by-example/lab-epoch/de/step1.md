# Epoche

Das Problem, das in diesem Labor gelöst werden soll, ist es, ein Golang-Programm zu schreiben, das die Anzahl der Sekunden, Millisekunden oder Nanosekunden seit der Unix-Epoche berechnen kann.

Um dieses Labor abzuschließen, musst du eine grundlegende Kenntnis von Golang und die folgenden Anforderungen haben:

- Vertrautheit mit dem `time`-Paket in Golang.
- Kenntnisse darüber, wie die `Unix`, `UnixMilli` und `UnixNano`-Funktionen im `time`-Paket verwendet werden.

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# Als nächstes betrachten wir eine andere zeitbezogene Aufgabe: Zeit
# Parsing und Formatierung.
```

Hier ist der vollständige Code:

```go
// Ein häufiges Anfordernis in Programmen ist es, die Anzahl
// der Sekunden, Millisekunden oder Nanosekunden seit der
// [Unix-Epoche](https://en.wikipedia.org/wiki/Unix_time) zu erhalten.
// Hier ist, wie man es in Go macht.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Verwende `time.Now` mit `Unix`, `UnixMilli` oder `UnixNano`
	// um die verstrichene Zeit seit der Unix-Epoche in Sekunden,
	// Millisekunden oder Nanosekunden zu erhalten.
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// Du kannst auch ganze Sekunden oder Nanosekunden seit der Epoche
	// in die entsprechende `time` umwandeln.
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}

```
