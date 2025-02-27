# Literale abgleichen

Wie du im Kapitel 6 gesehen hast, kannst du Muster direkt gegen Literale abgleichen. Der folgende Code gibt einige Beispiele:

Dateiname: `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("eins"),
    2 => println!("zwei"),
    3 => println!("drei"),
    _ => println!("irgendwas"),
}
```

Dieser Code druckt `eins`, weil der Wert in `x` `1` ist. Diese Syntax ist nützlich, wenn du möchtest, dass dein Code eine Aktion ausführt, wenn er einen bestimmten konkreten Wert erhält.
