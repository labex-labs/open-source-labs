# pointers/ref

Para los punteros, es necesario distinguir entre la desestructuración y la desreferenciación, ya que son conceptos diferentes que se usan de manera distinta a los lenguajes como C/C++.

- La desreferenciación utiliza `*`
- La desestructuración utiliza `&`, `ref` y `ref mut`

```rust
fn main() {
    // Asigna una referencia de tipo `i32`. El `&` significa que
    // se está asignando una referencia.
    let reference = &4;

    match reference {
        // Si `reference` se coincide con el patrón `&val`, se produce
        // una comparación como:
        // `&i32`
        // `&val`
        // ^ Vemos que si se eliminan los `&` coincidentes, entonces el `i32`
        // debe ser asignado a `val`.
        &val => println!("Got a value via destructuring: {:?}", val),
    }

    // Para evitar el `&`, se desreferencia antes de coincidir.
    match *reference {
        val => println!("Got a value via dereferencing: {:?}", val),
    }

    // ¿Qué pasa si no se comienza con una referencia? `reference` era un `&`
    // porque el lado derecho ya era una referencia. Esto no
    // es una referencia porque el lado derecho no lo es.
    let _not_a_reference = 3;

    // Rust proporciona `ref` precisamente para este propósito. Modifica la
    // asignación para que se cree una referencia para el elemento; esta
    // referencia se asigna.
    let ref _is_a_reference = 3;

    // En consecuencia, al definir 2 valores sin referencias, se pueden
    // recuperar referencias a través de `ref` y `ref mut`.
    let value = 5;
    let mut mut_value = 6;

    // Utiliza la palabra clave `ref` para crear una referencia.
    match value {
        ref r => println!("Got a reference to a value: {:?}", r),
    }

    // Utiliza `ref mut` de manera similar.
    match mut_value {
        ref mut m => {
            // Obtuvimos una referencia. Tenemos que desreferenciarla antes de poder
            // agregarle nada.
            *m += 10;
            println!("We added 10. `mut_value`: {:?}", m);
        },
    }
}
```
