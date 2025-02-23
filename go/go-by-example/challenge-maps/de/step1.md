# Maps

In dieser Aufgabe müssen Sie eine Map erstellen, die die Anzahl der Vorkommen jedes Wortes in einem gegebenen String speichert. Sie müssen den String in Wörter aufteilen und dann über jedes Wort iterieren, es der Map hinzufügen, wenn es noch nicht vorhanden ist, oder seinen Zähler inkrementieren, wenn es bereits vorhanden ist.

## Anforderungen

- Sie müssen eine Map verwenden, um die Wortzahlen zu speichern.
- Sie müssen den Eingabestring in Wörter aufteilen.
- Sie müssen über jedes Wort im Eingabestring iterieren.
- Sie müssen jedes Wort der Map hinzufügen, wenn es noch nicht vorhanden ist, oder seinen Zähler inkrementieren, wenn es bereits vorhanden ist.

## Beispiel

```sh
# Beachten Sie, dass Maps im Format `map[k:v k:v]` erscheinen, wenn
# mit `fmt.Println` gedruckt.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```
