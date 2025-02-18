# Crear un nuevo mapa hash

Una forma de crear un mapa hash vacío es utilizar `new` y agregar elementos con `insert`. En la Lista 8-20, estamos llevando un registro de las puntuaciones de dos equipos cuyos nombres son _Blue_ (Azul) y _Yellow_ (Amarillo). El equipo Azul comienza con 10 puntos, y el equipo Amarillo comienza con 50.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

Lista 8-20: Crear un nuevo mapa hash e insertar algunas claves y valores

Ten en cuenta que primero debemos `usar` el `HashMap` de la sección de colecciones de la biblioteca estándar. De nuestras tres colecciones comunes, esta es la menos utilizada, por lo que no se incluye en las características que se traen automáticamente al alcance en el preludio. Los mapas hash también tienen menos soporte de la biblioteca estándar; por ejemplo, no hay una macro incorporada para construirlos.

Al igual que los vectores, los mapas hash almacenan sus datos en el montón (heap). Este `HashMap` tiene claves de tipo `String` y valores de tipo `i32`. Al igual que los vectores, los mapas hash son homogéneos: todas las claves deben tener el mismo tipo, y todos los valores deben tener el mismo tipo.
