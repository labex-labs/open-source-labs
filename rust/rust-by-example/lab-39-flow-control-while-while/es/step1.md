# while

La palabra clave `while` se puede utilizar para ejecutar un bucle mientras una condición sea verdadera.

Vamos a escribir el famoso FizzBuzz utilizando un bucle `while`.

```rust
fn main() {
    // Una variable contador
    let mut n = 1;

    // Bucle mientras `n` sea menor que 101
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

        // Incrementar el contador
        n += 1;
    }
}
```
