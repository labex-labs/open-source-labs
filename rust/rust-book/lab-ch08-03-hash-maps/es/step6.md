# Sobrescribir un valor

Si insertamos una clave y un valor en un mapa hash y luego insertamos la misma clave con un valor diferente, el valor asociado a esa clave se reemplazará. Aunque el código de la Lista 8-23 llama a `insert` dos veces, el mapa hash solo contendrá un par clave-valor porque estamos insertando el valor para la clave del equipo Azul ambas veces.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

Lista 8-23: Reemplazando un valor almacenado con una clave en particular

Este código imprimirá `{"Blue": 25}`. El valor original de `10` ha sido sobrescrito.
