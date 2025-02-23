# Iteration über Kanäle

Du musst eine Funktion schreiben, die einen Kanal von ganzen Zahlen annimmt und die Summe aller empfangenen ganzen Zahlen zurückgibt.

## Anforderungen

- Die Funktion sollte `sumInts` heißen.
- Die Funktion sollte einen einzigen Parameter vom Typ `chan int` entgegennehmen.
- Die Funktion sollte einen einzigen ganzzahligen Wert zurückgeben.
- Du darfst keine Schleifen oder Rekursionen innerhalb des Funktionskörpers verwenden.
- Du darfst keine externen Pakete verwenden.

## Beispiel

```sh
$ go run range-over-channels.go
eins
zwei

# Dieses Beispiel hat auch gezeigt, dass es möglich ist,
# einen nicht-leeren Kanal zu schließen, aber die verbleibenden
# Werte weiterhin zu empfangen.
```
