# Verzeichnisse

Erstelle ein Go-Programm, das ein neues Unterverzeichnis im aktuellen Arbeitsverzeichnis erstellt, eine Verzeichnishierarchie einschließlich der Elternverzeichnisse erstellt, die Verzeichnisinhalte auflistet, das aktuelle Arbeitsverzeichnis ändert und ein Verzeichnis rekursiv durchsucht.

## Anforderungen

- Erstelle ein neues Unterverzeichnis im aktuellen Arbeitsverzeichnis.
- Wenn temporäre Verzeichnisse erstellt werden, ist es eine gute Praxis, deren Entfernung mit `defer` zu planen. `os.RemoveAll` löscht einen ganzen Verzeichnisbaum (ähnlich wie `rm -rf`).
- Erstelle eine Verzeichnishierarchie einschließlich der Elternverzeichnisse mit `MkdirAll`. Dies ist ähnlich dem Befehlszeilenbefehl `mkdir -p`.
- `ReadDir` listet die Verzeichnisinhalte auf und gibt eine Liste von `os.DirEntry`-Objekten zurück.
- `Chdir` ermöglicht es uns, das aktuelle Arbeitsverzeichnis zu ändern, ähnlich wie `cd`.
- Besuche ein Verzeichnis rekursiv, einschließlich aller seiner Unterverzeichnisse. `Walk` akzeptiert eine Rückruffunktion, um jedes besuchte Verzeichnis oder jede besuchte Datei zu verarbeiten.

## Beispiel

```sh
$ go run directories.go
Verzeichnisinhalt von subdir/parent auflisten
child true
file2 false
file3 false
Verzeichnisinhalt von subdir/parent/child auflisten
file4 false
Verzeichnis subdir durchsuchen
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
