# Wertebereiche mit..= abgleichen

Die `..=`-Syntax ermöglicht es uns, auf einen inklusiven Wertebereich abzustimmen. Im folgenden Code wird, wenn ein Muster einem der Werte innerhalb des angegebenen Bereichs entspricht, der Arm ausgeführt:

Dateiname: `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("eins bis fünf"),
    _ => println!("etwas anderes"),
}
```

Wenn `x` `1`, `2`, `3`, `4` oder `5` ist, wird der erste Arm übereinstimmen. Diese Syntax ist für mehrere Übereinstimmungswerte bequemer als die Verwendung des `|`-Operators, um die gleiche Idee auszudrücken; wenn wir `|` verwenden würden, müssten wir `1 | 2 | 3 | 4 | 5` angeben. Das Angeben eines Bereichs ist viel kürzer, insbesondere wenn wir beispielsweise alle Zahlen zwischen 1 und 1.000 abgleichen möchten!

Der Compiler überprüft bei der Kompilierung, dass der Bereich nicht leer ist, und da die einzigen Typen, für die Rust feststellen kann, ob ein Bereich leer ist oder nicht, `char` und numerische Werte sind, sind nur numerische oder `char`-Werte mit Bereichen erlaubt.

Hier ist ein Beispiel mit `char`-Wertebereichen:

Dateiname: `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("früher ASCII-Buchstabe"),
    'k'..='z' => println!("später ASCII-Buchstabe"),
    _ => println!("etwas anderes"),
}
```

Rust kann erkennen, dass `'c'` innerhalb des ersten Musters liegt, und druckt `früher ASCII-Buchstabe`.
