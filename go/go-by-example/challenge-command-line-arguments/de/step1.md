# Befehlszeilenargumente

Das Programm druckt derzeit die übergebenen rohen Befehlszeilenargumente aus. Es muss jedoch so modifiziert werden, dass bestimmte Argumente anhand ihrer Indexposition ausgegeben werden.

## Anforderungen

- Grundkenntnisse von Golang
- Vertrautheit mit Befehlszeilenargumenten

## Beispiel

```sh
# Um mit Befehlszeilenargumenten zu experimentieren, ist es am besten,
# zunächst eine Binärdatei mit `go build` zu erstellen.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Als nächstes betrachten wir die fortgeschrittene Befehlszeilenverarbeitung
# mit Flags.
```
