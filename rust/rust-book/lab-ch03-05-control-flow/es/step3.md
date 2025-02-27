# Manejo de múltiples condiciones con `else if`

Puedes utilizar múltiples condiciones combinando `if` y `else` en una expresión `else if`. Por ejemplo:

Nombre del archivo: `src/main.rs`

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

Este programa tiene cuatro posibles caminos que puede tomar. Después de ejecutarlo, deberías ver la siguiente salida:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

Cuando este programa se ejecuta, comprueba cada expresión `if` por turnos y ejecuta el primer cuerpo para el cual la condición evalúa a `true`. Tenga en cuenta que aunque 6 es divisible por 2, no vemos la salida `number is divisible by 2`, ni tampoco vemos el texto `number is not divisible by 4, 3, or 2` del bloque `else`. Eso se debe a que Rust solo ejecuta el bloque para la primera condición `true`, y una vez que la encuentra, ni siquiera comprueba el resto.

Utilizar demasiadas expresiones `else if` puede desordenar su código, por lo que si tiene más de una, es posible que desee refactorizar su código. El Capítulo 6 describe una constructura de ramificación poderosa de Rust llamada `match` para estos casos.
