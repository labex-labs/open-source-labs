# Timer und Taster

In dieser Herausforderung müssen Sie einen Taster erstellen, der alle 500 Millisekunden tickt, bis wir ihn stoppen. Sie werden einen Kanal verwenden, um auf die Werte zu warten, wenn sie eintreffen.

## Anforderungen

- Verwenden Sie das `time`-Paket, um einen Taster zu erstellen.
- Verwenden Sie einen Kanal, um auf die Werte zu warten, wenn sie eintreffen.
- Verwenden Sie die `select`-Anweisung, um Werte aus dem Kanal zu empfangen.
- Stoppen Sie den Taster nach 1600 Millisekunden.

## Beispiel

```sh
# Wenn wir dieses Programm ausführen, sollte der Taster 3 mal ticken
# bevor wir ihn stoppen.
$ go run tickers.go
Tick um 2012-09-23 11:29:56.487625 -0700 PDT
Tick um 2012-09-23 11:29:56.988063 -0700 PDT
Tick um 2012-09-23 11:29:57.488076 -0700 PDT
Taster gestoppt
```
