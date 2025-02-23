# Zahlensyntaxanalyse

Das Extrahieren von Zahlen aus Zeichenketten ist in vielen Programmen eine häufige Aufgabe. In dieser Herausforderung müssen Sie das integrierte Paket `strconv` verwenden, um verschiedene Arten von Zahlen aus Zeichenketten zu analysieren.

## Anforderungen

- Verwenden Sie das Paket `strconv`, um Zahlen aus Zeichenketten zu analysieren.
- Analysieren Sie eine Gleitkommazahl mit `ParseFloat`.
- Analysieren Sie eine Ganzzahl mit `ParseInt`.
- Analysieren Sie eine hexadezimal formatierte Zahl mit `ParseInt`.
- Analysieren Sie eine vorzeichenlose Ganzzahl mit `ParseUint`.
- Analysieren Sie eine Dezimalzahl mit `Atoi`.
- Behandeln Sie die von den Analysefunktionen zurückgegebenen Fehler.

## Beispiel

```sh
$ go run number-parsing.go
1,234
123
456
789
135
strconv.ParseInt: Analyse von "wat": ungültige Syntax

# Als nächstes betrachten wir eine weitere häufige Analysetask: URLs.
```
