# Referencias colgantes

En los lenguajes con punteros, es fácil crear erróneamente un _puntero colgante_ (un puntero que hace referencia a una ubicación en memoria que puede haber sido dada a alguien más) liberando alguna memoria mientras se conserva un puntero a esa memoria. En Rust, en cambio, el compilador garantiza que las referencias nunca serán referencias colgantes: si tienes una referencia a algunos datos, el compilador asegurará de que los datos no saldrán del ámbito antes de que la referencia a los datos lo haga.

Intentemos crear una referencia colgante para ver cómo Rust las previene con un error en tiempo de compilación:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Aquí está el error:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

Este mensaje de error se refiere a una característica que aún no hemos cubierto: los lifetimes. Discutiremos los lifetimes en detalle en el Capítulo 10. Pero, si ignores las partes sobre lifetimes, el mensaje contiene la clave de por qué este código es un problema:

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

Echemos un vistazo más detenido a exactamente lo que está sucediendo en cada etapa de nuestro código `dangle`:

    // src/main.rs
    fn dangle() -> &String { // dangle devuelve una referencia a una String

        let s = String::from("hello"); // s es una nueva String

        &s // devolvemos una referencia a la String, s
    } // Aquí, s sale del ámbito y se elimina, por lo que su memoria desaparece
      // ¡Peligro!

Debido a que `s` se crea dentro de `dangle`, cuando se termine el código de `dangle`, `s` se desasignará. Pero intentamos devolver una referencia a ella. Eso significa que esta referencia apuntaría a una `String` inválida. ¡Eso no es bueno! Rust no nos dejará hacer esto.

La solución aquí es devolver la `String` directamente:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

Esto funciona sin problemas. La posesión se mueve y nada se desasigna.
