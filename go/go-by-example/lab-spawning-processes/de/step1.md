# Prozesse starten

Das Lab erfordert die Implementierung eines Go-Programms, das externe Prozesse startet und deren Ausgabe sammelt.

- Das Programm sollte in der Lage sein, externe Prozesse zu starten.
- Das Programm sollte in der Lage sein, die Ausgabe der externen Prozesse zu sammeln.
- Das Programm sollte Fehler behandeln, die während der Ausführung der externen Prozesse auftreten können.

```sh
# Die gestarteten Programme geben die gleiche Ausgabe zurück,
# als hätten wir sie direkt von der Befehlszeile ausgeführt.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date hat keinen `-x`-Flag, daher wird es mit einer
# Fehlermeldung und einem nicht-nullen Rückgabecode beenden.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

Hier ist der vollständige Code:

```go
// Manchmal müssen unsere Go-Programme andere, nicht-Go-
// Prozesse starten.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// Wir beginnen mit einem einfachen Befehl, der keine
	// Argumente oder Eingabe erwartet und einfach etwas
	// auf die Standardausgabe ausgibt. Die `exec.Command`-
	// Hilfsmethode erstellt ein Objekt, um diesen externen
	// Prozess zu repräsentieren.
	dateCmd := exec.Command("date")

	// Die `Output`-Methode führt den Befehl aus, wartet,
	// bis er beendet ist und sammelt seine Standardausgabe.
	// Wenn keine Fehler auftraten, enthält `dateOut` die
	// Bytes mit den Datumsinformationen.
	dateOut, err := dateCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` und andere Methoden von `Command` werden
	// `*exec.Error` zurückgeben, wenn es ein Problem bei
	// der Ausführung des Befehls gab (z.B. falscher Pfad),
	// und `*exec.ExitError`, wenn der Befehl ausgeführt
	// wurde, aber mit einem nicht-nullen Rückgabecode
	// beendet wurde.
	_, err = exec.Command("date", "-x").Output()
	if err!= nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("failed executing:", err)
		case *exec.ExitError:
			fmt.Println("command exit rc =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// Als nächstes betrachten wir einen etwas komplexeren
	// Fall, in dem wir Daten an den externen Prozess über
	// seine `stdin` senden und die Ergebnisse von seiner
	// `stdout` sammeln.
	grepCmd := exec.Command("grep", "hello")

	// Hier greifen wir explizit auf die Eingabe-/Ausgabepipen
	// zu, starten den Prozess, schreiben einige Eingabe
	// hinein, lesen die resultierende Ausgabe und warten
	// schließlich auf das Beenden des Prozesses.
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// Wir haben in obigem Beispiel die Fehlerprüfungen
	// weggelassen, aber Sie könnten das übliche
	// `if err!= nil`-Muster für alle verwenden. Wir
	// sammeln auch nur die `StdoutPipe`-Ergebnisse, aber
	// Sie könnten die `StderrPipe` genauso sammeln.
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// Beachten Sie, dass wir beim Start von Befehlen ein
	// explizit aufgetrenntes Befehls- und Argumentarray
	// angeben müssen, im Gegensatz dazu, dass wir nur
	// eine einzelne Befehlszeilenzeichenfolge übergeben
	// können. Wenn Sie einen vollständigen Befehl mit einer
	// Zeichenfolge starten möchten, können Sie die `-c`-
	// Option von `bash` verwenden:
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}

```
