# HashMap

Mientras que los vectores almacenan valores mediante un índice entero, los `HashMap` almacenan valores por clave. Las claves de `HashMap` pueden ser booleanos, enteros, cadenas o cualquier otro tipo que implemente los rasgos `Eq` y `Hash`. Más sobre esto en la siguiente sección.

Como los vectores, los `HashMap` son crecibles, pero los `HashMap` también pueden contraerse a sí mismos cuando tienen espacio sobrante. Puedes crear un `HashMap` con una capacidad inicial determinada utilizando `HashMap::with_capacity(uint)`, o utilizar `HashMap::new()` para obtener un `HashMap` con una capacidad inicial predeterminada (recomendado).

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "Lo sentimos, la llamada no se puede completar con el número marcado.
            Por favor cuelgue y vuelva a intentarlo.",
        "645-7689" => "Hola, esta es la pizzería de Sr. Genial. Me llamo Fred.
            ¿En qué puedo ayudarte hoy?",
        _ => "¡Hola! ¿Quién es esta vez?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Toma una referencia y devuelve Option<&V>
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Llamando a Daniel: {}", call(number)),
        _ => println!("No tengo el número de Daniel."),
    }

    // `HashMap::insert()` devuelve `None`
    // si el valor insertado es nuevo, `Some(value)` en caso contrario
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Llamando a Ashley: {}", call(number)),
        _ => println!("No tengo el número de Ashley."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` devuelve un iterador que produce
    // pares (&'a key, &'a value) en un orden arbitrario.
    for (contact, &number) in contacts.iter() {
        println!("Llamando a {}: {}", contact, call(number));
    }
}
```

Para obtener más información sobre cómo funcionan los algoritmos de hash y las tablas hash (a veces llamadas tablas hash), echa un vistazo a Tabla hash en Wikipedia
