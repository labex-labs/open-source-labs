# match

Rust bietet Musterabgleich über das Schlüsselwort `match`, das wie eine C-`switch` verwendet werden kann. Der erste übereinstimmende Fall wird ausgewertet, und alle möglichen Werte müssen abgedeckt werden.

```rust
fn main() {
    let number = 13;
    // TODO ^ Versuchen Sie verschiedene Werte für `number`

    println!("Sag mir etwas über {}", number);
    match number {
        // Einen einzelnen Wert abgleichen
        1 => println!("Eins!"),
        // Mehrere Werte abgleichen
        2 | 3 | 5 | 7 | 11 => println!("Dies ist eine Primzahl"),
        // TODO ^ Versuchen Sie, 13 der Liste der Primzahlen hinzuzufügen
        // Einen eingeschlossenen Bereich abgleichen
        13..=19 => println!("Eine Zehner"),
        // Die restlichen Fälle behandeln
        _ => println!("Nichts besonderes"),
        // TODO ^ Versuchen Sie, diesen allgemeinen Fall zu kommentieren
    }

    let boolean = true;
    // Match ist auch ein Ausdruck
    let binary = match boolean {
        // Die Fälle eines Matches müssen alle möglichen Werte abdecken
        false => 0,
        true => 1,
        // TODO ^ Versuchen Sie, einen dieser Fälle zu kommentieren
    };

    println!("{} -> {}", boolean, binary);
}
```
