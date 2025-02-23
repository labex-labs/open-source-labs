# Dateien schreiben

Sie müssen ein Go-Programm schreiben, das einen String und Bytes in eine Datei schreibt und bufferte Writer verwendet.

- Das Programm sollte einen String und Bytes in eine Datei schreiben.
- Das Programm sollte bufferte Writer verwenden.

```sh
# Versuchen Sie, den Dateischreibcode auszuführen.
$ go run writing-files.go
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes

# Überprüfen Sie dann den Inhalt der geschriebenen Dateien.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# Als Nächstes betrachten wir die Anwendung einiger der
# Datei-E/A-Ideen, die wir gerade gesehen haben, auf die
# `stdin`- und `stdout`-Ströme.
```

Hier ist der vollständige Code:

```go
// Dateien in Go zu schreiben, folgt ähnlichen Mustern wie die,
// die wir früher beim Lesen gesehen haben.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Um zu beginnen, hier ist, wie man einen String (oder einfach
	// Bytes) in eine Datei schreibt.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// Für feinere Schreibvorgänge öffnen Sie eine Datei zum Schreiben.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// Es ist üblich, direkt nach dem Öffnen einer Datei ein `Close`
	// auszulösen.
	defer f.Close()

	// Sie können wie erwartet Byte-Slices `Write`.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// Ein `WriteString` ist ebenfalls verfügbar.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// Stellen Sie eine `Sync`-Operation aus, um die Schreibvorgänge
	// in die dauerhafte Speicherung zu flushen.
	f.Sync()

	// `bufio` bietet neben den buffered Readers, die wir früher
	// gesehen haben, auch buffered Writer an.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// Verwenden Sie `Flush`, um sicherzustellen, dass alle
	// buffered Operationen auf den zugrunde liegenden Writer
	// angewendet wurden.
	w.Flush()

}

```
