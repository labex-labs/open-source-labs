# Funciones con valores de retorno

Las funciones pueden devolver valores al código que las llama. No nombramos los valores de retorno, pero debemos declarar su tipo después de una flecha (`->`). En Rust, el valor de retorno de una función es sinónimo del valor de la última expresión en el bloque del cuerpo de una función. Puedes retornar tempranamente desde una función usando la palabra clave `return` y especificando un valor, pero la mayoría de las funciones retornan la última expresión implícitamente. Aquí hay un ejemplo de una función que devuelve un valor:

Nombre del archivo: `src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

No hay llamadas a funciones, macros ni siquiera declaraciones `let` en la función `five`; solo el número `5` por sí mismo. Esa es una función perfectamente válida en Rust. Observe que también se especifica el tipo de retorno de la función, como `-> i32`. Intenta ejecutar este código; la salida debería verse así:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

El `5` en `five` es el valor de retorno de la función, por eso el tipo de retorno es `i32`. Vamos a examinar esto con más detalle. Hay dos aspectos importantes: primero, la línea `let x = five();` muestra que estamos usando el valor de retorno de una función para inicializar una variable. Debido a que la función `five` devuelve un `5`, esa línea es equivalente a la siguiente:

```rust
let x = 5;
```

Segundo, la función `five` no tiene parámetros y define el tipo del valor de retorno, pero el cuerpo de la función es un solo `5` sin punto y coma porque es una expresión cuyo valor queremos retornar.

Veamos otro ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

Ejecutar este código imprimirá `The value of x is: 6`. Pero si ponemos un punto y coma al final de la línea que contiene `x + 1`, cambiándola de una expresión a una declaración, obtendremos un error:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

Compilar este código produce un error, como sigue:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

El mensaje de error principal, `mismatched types`, revela el problema central de este código. La definición de la función `plus_one` dice que devolverá un `i32`, pero las declaraciones no se evalúan a un valor, lo que se expresa por `()`, el tipo unitario. Por lo tanto, no se devuelve nada, lo que contradice la definición de la función y da lugar a un error. En esta salida, Rust proporciona un mensaje que puede ayudar a corregir este problema: sugiere quitar el punto y coma, lo que solucionaría el error.
