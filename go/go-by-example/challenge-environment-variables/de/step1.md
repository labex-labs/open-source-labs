# Umgebungsvariablen

In dieser Aufgabe musst du Umgebungsvariablen setzen, abrufen und auflisten.

## Anforderungen

- Verwende `os.Setenv`, um ein Schlüssel-Wert-Paar zu setzen.
- Verwende `os.Getenv`, um einen Wert für einen Schlüssel abzurufen.
- Verwende `os.Environ`, um alle Schlüssel-Wert-Paare in der Umgebung aufzulisten.
- Verwende `strings.SplitN`, um den Schlüssel und den Wert aufzuteilen.

## Beispiel

```sh
# Wenn man das Programm ausführt, zeigt sich, dass wir den Wert
# für `FOO` erhalten, den wir im Programm gesetzt haben, aber dass
# `BAR` leer ist.
$ go run environment-variables.go
FOO: 1
BAR:

# Die Liste der Schlüssel in der Umgebung hängt von deiner
# speziellen Maschine ab.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Wenn wir `BAR` zuerst in der Umgebung setzen, erhält das
# ausgeführte Programm diesen Wert.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```
