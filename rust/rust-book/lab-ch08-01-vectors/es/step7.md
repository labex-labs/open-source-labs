# Al eliminar un vector, se eliminan sus elementos

Como cualquier otro `struct`, un vector se libera cuando sale de ámbito, como se anota en la Lista 8-10.

```rust
{
    let v = vec![1, 2, 3, 4];

    // hacer cosas con v
} // <- v sale de ámbito y se libera aquí
```

Lista 8-10: Mostrando dónde se eliminan el vector y sus elementos

Cuando el vector se elimina, todos sus contenidos también se eliminan, lo que significa que los enteros que contiene se limpiarán. El verificador de préstamos asegura que cualquier referencia a los contenidos de un vector solo se use mientras el vector mismo es válido.

Pasemos a la siguiente tipo de colección: `String`!
