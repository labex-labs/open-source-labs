# Retornar desde bucles

Una de las usos de un `loop` es reintentar una operación hasta que tenga éxito. Sin embargo, si la operación devuelve un valor, es posible que necesites pasarlo al resto del código: colócalo después del `break`, y será devuelto por la expresión `loop`.

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
