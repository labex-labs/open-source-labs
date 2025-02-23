# Dateien schreiben

Sie müssen ein Go-Programm schreiben, das einen String und Bytes in eine Datei schreibt und Pufferwriter verwendet.

## Anforderungen

- Das Programm sollte einen String und Bytes in eine Datei schreiben.
- Das Programm sollte Pufferwriter verwenden.

## Beispiel

```sh
# Versuchen Sie, den Dateischreibencode auszuführen.
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
# gerade gesehenen Datei-E/A-Ideen auf die `stdin`- und
# `stdout`-Ströme.
```
