# Text Templates

In dieser Aufgabe müssen Sie die Verwendung des Pakets `text/template` zur Erzeugung von dynamischem Inhalt demonstrieren.

## Anforderungen

- Verwenden Sie das Paket `text/template` zur Erzeugung von dynamischem Inhalt.
- Verwenden Sie die Funktion `template.Must`, um einen Fehler auszulösen, wenn `Parse` einen Fehler zurückgibt.
- Verwenden Sie die Aktion `{{.FieldName}}`, um auf Strukturfelder zuzugreifen.
- Verwenden Sie die Aktion `{{if..}} ja {{else..}} nein {{end}}\n`, um bedingte Ausführung für Vorlagen zu gewährleisten.
- Verwenden Sie die Aktion `{{range.}}{{.}} {{end}}\n`, um durch Slices, Arrays, Maps oder Kanäle zu iterieren.

## Beispiel

```sh
$ go run templates.go
Wert: einiger Text
Wert: 5
Wert: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
ja
nein
Range: Go Rust C++ C#
```
