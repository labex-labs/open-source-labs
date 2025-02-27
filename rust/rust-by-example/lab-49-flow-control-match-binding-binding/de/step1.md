# Bindung

Indirekter Zugang zu einer Variable macht es unmöglich, diese Variable zu verzweigen und zu verwenden, ohne sie erneut zu binden. `match` bietet das `@`-Zeichen zum Binden von Werten an Namen:

```rust
// Eine Funktion `age`, die eine `u32` zurückgibt.
fn age() -> u32 {
    15
}

fn main() {
    println!("Sag mir, was für eine Art Person du bist");

    match age() {
        0             => println!("Ich habe noch keinen Geburtstag gefeiert"),
        // Könnte direkt `match` 1..= 12 verwenden, aber dann wäre das Alter
        // der Kindes noch unklar. Stattdessen binden wir an `n` für die
        // Sequenz 1..= 12. Jetzt kann das Alter gemeldet werden.
        n @ 1 ..= 12 => println!("Ich bin ein Kind im Alter von {:?}", n),
        n @ 13..= 19 => println!("Ich bin ein Teenager im Alter von {:?}", n),
        // Kein Binding. Gib das Ergebnis zurück.
        n             => println!("Ich bin ein alter Mensch im Alter von {:?}", n),
    }
}
```

Man kann auch Binding verwenden, um `enum`-Varianten wie `Option` "zerzulegen":

```rust
fn some_number() -> Option<u32> {
    Some(42)
}

fn main() {
    match some_number() {
        // Es wurde die `Some`-Variante erhalten. Prüfe, ob ihr Wert,
        // der an `n` gebunden ist, gleich 42 ist.
        Some(n @ 42) => println!("Die Antwort: {}!", n),
        // Prüfe auf jede andere Zahl.
        Some(n)      => println!("Nicht interessant... {}", n),
        // Prüfe auf alles andere (`None`-Variante).
        _            => (),
    }
}
```
