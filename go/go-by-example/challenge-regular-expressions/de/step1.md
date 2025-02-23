# Reguläre Ausdrücke

Die Herausforderung erfordert es, den Code zu vervollständigen, um verschiedene mit regulären Ausdrücken zusammenhängende Aufgaben in Golang durchzuführen.

## Anforderungen

- Verwenden des `regexp`-Pakets, um mit regulären Ausdrücken zusammenhängende Aufgaben durchzuführen.
- Verwenden von `MatchString`, um zu testen, ob ein Muster einem String entspricht.
- Verwenden von `Compile`, um eine `Regexp`-Struktur zu optimieren.
- Verwenden von `MatchString`, um eine Übereinstimmung wie `Compile` zu testen.
- Verwenden von `FindString`, um die Übereinstimmung für den regulären Ausdruck zu finden.
- Verwenden von `FindStringIndex`, um die erste Übereinstimmung zu finden und die Start- und Endindizes für die Übereinstimmung statt des übereinstimmenden Texts zurückzugeben.
- Verwenden von `FindStringSubmatch`, um Informationen für sowohl `p([a-z]+)ch` als auch `([a-z]+)` zurückzugeben.
- Verwenden von `FindStringSubmatchIndex`, um Informationen über die Indizes von Übereinstimmungen und Teilübereinstimmungen zurückzugeben.
- Verwenden von `FindAllString`, um alle Übereinstimmungen für einen regulären Ausdruck zu finden.
- Verwenden von `FindAllStringSubmatchIndex`, um auf alle Übereinstimmungen in der Eingabe anzuwenden, nicht nur auf die erste.
- Verwenden von `Match`, um eine Übereinstimmung mit `[]byte`-Argumenten zu testen und `String` aus dem Funktionsnamen zu entfernen.
- Verwenden von `MustCompile`, um globale Variablen mit regulären Ausdrücken zu erstellen.
- Verwenden von `ReplaceAllString`, um Teilmengen von Strings durch andere Werte zu ersetzen.
- Verwenden von `ReplaceAllFunc`, um das übereinstimmende Text mit einer angegebenen Funktion zu transformieren.

## Beispiel

```sh
$ go run regular-expressions.go
true
true
peach
idx: [0 5]
[peach ea]
[0 5 1 3]
[peach punch pinch]
all: [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
[peach punch]
true
regexp: p([a-z]+)ch
a <fruit>
a PEACH

# Für eine vollständige Referenz zu Go regulären Ausdrücken überprüfen
# die Dokumentation des [`regexp`](https://pkg.go.dev/regexp)-Pakets.

```
