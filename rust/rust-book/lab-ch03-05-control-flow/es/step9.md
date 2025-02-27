# Bucles Condicionales con `while`

Un programa a menudo necesita evaluar una condición dentro de un bucle. Mientras la condición sea `true`, el bucle se ejecuta. Cuando la condición deja de ser `true`, el programa llama a `break`, deteniendo el bucle. Es posible implementar un comportamiento como este combinando `loop`, `if`, `else` y `break`; podrías probarlo ahora en un programa, si quieres. Sin embargo, este patrón es tan común que Rust tiene una construcción de lenguaje incorporada para ello, llamada bucle `while`. En la Lista 3-3, usamos `while` para hacer que el programa itere tres veces, contando hacia atrás cada vez, y luego, después del bucle, imprimir un mensaje y salir.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let mut number = 3;

    while number!= 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

Lista 3-3: Usando un bucle `while` para ejecutar código mientras una condición se evalúa como `true`

Esta construcción elimina mucha de la anidación que sería necesaria si se usaran `loop`, `if`, `else` y `break`, y es más clara. Mientras una condición se evalúa como `true`, el código se ejecuta; de lo contrario, sale del bucle.
