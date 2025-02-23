# Zufallszahlen

Es wird ein Programm geschrieben, das Zufallszahlen im Bereich von ganzzahligen und Gleitkommazahlen generiert. Das Programm sollte auch in der Lage sein, verschiedene Zahlenfolgen durch Ändern des Seeds zu erzeugen.

## Anforderungen

- Das Programm sollte das Paket `math/rand` verwenden, um Zufallszahlen zu generieren.
- Das Programm sollte Zufallszahlen im Bereich von ganzzahligen Zahlen generieren.
- Das Programm sollte Zufallszahlen im Bereich von Gleitkommazahlen generieren.
- Das Programm sollte in der Lage sein, verschiedene Zahlenfolgen durch Ändern des Seeds zu erzeugen.

## Beispiel

```sh
# Je nach Ausführungsort dieses Beispiels können
# einige der generierten Zahlen unterschiedlich
# sein. Beachten Sie, dass auf dem Go-Playground
# das Setzen des Seeds mit `time.Now()` aufgrund
# der Implementierung des Playgrounds immer noch
# deterministische Ergebnisse liefert.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Siehe die Dokumentation des Pakets
# [`math/rand`](https://pkg.go.dev/math/rand), um
# Referenzen zu anderen Zufallszahlen zu erhalten,
# die Go liefern kann.
```
