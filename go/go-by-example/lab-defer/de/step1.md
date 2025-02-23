# Defer

In diesem Lab müssen Sie `defer` verwenden, um eine Datei zu erstellen, in sie zu schreiben und sie anschließend zu schließen, wenn Sie fertig sind.

- Die `createFile`-Funktion sollte eine Datei mit dem angegebenen Pfad erstellen und einen Zeiger auf die Datei zurückgeben.
- Die `writeFile`-Funktion sollte den String "data" in die Datei schreiben.
- Die `closeFile`-Funktion sollte die Datei schließen und auf Fehler prüfen.

```sh
# Wenn Sie das Programm ausführen, wird bestätigt, dass die Datei
# nach dem Schreiben geschlossen wird.
$ go run defer.go
creating
writing
closing
```

Hier ist der vollständige Code:

```go
// _Defer_ wird verwendet, um sicherzustellen, dass eine Funktionsaufruf
// später während der Ausführung eines Programms durchgeführt wird, normalerweise
// zu Zwecken der Bereinigung. `defer` wird häufig dort verwendet, wo z.B.
// `ensure` und `finally` in anderen Sprachen verwendet würden.

package main

import (
	"fmt"
	"os"
)

// Nehmen wir an, dass wir eine Datei erstellen möchten, in sie schreiben
// und sie dann schließen möchten, wenn wir fertig sind. Hier ist, wie wir
// das mit `defer` tun könnten.
func main() {

	// Unmittelbar nachdem wir ein Dateiobjekt mit
	// `createFile` erhalten haben, verzögern wir das Schließen
	// dieser Datei mit `closeFile`. Dies wird am Ende der umgebenden
	// Funktion (`main`) ausgeführt, nachdem
	// `writeFile` abgeschlossen ist.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err!= nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	// Es ist wichtig, auf Fehler zu prüfen, wenn eine Datei
	// geschlossen wird, auch in einer verzögerten Funktion.
	if err!= nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

```
