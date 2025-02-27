# Expresiones

Un programa Rust está (en su mayoría) compuesto por una serie de declaraciones:

```rust
fn main() {
    // declaración
    // declaración
    // declaración
}
```

Hay varios tipos de declaraciones en Rust. Los dos más comunes son declarar un enlace de variable y usar un `;` con una expresión:

```rust
fn main() {
    // enlace de variable
    let x = 5;

    // expresión;
    x;
    x + 1;
    15;
}
```

Los bloques también son expresiones, por lo que se pueden usar como valores en asignaciones. La última expresión en el bloque se asignará a la ubicación de la expresión, como una variable local. Sin embargo, si la última expresión del bloque termina con un punto y coma, el valor de retorno será `()`.

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Esta expresión se asignará a `y`
        x_cube + x_squared + x
    };

    let z = {
        // El punto y coma suprime esta expresión y `()` se asigna a `z`
        2 * x;
    };

    println!("x es {:?}", x);
    println!("y es {:?}", y);
    println!("z es {:?}", z);
}
```
