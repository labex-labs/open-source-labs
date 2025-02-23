# Defer

In dieser Aufgabe musst du `defer` verwenden, um eine Datei zu erstellen, in sie zu schreiben und sie anschließend zu schließen, wenn du fertig bist.

## Anforderungen

- Die `createFile`-Funktion sollte eine Datei mit dem angegebenen Pfad erstellen und einen Zeiger auf die Datei zurückgeben.
- Die `writeFile`-Funktion sollte den String "data" in die Datei schreiben.
- Die `closeFile`-Funktion sollte die Datei schließen und auf Fehler prüfen.

## Beispiel

```sh
# Wenn das Programm ausgeführt wird, wird bestätigt, dass die Datei
# nach dem Schreiben geschlossen ist.
$ go run defer.go
creating
writing
closing
```
