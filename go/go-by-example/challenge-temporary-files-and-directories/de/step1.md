# Temporäre Dateien und Verzeichnisse

In dieser Aufgabe musst du temporäre Dateien und Verzeichnisse in Go erstellen.

## Anforderungen

- Verwende `os.CreateTemp`, um eine temporäre Datei zu erstellen.
- Verwende `os.MkdirTemp`, um ein temporäres Verzeichnis zu erstellen.
- Verwende `os.RemoveAll`, um das temporäre Verzeichnis zu entfernen.
- Verwende `os.WriteFile`, um Daten in eine Datei zu schreiben.

## Beispiel

```sh
$ go run temporary-files-and-directories.go
Temp Dateiname: /tmp/sample610887201
Temp Verzeichnisname: /tmp/sampledir898854668
```
