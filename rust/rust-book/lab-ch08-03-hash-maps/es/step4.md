# Mapas hash y propiedad (Ownership)

Para tipos que implementan el rasgo (trait) `Copy`, como `i32`, los valores se copian en el mapa hash. Para valores con propiedad (owned values) como `String`, los valores se moverán y el mapa hash será el propietario de esos valores, como se demuestra en la Lista 8-22.

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

Lista 8-22: Mostrando que las claves y valores son propiedad del mapa hash una vez que se insertan

No podemos usar las variables `field_name` y `field_value` después de que se hayan movido al mapa hash con la llamada a `insert`.

Si insertamos referencias a valores en el mapa hash, los valores no se moverán al mapa hash. Los valores a los que apuntan las referencias deben ser válidos al menos durante el tiempo que el mapa hash sea válido. Hablaremos más sobre estos problemas en "Validating References with Lifetimes" (Validando referencias con períodos de vida).
