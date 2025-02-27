# Mehrere Muster

In `match`-Ausdrücken kannst du mehrere Muster mit der `|`-Syntax abgleichen, die der Muster-_oder_-Operator ist. Beispielsweise passen wir im folgenden Code den Wert von `x` gegen die `match`-Arme an. Der erste Arm hat eine _oder_-Option, was bedeutet, dass wenn der Wert von `x` einem der Werte in diesem Arm entspricht, der Code dieses Arms ausgeführt wird:

Dateiname: `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("eins oder zwei"),
    3 => println!("drei"),
    _ => println!("irgendwas"),
}
```

Dieser Code druckt `eins oder zwei`.
