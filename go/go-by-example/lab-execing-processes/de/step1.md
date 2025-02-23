# Prozesse ausführen

Das Problem besteht darin, den aktuellen Go-Prozess durch einen anderen Prozess, wie beispielsweise einen Nicht-Go-Prozess, zu ersetzen.

- Go-Programmiersprache
- Grundkenntnisse der Go-`exec`-Funktion
- Vertrautheit mit Umgebungsvariablen

```sh
# Wenn wir unser Programm ausführen, wird es durch `ls` ersetzt.
$ go run execing-processes.go
gesamt 16
drwxr-xr-x 4 mark 136B Okt 3 16:29.
drwxr-xr-x 91 mark 3,0K Okt 3 12:50..
-rw-r--r-- 1 mark 1,3K Okt 3 16:28 execing-processes.go

# Beachten Sie, dass Go keine klassische Unix-`fork`-Funktion bietet.
# Normalerweise ist dies jedoch kein Problem, da das Starten von Goroutinen,
# das Erzeugen von Prozessen und das Ausführen von Prozessen die meisten
# Anwendungsfälle für `fork` abdecken.
```

Das vollständige Codebeispiel finden Sie hier unten:

```go
// Im vorherigen Beispiel haben wir uns die [Erzeugung externer Prozesse](spawning-processes) angeschaut.
// Wir tun dies, wenn wir einen externen Prozess benötigen, auf den ein laufender Go-Prozess zugreifen kann.
// Manchmal möchten wir einfach den aktuellen Go-Prozess vollständig durch einen anderen (eventuell Nicht-Go-) ersetzen.
// Dazu verwenden wir die Go-Implementierung der klassischen <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>-Funktion.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// Für unser Beispiel werden wir `ls` ausführen. Go erfordert einen absoluten Pfad zur Binärdatei, die wir ausführen möchten,
	// also verwenden wir `exec.LookPath`, um ihn zu finden (wahrscheinlich `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr!= nil {
		panic(lookErr)
	}

	// `Exec` erfordert Argumente in Form eines Slices (im Gegensatz zu einem großen String).
	// Wir werden `ls` einige übliche Argumente geben. Beachten Sie, dass das erste Argument der Programmname sein sollte.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` benötigt auch eine Reihe von [Umgebungsvariablen](environment-variables), die verwendet werden sollen.
	// Hier geben wir einfach unsere aktuelle Umgebung an.
	env := os.Environ()

	// Hier erfolgt der tatsächliche `syscall.Exec`-Aufruf. Wenn dieser Aufruf erfolgreich ist, endet die Ausführung unseres Prozesses hier und wird durch den `/bin/ls -a -l -h`-Prozess ersetzt.
	// Wenn ein Fehler auftritt, erhalten wir einen Rückgabewert.
	execErr := syscall.Exec(binary, args, env)
	if execErr!= nil {
		panic(execErr)
	}
}

```
