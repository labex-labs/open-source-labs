# Dateipfade

In diesem Lab müssen Sie das Paket `filepath` verwenden, um verschiedene Operationen an Dateipfaden auszuführen, wie z. B. das portables Konstruieren von Pfaden, das Aufteilen eines Pfads in Verzeichnis- und Dateikomponenten, das Prüfen, ob ein Pfad absolut ist, das Finden der Dateierweiterung und das Finden eines relativen Pfads zwischen zwei Pfaden.

- Verwenden Sie `Join`, um Pfade auf eine portable Weise zu konstruieren.
- Verwenden Sie `Dir` und `Base`, um einen Pfad in Verzeichnis- und Dateikomponenten aufzuteilen.
- Verwenden Sie `IsAbs`, um zu prüfen, ob ein Pfad absolut ist.
- Verwenden Sie `Ext`, um die Dateierweiterung zu finden.
- Verwenden Sie `TrimSuffix`, um die Dateierweiterung aus einem Dateinamen zu entfernen.
- Verwenden Sie `Rel`, um einen relativen Pfad zwischen zwei Pfaden zu finden.

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

Hier ist der vollständige Code:

```go
// Das Paket `filepath` bietet Funktionen, um *Dateipfade*
// auf eine Art und Weise zu analysieren und zu konstruieren,
// die zwischen Betriebssystemen portabel ist; `dir/file`
// unter Linux im Vergleich zu `dir\file` unter Windows.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` sollte verwendet werden, um Pfade auf eine
	// portable Weise zu konstruieren. Es nimmt eine beliebige
	// Anzahl von Argumenten entgegen und konstruiert daraus
	// einen hierarchischen Pfad.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// Sie sollten immer `Join` verwenden, anstatt `/` oder `\`
	// manuell zu verketten. Neben der Portabilität normalisiert
	// `Join` auch Pfade, indem es überflüssige Trennzeichen und
	// Verzeichniswechsel entfernt.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` und `Base` können verwendet werden, um einen Pfad
	// in das Verzeichnis und die Datei aufzuteilen. Alternativ
	// gibt `Split` beide in einem Aufruf zurück.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// Wir können prüfen, ob ein Pfad absolut ist.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// Einige Dateinamen haben eine Dateierweiterung nach einem Punkt.
	// Wir können die Dateierweiterung aus solchen Namen mit `Ext`
	// extrahieren.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// Um den Dateinamen ohne die Dateierweiterung zu erhalten,
	// verwenden Sie `strings.TrimSuffix`.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` findet einen relativen Pfad zwischen einer *Basis*
	// und einem *Ziel*. Es gibt einen Fehler zurück, wenn das
	// Ziel nicht relativ zur Basis gemacht werden kann.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)
}

```
