# Line Filters

Das Problem, das in dieser Herausforderung gelöst werden muss, ist es, ein Go-Programm zu schreiben, das Eingabetext von der Standardeingabe liest, alle Buchstaben im Text in Großbuchstaben umwandelt und dann den modifizierten Text auf die Standardausgabe ausgibt.

## Anforderungen

- Das Programm muss Eingabetext von der Standardeingabe lesen.
- Das Programm muss alle Buchstaben im Eingabetext in Großbuchstaben umwandeln.
- Das Programm muss den modifizierten Text auf die Standardausgabe ausgeben.

## Beispiel

```sh
# Um unseren Line Filter zu testen, erstellen Sie zunächst eine Datei
# mit einigen Kleinbuchstabenzeilen.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Verwenden Sie dann den Line Filter, um Großbuchstabenzeilen zu erhalten.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```
