# Dateien lesen

In Ihrem Go-Programm müssen Sie Dateien lesen und verschiedene Operationen auf den Daten in der Datei ausführen.

## Anforderungen

- Sie sollten mit den grundlegenden Go-Programmierkonzepten vertraut sein.
- Sie sollten Go auf Ihrem Computer installiert haben.

## Beispiel

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Als nächstes werden wir uns ansehen, wie man Dateien schreibt.
```
