# Der Tupeltyp

Ein _Tupel_ ist eine allgemeine Möglichkeit, eine Anzahl von Werten mit verschiedenen Typen zu einer zusammengesetzten Einheit zu gruppieren. Tupel haben eine feste Länge: Einmal deklariert, können sie sich nicht in der Größe vergrößern oder verkleinern.

Wir erstellen ein Tupel, indem wir eine komma-getrennte Liste von Werten in Klammern schreiben. Jede Position im Tupel hat einen Typ, und die Typen der verschiedenen Werte im Tupel müssen nicht gleich sein. Wir haben in diesem Beispiel optionale Typangaben hinzugefügt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

Die Variable `tup` bindet sich an das gesamte Tupel, da ein Tupel als einzelnes zusammengesetztes Element betrachtet wird. Um die einzelnen Werte aus einem Tupel zu extrahieren, können wir Musterzuweisung verwenden, um einen Tupelwert aufzuteilen, wie folgt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("The value of y is: {y}");
}
```

Dieses Programm erstellt zunächst ein Tupel und bindet es an die Variable `tup`. Anschließend verwendet es ein Muster mit `let`, um `tup` zu nehmen und es in drei separate Variablen, `x`, `y` und `z`, umzuwandeln. Dies wird als _Auflösen_ bezeichnet, da es das einzelne Tupel in drei Teile aufbricht. Schließlich druckt das Programm den Wert von `y`, der `6.4` ist.

Wir können auch direkt auf ein Tupel-Element zugreifen, indem wir ein Punkt (`.`) gefolgt von dem Index des Werts, auf den wir zugreifen möchten, verwenden. Beispiel:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

Dieses Programm erstellt das Tupel `x` und greift dann auf jedes Element des Tupels über ihre jeweiligen Indizes zu. Wie in den meisten Programmiersprachen ist der erste Index in einem Tupel 0.

Das Tupel ohne irgendwelche Werte hat einen speziellen Namen, _Unit_. Dieser Wert und sein zugehöriger Typ werden beide als `()` geschrieben und stellen einen leeren Wert oder einen leeren Rückgabetyp dar. Ausdrücke geben implizit den Unit-Wert zurück, wenn sie keinen anderen Wert zurückgeben.
