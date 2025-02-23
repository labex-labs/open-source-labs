# Dateipfade

In dieser Aufgabe musst du das `filepath`-Paket verwenden, um verschiedene Operationen auf Dateipfaden durchzuführen, wie z. B. das portierbare Konstruieren von Pfaden, das Aufteilen eines Pfads in Verzeichnis- und Dateikomponenten, das Überprüfen, ob ein Pfad absolut ist, das Finden der Dateierweiterung und das Finden eines relativen Pfads zwischen zwei Pfaden.

## Anforderungen

- Verwende `Join`, um Pfade auf eine portierbare Weise zu konstruieren.
- Verwende `Dir` und `Base`, um einen Pfad in Verzeichnis- und Dateikomponenten aufzuteilen.
- Verwende `IsAbs`, um zu überprüfen, ob ein Pfad absolut ist.
- Verwende `Ext`, um die Dateierweiterung einer Datei zu finden.
- Verwende `TrimSuffix`, um die Dateierweiterung aus einem Dateinamen zu entfernen.
- Verwende `Rel`, um einen relativen Pfad zwischen zwei Pfaden zu finden.

## Beispiel

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```
