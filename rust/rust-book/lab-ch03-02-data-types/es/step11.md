# Accediendo a los Elementos de un Array

Un array es un solo bloque de memoria de un tamaño conocido y fijo que se puede asignar en la pila. Puedes acceder a los elementos de un array usando índices, como esto:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

En este ejemplo, la variable llamada `first` obtendrá el valor `1` porque ese es el valor en el índice `[0]` del array. La variable llamada `second` obtendrá el valor `2` del índice `[1]` en el array.
