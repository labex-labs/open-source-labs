# Embed-Anweisung

Ihre Aufgabe ist es, den gegebenen Code zu modifizieren, um Dateien und Ordner in die Go-Binärdatei zu integrieren und deren Inhalt auszugeben.

- Sie müssen das `embed`-Paket verwenden, um Dateien und Ordner zu integrieren.
- Sie müssen die `string`- und `[]byte`-Typen verwenden, um den Inhalt der integrierten Dateien zu speichern.
- Sie müssen den `embed.FS`-Typ verwenden, um mehrere Dateien oder Ordner mit Platzhaltern zu integrieren.
- Sie müssen den Inhalt der integrierten Dateien ausgeben.

```sh
# Verwenden Sie diese Befehle, um das Beispiel auszuführen.
# (Hinweis: Aufgrund der Einschränkungen auf dem Go Playground
# kann dieses Beispiel nur auf Ihrem lokalen Computer ausgeführt werden.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```

Hier ist der vollständige Code:

```go
// `//go:embed` ist eine [Compileranweisung](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives),
// die es Programmen ermöglicht, beliebige Dateien und Ordner bei der Build-Zeit in die Go-Binärdatei zu integrieren.
// Lesen Sie mehr über die embed-Anweisung [hier](https://pkg.go.dev/embed).
package main

// Importieren Sie das `embed`-Paket; wenn Sie keine exportierten
// Bezeichner aus diesem Paket verwenden, können Sie eine leere Importe mit `_ "embed"` durchführen.
import (
	"embed"
)

// `embed`-Anweisungen akzeptieren Pfade relativ zum Verzeichnis, das die
// Go-Quelldatei enthält. Diese Anweisung integriert den Inhalt der Datei in die
// `string`-Variable, die unmittelbar darauf folgt.
//
//go:embed folder/single_file.txt
var fileString string

// Oder integrieren Sie den Inhalt der Datei in ein `[]byte`.
//
//go:embed folder/single_file.txt
var fileByte []byte

// Wir können auch mehrere Dateien oder sogar Ordner mit Platzhaltern integrieren.
// Dies verwendet eine Variable vom Typ [embed.FS](https://pkg.go.dev/embed#FS),
// der ein einfaches virtuelles Dateisystem implementiert.
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// Geben Sie den Inhalt von `single_file.txt` aus.
	print(fileString)
	print(string(fileByte))

	// Holen Sie sich einige Dateien aus dem integrierten Ordner.
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}

```
