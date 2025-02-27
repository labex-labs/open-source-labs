# Rückgabe von Werten aus Schleifen

Eine der Verwendungszwecke eines `loop` ist es, eine Operation erneut auszuführen, von der Sie wissen, dass sie fehlschlagen kann, wie etwa das Überprüfen, ob ein Thread seine Aufgabe abgeschlossen hat. Möglicherweise müssen Sie auch das Ergebnis dieser Operation aus der Schleife an den Rest Ihres Codes weitergeben. Dazu können Sie den Wert, den Sie zurückgeben möchten, hinter dem `break`-Ausdruck anfügen, mit dem Sie die Schleife beenden; dieser Wert wird aus der Schleife zurückgegeben, sodass Sie ihn verwenden können, wie hier gezeigt:

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```

Vor der Schleife deklarieren wir eine Variable namens `counter` und initialisieren sie mit `0`. Dann deklarieren wir eine Variable namens `result`, um den Wert zu speichern, der aus der Schleife zurückgegeben wird. In jeder Iteration der Schleife erhöhen wir die Variable `counter` um `1` und überprüfen dann, ob `counter` gleich `10` ist. Wenn dies der Fall ist, verwenden wir das Schlüsselwort `break` mit dem Wert `counter * 2`. Nach der Schleife verwenden wir ein Semikolon, um den Ausdruck zu beenden, der den Wert an `result` zuweist. Schließlich drucken wir den Wert in `result`, der in diesem Fall `20` ist.
