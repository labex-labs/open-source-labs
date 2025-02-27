# Bucles `for`

En un bucle `for`, el valor que sigue directamente a la palabra clave `for` es un patrón. Por ejemplo, en `for x in y`, el `x` es el patrón. El Listado 18-3 demuestra cómo usar un patrón en un bucle `for` para _desestructurar_, o descomponer, una tupla como parte del bucle `for`.

Nombre del archivo: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listado 18-3: Usando un patrón en un bucle `for` para desestructurar una tupla

El código en el Listado 18-3 imprimirá lo siguiente:

    a is at index 0
    b is at index 1
    c is at index 2

Adaptamos un iterador usando el método `enumerate` para que produzca un valor y el índice para ese valor, colocados en una tupla. El primer valor producido es la tupla `(0, 'a')`. Cuando este valor se coincide con el patrón `(index, value)`, `index` será `0` y `value` será `'a'`, imprimiendo la primera línea de la salida.
