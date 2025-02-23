# Verzeichnisse

Erstelle ein Go-Programm, das ein neues Unterverzeichnis im aktuellen Arbeitsverzeichnis erstellt, eine Verzeichnishierarchie einschließlich der Übergeordneten erstellt, die Verzeichnisinhalte auflistet, das aktuelle Arbeitsverzeichnis ändert und ein Verzeichnis rekursiv durchsucht.

- Erstelle ein neues Unterverzeichnis im aktuellen Arbeitsverzeichnis.
- Wenn du temporäre Verzeichnisse erstellst, ist es eine gute Praxis, deren Entfernung mit `defer` zu planen. `os.RemoveAll` wird einen ganzen Verzeichnistbaum löschen (ähnlich wie `rm -rf`).
- Erstelle eine Verzeichnishierarchie einschließlich der Übergeordneten mit `MkdirAll`. Dies ist ähnlich dem Befehlszeilenbefehl `mkdir -p`.
- `ReadDir` listet die Verzeichnisinhalte auf und gibt eine Liste von `os.DirEntry`-Objekten zurück.
- `Chdir` ermöglicht es uns, das aktuelle Arbeitsverzeichnis zu ändern, ähnlich wie `cd`.
- Besuche ein Verzeichnis rekursiv, einschließlich aller seiner Unterverzeichnisse. `Walk` akzeptiert eine Callback-Funktion, um jedes besuchte Verzeichnis oder Datei zu verarbeiten.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

Hier ist der vollständige Code:

```go
// Go hat mehrere nützliche Funktionen zum Umgang mit
// *Verzeichnissen* im Dateisystem.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Erstelle ein neues Unterverzeichnis im aktuellen Arbeits
	// verzeichnis.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// Wenn du temporäre Verzeichnisse erstellst, ist es eine gute
	// Praxis, deren Entfernung mit `defer` zu planen. `os.RemoveAll`
	// wird einen ganzen Verzeichnistbaum löschen (ähnlich wie
	// `rm -rf`).
	defer os.RemoveAll("subdir")

	// Hilfsfunktion, um eine neue leere Datei zu erstellen.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// Wir können eine Verzeichnishierarchie einschließlich der
	// Übergeordneten mit `MkdirAll` erstellen. Dies ist ähnlich dem
	// Befehlszeilenbefehl `mkdir -p`.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` listet die Verzeichnisinhalte auf und gibt eine
	// Liste von `os.DirEntry`-Objekten zurück.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` ermöglicht es uns, das aktuelle Arbeitsverzeichnis zu
	// ändern, ähnlich wie `cd`.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// Jetzt sehen wir die Inhalte von `subdir/parent/child`, wenn
	// wir das *aktuelle* Verzeichnis auflisten.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` zurück zu unserem Ausgangspunkt.
	err = os.Chdir("../../..")
	check(err)

	// Wir können auch ein Verzeichnis *rekursiv* durchsuchen,
	// einschließlich aller seiner Unterverzeichnisse. `Walk` akzeptiert
	// eine Callback-Funktion, um jedes besuchte Verzeichnis oder
	// Datei zu verarbeiten.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` wird für jede gefundene Datei oder jedes Verzeichnis, das
// rekursiv von `filepath.Walk` gefunden wird, aufgerufen.
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```
