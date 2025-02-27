# Partes restantes de un valor con..

Con valores que tienen muchas partes, podemos usar la sintaxis `..` para usar partes específicas e ignorar el resto, evitando la necesidad de listar guiones bajos para cada valor ignorado. El patrón `..` ignora cualquier parte de un valor que no hayamos coincidido explícitamente en el resto del patrón. En la Lista 18-23, tenemos una struct `Point` que almacena una coordenada en un espacio tridimensional. En la expresión `match`, queremos operar solo en la coordenada `x` e ignorar los valores en los campos `y` y `z`.

Nombre de archivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
    z: i32,
}

let origin = Point { x: 0, y: 0, z: 0 };

match origin {
    Point { x,.. } => println!("x es {x}"),
}
```

Lista 18-23: Ignorar todos los campos de un `Point` excepto `x` usando `..`

Listamos el valor de `x` y luego simplemente incluimos el patrón `..`. Esto es más rápido que tener que listar `y: _` y `z: _`, especialmente cuando estamos trabajando con structs que tienen muchos campos en situaciones donde solo uno o dos campos son relevantes.

La sintaxis `..` se expandirá a tantos valores como sea necesario. La Lista 18-24 muestra cómo usar `..` con una tupla.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (first,.., last) => {
            println!("Algunos números: {first}, {last}");
        }
    }
}
```

Lista 18-24: Coincidir solo con los primeros y últimos valores en una tupla e ignorar todos los demás valores

En este código, los primeros y últimos valores se coinciden con `first` y `last`. El `..` coincidirá e ignorará todo lo que está en el medio.

Sin embargo, usar `..` debe ser inequívoco. Si no es claro qué valores se pretenden coincidir y cuáles deben ser ignorados, Rust nos dará un error. La Lista 18-25 muestra un ejemplo de usar `..` de manera ambigua, por lo que no se compilará.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        (.., second,..) => {
            println!("Algunos números: {second}");
        },
    }
}
```

Lista 18-25: Un intento de usar `..` de manera ambigua

Cuando compilamos este ejemplo, obtenemos este error:

```bash
error: `..` solo se puede usar una vez por patrón de tupla
 --> src/main.rs:5:22
  |
5 |         (.., second,..) => {
  |          --          ^^ solo se puede usar una vez por patrón de tupla
  |          |
  |          previamente usado aquí
```

Es imposible para Rust determinar cuántos valores de la tupla se deben ignorar antes de coincidir un valor con `second` y luego cuántos valores adicionales se deben ignorar después. Este código podría significar que queremos ignorar `2`, enlazar `second` a `4` y luego ignorar `8`, `16` y `32`; o que queremos ignorar `2` y `4`, enlazar `second` a `8` y luego ignorar `16` y `32`; y así sucesivamente. El nombre de variable `second` no significa nada especial para Rust, por lo que obtenemos un error del compilador porque usar `..` en dos lugares como este es ambiguo.
