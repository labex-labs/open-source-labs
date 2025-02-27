# Usando Estructuras Tupla Sin Campos con Nombres para Crear Diferentes Tipos

Rust también admite estructuras que se parecen a las tuplas, llamadas _estructuras tupla_. Las estructuras tupla tienen el significado adicional que proporciona el nombre de la estructura pero no tienen nombres asociados a sus campos; en cambio, solo tienen los tipos de los campos. Las estructuras tupla son útiles cuando quieres darle un nombre a toda la tupla y hacer que la tupla sea de un tipo diferente de otras tuplas, y cuando nombrar cada campo como en una estructura regular sería verboso o redundante.

Para definir una estructura tupla, comienza con la palabra clave `struct` y el nombre de la estructura seguido de los tipos en la tupla. Por ejemplo, aquí definimos y usamos dos estructuras tupla llamadas `Color` y `Point`:

Nombre del archivo: `src/main.rs`

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Tenga en cuenta que los valores `black` y `origin` son de diferentes tipos porque son instancias de diferentes estructuras tupla. Cada estructura que defines es su propio tipo, aunque los campos dentro de la estructura pueden tener los mismos tipos. Por ejemplo, una función que toma un parámetro de tipo `Color` no puede tomar un `Point` como argumento, aunque ambos tipos están compuestos por tres valores de `i32`. De lo contrario, las instancias de estructuras tupla son similares a las tuplas en el sentido de que se pueden desestructurar en sus piezas individuales, y se puede usar un `.` seguido del índice para acceder a un valor individual.
