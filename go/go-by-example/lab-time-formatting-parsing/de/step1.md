# Zeitformatierung und -parsing

Das Problem besteht darin, die Zeit in Golang mit den bereitgestellten Layouts zu formatieren und zu parsen.

- Verwenden Sie das `time`-Paket, um die Zeit zu formatieren und zu parsen.
- Verwenden Sie das `time.RFC3339`-Layout, um die Zeit zu formatieren und zu parsen.
- Verwenden Sie die Referenzeit `Mon Jan 2 15:04:05 MST 2006`, um das Muster anzuzeigen, mit dem eine gegebene Zeit/Zeichenfolge formatiert/parsiert wird.
- Verwenden Sie die `Parse`-Funktion, um die Zeit zu parsen.
- Verwenden Sie die `Format`-Funktion, um die Zeit zu formatieren.
- Verwenden Sie die `fmt.Println`-Funktion, um die formattierte Zeit auszugeben.
- Verwenden Sie die `fmt.Printf`-Funktion, um die formattierte Zeit mit extrahierten Komponenten auszugeben.

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```

Hier ist der vollständige Code:

```go
// Go unterstützt die Zeitformatierung und -parsing über
// musterbasierte Layouts.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Hier ist ein einfaches Beispiel für die Formatierung einer Zeit
	// gemäß RFC3339, unter Verwendung der entsprechenden Layout-
	// Konstante.
	t := time.Now()
	p(t.Format(time.RFC3339))

	// Die Zeitparsing verwendet die gleichen Layoutwerte wie `Format`.
	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	// `Format` und `Parse` verwenden musterbasierte Layouts. Normalerweise
	// verwenden Sie eine Konstante aus `time` für diese Layouts, aber
	// Sie können auch benutzerdefinierte Layouts angeben. Layouts müssen die
	// Referenzeit `Mon Jan 2 15:04:05 MST 2006` verwenden, um das
	// Muster anzuzeigen, mit dem eine gegebene Zeit/Zeichenfolge formatiert/parsiert wird.
	// Die Beispielzeit muss genau so aussehen wie angegeben: das Jahr 2006,
	// 15 für die Stunde, Montag für den Wochentag usw.
	p(t.Format("3:04PM"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))
	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// Für rein numerische Darstellungen können Sie auch
	// standardmäßige Zeichenfolgformatierung mit den extrahierten
	// Komponenten des Zeitwerts verwenden.
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// `Parse` wird einen Fehler bei fehlerhafter Eingabe zurückgeben
	// und erklärt das Parsingproblem.
	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}

```
