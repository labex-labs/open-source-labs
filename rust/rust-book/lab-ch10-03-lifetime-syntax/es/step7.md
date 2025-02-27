# Pensando en términos de lifetimes

La forma en que se deben especificar los parámetros de lifetime depende de lo que hace su función. Por ejemplo, si cambiamos la implementación de la función `longest` para siempre devolver el primer parámetro en lugar del trozo de cadena más largo, no necesitaríamos especificar un lifetime en el parámetro `y`. El siguiente código se compilará:

Nombre de archivo: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

Hemos especificado un parámetro de lifetime `'a` para el parámetro `x` y el tipo de retorno, pero no para el parámetro `y`, porque el lifetime de `y` no tiene ninguna relación con el lifetime de `x` o el valor de retorno.

Cuando se devuelve una referencia desde una función, el parámetro de lifetime para el tipo de retorno debe coincidir con el parámetro de lifetime de uno de los parámetros. Si la referencia devuelta _no_ se refiere a uno de los parámetros, debe referirse a un valor creado dentro de esta función. Sin embargo, esto sería una referencia colgante porque el valor saldrá de ámbito al final de la función. Considere esta implementación intentada de la función `longest` que no se compilará:

Nombre de archivo: `src/main.rs`

```rust
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

Aquí, aunque hemos especificado un parámetro de lifetime `'a` para el tipo de retorno, esta implementación no se compilará porque el lifetime del valor de retorno no está relacionado con el lifetime de los parámetros en absoluto. Aquí está el mensaje de error que obtenemos:

```bash
error[E0515]: cannot return reference to local variable `result`
  --> src/main.rs:11:5
   |
11 |     result.as_str()
   |     ^^^^^^^^^^^^^^^ returns a reference to data owned by the
current function
```

El problema es que `result` sale de ámbito y se limpia al final de la función `longest`. También estamos intentando devolver una referencia a `result` desde la función. No hay forma de que podamos especificar parámetros de lifetime que cambiarían la referencia colgante, y Rust no nos permitirá crear una referencia colgante. En este caso, la mejor solución sería devolver un tipo de datos con propiedad en lugar de una referencia para que la función llamante sea responsable de limpiar el valor.

En última instancia, la sintaxis de lifetime es sobre conectar los lifetimes de varios parámetros y valores de retorno de funciones. Una vez que están conectados, Rust tiene suficiente información para permitir operaciones seguras de memoria y no permitir operaciones que crearían punteros colgantes o que de otra manera violarían la seguridad de memoria.
