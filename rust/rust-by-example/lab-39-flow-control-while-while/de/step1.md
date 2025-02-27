# while

Das Schlüsselwort `while` kann verwendet werden, um eine Schleife auszuführen, solange eine Bedingung wahr ist.

Schreiben wir das berüchtigte FizzBuzz mit einer `while`-Schleife.

```rust
fn main() {
    // Eine Zählvariable
    let mut n = 1;

    // Schleife, solange `n` kleiner als 101 ist
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // Zähler erhöhen
        n += 1;
    }
}
```
