# if/else

La bifurcación con `if`-`else` es similar a otros lenguajes. A diferencia de muchos de ellos, la condición booleana no necesita estar rodeada de paréntesis y cada condición está seguida de un bloque. Las condicionales `if`-`else` son expresiones y todas las ramas deben devolver el mismo tipo.

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} es negativo", n);
    } else if n > 0 {
        print!("{} es positivo", n);
    } else {
        print!("{} es cero", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", y es un número pequeño, multiplíquelo por diez");

            // Esta expresión devuelve un `i32`.
            10 * n
        } else {
            println!(", y es un número grande, divídalo por dos");

            // Esta expresión también debe devolver un `i32`.
            n / 2
            // TODO ^ Intente suprimir esta expresión con un punto y coma.
        };
    //   ^ No olvide poner un punto y coma aquí. Todas las asignaciones `let` lo necesitan.

    println!("{} -> {}", n, big_n);
}
```
