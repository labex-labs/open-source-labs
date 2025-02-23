# Befehlszeilen-Unterbefehle

Es wird ein Programm erstellt, das zwei Unterbefehle unterstützt, `foo` und `bar`, jeder mit seiner eigenen Flaggegruppe. Der `foo`-Unterbefehl sollte zwei Flags haben, `enable` und `name`, während der `bar`-Unterbefehl ein Flag `level` haben sollte.

- Das Programm sollte das `flag`-Paket verwenden, um Flags zu definieren und zu analysieren.
- Der `foo`-Unterbefehl sollte zwei Flags haben, `enable` und `name`, beide vom Typ string.
- Der `bar`-Unterbefehl sollte ein Flag `level` vom Typ int haben.
- Das Programm sollte eine Fehlermeldung ausgeben, wenn ein ungültiger Unterbefehl angegeben wird.
- Das Programm sollte die Werte der Flags für den aufgerufenen Unterbefehl ausgeben.

```sh
$ go build command-line-subcommands.go

# Rufen Sie zunächst den foo-Unterbefehl auf.
$./command-line-subcommands foo -enable -name=joe a1 a2
subcommand 'foo'
enable: true
name: joe
tail: [a1 a2]

# Versuchen Sie jetzt bar.
$./command-line-subcommands bar -level 8 a1
subcommand 'bar'
level: 8
tail: [a1]

# Aber bar akzeptiert die Flags von foo nicht.
$./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
-level int
level

# Als nächstes betrachten wir Umgebungsvariablen, eine weitere häufige
# Möglichkeit, Programme zu parametrisieren.
```

Hier ist der vollständige Code:

```go
// Einige Befehlszeilentools wie das `go`-Tool oder `git`
// haben viele *Unterbefehle*, jeder mit seiner eigenen
// Flaggegruppe. Beispielsweise sind `go build` und `go get`
// zwei verschiedene Unterbefehle des `go`-Tools.
// Das `flag`-Paket ermöglicht es uns, einfache Unterbefehle
// mit eigenen Flags leicht zu definieren.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// Wir deklarieren einen Unterbefehl mit der `NewFlagSet`-
	// Funktion und definieren anschließend neue Flags, die
	// speziell für diesen Unterbefehl gelten.
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// Für einen anderen Unterbefehl können wir unterschiedliche
	// unterstützte Flags definieren.
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// Der Unterbefehl wird als erstes Argument erwartet,
	// das an das Programm übergeben wird.
	if len(os.Args) < 2 {
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}

	// Überprüfen, welcher Unterbefehl aufgerufen wird.
	switch os.Args[1] {

	// Für jeden Unterbefehl analysieren wir seine eigenen Flags
	// und haben Zugang zu den nachfolgenden positionellen Argumenten.
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}
}

```
