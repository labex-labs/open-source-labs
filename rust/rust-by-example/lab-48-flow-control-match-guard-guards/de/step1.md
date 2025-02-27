# Guards

Ein `match`-_Guard_ kann hinzugefügt werden, um den Arm zu filtern.

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO versuchen Sie verschiedene Werte für `temperature`

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C ist über 30 Celsius", t),
        // Der `if-Bedingung`-Teil ^ ist ein Guard
        Temperature::Celsius(t) => println!("{}C ist unter 30 Celsius", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}F ist über 86 Fahrenheit", t),
        Temperature::Fahrenheit(t) => println!("{}F ist unter 86 Fahrenheit", t),
    }
}
```

Beachten Sie, dass der Compiler die Guard-Bedingungen nicht berücksichtigt, wenn er überprüft, ob alle Muster vom Match-Ausdruck abgedeckt werden.

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("Zero"),
        i if i > 0 => println!("Greater than zero"),
        // _ => unreachable!("Should never happen."),
        // TODO ^ kommentieren Sie diese Zeile aus, um die Kompilierung zu beheben
    }
}
```
