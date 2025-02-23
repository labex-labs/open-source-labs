# Temporäre Dateien und Verzeichnisse

In diesem Lab müssen Sie temporäre Dateien und Verzeichnisse in Go erstellen.

- Verwenden Sie `os.CreateTemp`, um eine temporäre Datei zu erstellen.
- Verwenden Sie `os.MkdirTemp`, um ein temporäres Verzeichnis zu erstellen.
- Verwenden Sie `os.RemoveAll`, um das temporäre Verzeichnis zu entfernen.
- Verwenden Sie `os.WriteFile`, um Daten in eine Datei zu schreiben.

```sh
$ go run temporary-files-and-directories.go
Temp file name: /tmp/sample610887201
Temp dir name: /tmp/sampledir898854668
```

Hier ist der vollständige Code:

```go
// Während der gesamten Programmausführung möchten wir oft Daten erstellen,
// die nach dem Beenden des Programms nicht mehr benötigt werden.
// *Temporäre Dateien und Verzeichnisse* sind für diesen Zweck nützlich,
// da sie das Dateisystem im Laufe der Zeit nicht verschmutzen.

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

	// Der einfachste Weg, eine temporäre Datei zu erstellen, ist es,
	// `os.CreateTemp` aufzurufen. Es erstellt eine Datei *und*
	// öffnet sie zum Lesen und Schreiben. Wir geben `""` als ersten
	// Argument an, so dass `os.CreateTemp` die Datei an der Standard-
	// position für unseren Betriebssystem erstellt.
	f, err := os.CreateTemp("", "sample")
	check(err)

	// Zeigen Sie den Namen der temporären Datei an. Auf Unix-basierten
	// Betriebssystemen wird das Verzeichnis wahrscheinlich `/tmp` sein.
	// Der Dateiname beginnt mit dem Präfix, das als zweites Argument
	// an `os.CreateTemp` gegeben wurde, und der Rest wird automatisch
	// gewählt, um sicherzustellen, dass konkurrierende Aufrufe immer
	// unterschiedliche Dateinamen erzeugen.
	fmt.Println("Temp file name:", f.Name())

	// Bereinigen Sie die Datei, nachdem wir fertig sind. Der Betriebssystem
	// wird wahrscheinlich die temporären Dateien nach einiger Zeit
	// automatisch bereinigen, aber es ist eine gute Praxis, dies
	// explizit zu tun.
	defer os.Remove(f.Name())

	// Wir können einige Daten in die Datei schreiben.
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// Wenn wir viele temporäre Dateien schreiben möchten, können wir
	// lieber ein temporäres *Verzeichnis* erstellen. Die Argumente von
	// `os.MkdirTemp` sind die gleichen wie die von `CreateTemp`, aber
	// es wird ein Verzeichnis*name* zurückgegeben, statt einer geöffneten
	// Datei.
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Temp dir name:", dname)

	defer os.RemoveAll(dname)

	// Jetzt können wir temporäre Dateinamen synthetisieren, indem
	// wir ihnen unseren temporären Verzeichnisnamen voranstellen.
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}

```
