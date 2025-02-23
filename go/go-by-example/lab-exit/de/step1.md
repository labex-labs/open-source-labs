# Exit

Das Problem, das in diesem Labor gelöst werden soll, ist es, ein Go-Programm mit einem bestimmten Statuscode zu beenden, indem die `os.Exit`-Funktion verwendet wird.

Um dieses Labor abzuschließen, sollten Sie über ein grundlegendes Verständnis von Go-Programmierung und dem `os`-Paket verfügen.

```sh
# Wenn Sie `exit.go` mit `go run` ausführen, wird die Beendung
# von `go` erkannt und ausgegeben.
$ go run exit.go
exit status 3

# Indem Sie ein Binärprogramm erstellen und ausführen, können Sie
# den Status im Terminal sehen.
$ go build exit.go
$./exit
$ echo $?
3

# Beachten Sie, dass das `!` aus unserem Programm nie ausgegeben wurde.
```

Hier ist der vollständige Code:

```go
// Verwenden Sie `os.Exit`, um sofort mit einem bestimmten
// Status zu beenden.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `defer`-Anweisungen werden bei Verwendung von `os.Exit` _nicht_
	// ausgeführt, daher wird diese `fmt.Println`-Anweisung nie aufgerufen.
	defer fmt.Println("!")

	// Beenden Sie mit Status 3.
	os.Exit(3)
}

// Beachten Sie, dass im Gegensatz zu z.B. C Go nicht einen ganzzahligen
// Rückgabewert von `main` verwendet, um den Beendungsstatus anzugeben. Wenn
// Sie mit einem nicht-null-Status beenden möchten, sollten Sie `os.Exit` verwenden.

```
