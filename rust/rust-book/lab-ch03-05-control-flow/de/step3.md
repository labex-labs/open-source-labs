# Mehrere Bedingungen mit else if behandeln

Sie können mehrere Bedingungen kombinieren, indem Sie `if` und `else` in einem `else if`-Ausdruck verwenden. Beispielsweise:

Dateiname: `src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

Dieses Programm hat vier mögliche Pfade, die es einschlagen kann. Nachdem Sie es ausgeführt haben, sollten Sie die folgende Ausgabe sehen:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

Wenn dieses Programm ausgeführt wird, prüft es nacheinander jede `if`-Bedingung und führt den ersten Codeblock aus, für den die Bedingung `true` ausgewertet wird. Beachten Sie, dass obwohl 6 durch 2 teilbar ist, wir weder die Ausgabe `number is divisible by 2` noch den Text `number is not divisible by 4, 3, or 2` aus dem `else`-Block sehen. Das liegt daran, dass Rust nur den Codeblock für die erste `true`-Bedingung ausführt und sobald er eine findet, er nicht einmal die restlichen prüft.

Das Verwenden zu vieler `else if`-Ausdrücke kann Ihren Code unübersichtlich machen, daher sollten Sie, wenn Sie mehr als einen haben, Ihren Code möglicherweise umgestalten. Kapitel 6 beschreibt einen leistungsstarken Rust-Zweigungskonstrukt, den `match`, für diese Fälle.
