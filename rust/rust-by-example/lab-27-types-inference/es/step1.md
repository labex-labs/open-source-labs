# Inferencia

El motor de inferencia de tipos es bastante inteligente. Hace más que simplemente examinar el tipo de la expresión de valor durante una inicialización. También observa cómo se utiliza la variable posteriormente para inferir su tipo. Aquí hay un ejemplo avanzado de inferencia de tipos:

```rust
fn main() {
    // Debido a la anotación, el compilador sabe que `elem` tiene el tipo u8.
    let elem = 5u8;

    // Crea un vector vacío (una matriz creciente).
    let mut vec = Vec::new();
    // En este momento, el compilador no conoce el tipo exacto de `vec`, solo
    // sabe que es un vector de algo (`Vec<_>`).

    // Inserta `elem` en el vector.
    vec.push(elem);
    // Aha! Ahora el compilador sabe que `vec` es un vector de `u8` (`Vec<u8>`)
    // TODO ^ Intenta comentar la línea `vec.push(elem)`

    println!("{:?}", vec);
}
```

No se necesitó ninguna anotación de tipo de variables, el compilador está contento y el programador también!
