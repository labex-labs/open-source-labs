# Befehlszeilenflags

Implementieren Sie ein Golang-Programm, das Befehlszeilenflags auswertet und die ausgewerteten Optionen sowie alle nachfolgenden Positionsargumente ausgibt. Das Programm sollte die folgenden Flags unterstützen:

- `word`: Ein String-Flag mit dem Standardwert `"foo"`.
- `numb`: Ein Integer-Flag mit dem Standardwert `42`.
- `fork`: Ein boolescher Flag mit dem Standardwert `false`.
- `svar`: Ein String-Flag, das eine vorhandene Variable verwendet, die an anderer Stelle im Programm deklariert wurde.

- Das Programm sollte das `flag`-Paket verwenden, um Befehlszeilenflags zu analysieren.
- Das Programm sollte die ausgewerteten Optionen und alle nachfolgenden Positionsargumente ausgeben.
- Das Programm sollte die Flags `word`, `numb`, `fork` und `svar` wie oben beschrieben unterstützen.

```sh
# Um das Befehlszeilenflags-Programm zu testen, ist es
# am besten, es zunächst zu kompilieren und dann die
# resultierende Binärdatei direkt auszuführen.
$ go build command-line-flags.go

# Testen Sie das erstellte Programm, indem Sie zunächst
# allen Flags Werte zuweisen.
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Beachten Sie, dass die Flags automatisch ihre
# Standardwerte annehmen, wenn Sie sie weglassen.
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Nachfolgende Positionsargumente können nach allen
# Flags angegeben werden.
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Beachten Sie, dass das `flag`-Paket erfordert, dass
# alle Flags vor den Positionsargumenten erscheinen
# (ansonsten werden die Flags als Positionsargumente
# interpretiert).
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Verwenden Sie die Flags `-h` oder `--help`, um automatisch
# generierte Hilfetexte für das Befehlszeilenprogramm zu
# erhalten.
$./command-line-flags -h
Verwendung von./command-line-flags:
-fork=false: ein bool
-numb=42: eine int
-svar="bar": eine String-Variable
-word="foo": ein String

# Wenn Sie ein Flag angeben, das nicht dem `flag`-Paket
# angegeben wurde, wird das Programm eine Fehlermeldung
# ausgeben und den Hilfetext erneut anzeigen.
$./command-line-flags -wat
Flag angegeben, aber nicht definiert: -wat
Verwendung von./command-line-flags:
...
```

Der vollständige Code ist unten:

```go
// [_Befehlszeilenflags_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// sind eine häufige Möglichkeit, Optionen für
// Befehlszeilenprogramme anzugeben. Beispielsweise ist
// in `wc -l` das `-l` ein Befehlszeilenflag.

package main

// Go bietet ein `flag`-Paket, das die grundlegende
// Analyse von Befehlszeilenflags unterstützt. Wir werden
// dieses Paket verwenden, um unser Beispiel
// Befehlszeilenprogramm zu implementieren.
import (
	"flag"
	"fmt"
)

func main() {

	// Grundlegende Flagdeklarationen sind für String-,
	// Integer- und boolesche Optionen verfügbar. Hier
	// deklarieren wir ein String-Flag `word` mit dem
	// Standardwert `"foo"` und einer kurzen Beschreibung.
	// Diese `flag.String`-Funktion gibt einen
	// String-Zeiger zurück (nicht einen String-Wert);
	// wir werden sehen, wie wir diesen Zeiger unten
	// verwenden.
	wordPtr := flag.String("word", "foo", "ein String")

	// Dies deklariert die Flags `numb` und `fork` mit einem
	// ähnlichen Ansatz wie das `word`-Flag.
	numbPtr := flag.Int("numb", 42, "eine int")
	forkPtr := flag.Bool("fork", false, "ein bool")

	// Es ist auch möglich, eine Option zu deklarieren, die
	// eine vorhandene Variable verwendet, die an anderer
	// Stelle im Programm deklariert wurde. Beachten Sie,
	// dass wir einen Zeiger auf die Flagdeklarationsfunktion
	// übergeben müssen.
	var svar string
	flag.StringVar(&svar, "svar", "bar", "eine String-Variable")

	// Nachdem alle Flags deklariert sind, rufen Sie
	// `flag.Parse()` auf, um die Befehlszeilenanalyse
	// auszuführen.
	flag.Parse()

	// Hier werden wir einfach die ausgewerteten Optionen
	// und alle nachfolgenden Positionsargumente ausgeben.
	// Beachten Sie, dass wir die Pointer mit z.B. `*wordPtr`
	// dereferenzieren müssen, um die tatsächlichen
	// Optionenwerte zu erhalten.
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}

```
