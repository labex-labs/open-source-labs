# Accediendo a valores en un mapa hash

Podemos obtener un valor del mapa hash proporcionando su clave al método `get`, como se muestra en la Lista 8-21.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Lista 8-21: Accediendo a la puntuación del equipo Azul almacenada en el mapa hash

Aquí, `score` tendrá el valor asociado al equipo Azul, y el resultado será `10`. El método `get` devuelve un `Option<&V>`; si no hay un valor para esa clave en el mapa hash, `get` devolverá `None`. Este programa maneja el `Option` llamando a `copied` para obtener un `Option<i32>` en lugar de un `Option<&i32>`, luego `unwrap_or` para establecer `score` en cero si `scores` no tiene una entrada para la clave.

Podemos iterar sobre cada par clave-valor en un mapa hash de manera similar a como lo hacemos con los vectores, utilizando un bucle `for`:

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

Este código imprimirá cada par en un orden arbitrario:

```rust
Yellow: 50
Blue: 10
```
