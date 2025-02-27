# loop

Rust bietet das Schlüsselwort `loop` an, um eine Endlosschleife anzuzeigen.

Die `break`-Anweisung kann verwendet werden, um eine Schleife jederzeit zu verlassen, während die `continue`-Anweisung verwendet werden kann, um den Rest der Iteration zu überspringen und eine neue Iteration zu starten.

```rust
fn main() {
    let mut count = 0u32;

    println!("Lassen Sie uns bis ins Unendliche zählen!");

    // Endlosschleife
    loop {
        count += 1;

        if count == 3 {
            println!("drei");

            // Überspringen Sie den Rest dieser Iteration
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, das ist genug");

            // Beenden Sie diese Schleife
            break;
        }
    }
}
```
