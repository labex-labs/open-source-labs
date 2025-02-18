# Agregar una clave y un valor solo si la clave no está presente

Es común verificar si una clave en particular ya existe en el mapa hash con un valor y luego tomar las siguientes acciones: si la clave ya existe en el mapa hash, el valor existente debe permanecer tal como está; si la clave no existe, insertarla y un valor para ella.

Los mapas hash tienen una API especial para esto llamada `entry` que toma como parámetro la clave que se desea verificar. El valor de retorno del método `entry` es un enumerado (enum) llamado `Entry` que representa un valor que puede o no existir. Digamos que queremos verificar si la clave para el equipo Amarillo tiene un valor asociado. Si no lo tiene, queremos insertar el valor `50`, y lo mismo para el equipo Azul. Usando la API `entry`, el código se ve como en la Lista 8-24.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```

Lista 8-24: Usando el método `entry` para insertar solo si la clave no tiene ya un valor

El método `or_insert` en `Entry` está definido para devolver una referencia mutable al valor de la clave `Entry` correspondiente si esa clave existe, y si no, inserta el parámetro como el nuevo valor para esta clave y devuelve una referencia mutable al nuevo valor. Esta técnica es mucho más limpia que escribir la lógica nosotros mismos y, además, funciona mejor con el verificador de préstamos (borrow checker).

Ejecutar el código de la Lista 8-24 imprimirá `{"Yellow": 50, "Blue": 10}`. La primera llamada a `entry` insertará la clave para el equipo Amarillo con el valor `50` porque el equipo Amarillo no tiene un valor ya. La segunda llamada a `entry` no cambiará el mapa hash porque el equipo Azul ya tiene el valor `10`.
