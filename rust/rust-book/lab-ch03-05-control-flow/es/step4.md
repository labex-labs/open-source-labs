# Usando `if` en una declaración `let`

Debido a que `if` es una expresión, podemos utilizarla en el lado derecho de una declaración `let` para asignar el resultado a una variable, como en la Lista 3-2.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```

Lista 3-2: Asignando el resultado de una expresión `if` a una variable

La variable `number` se vinculará a un valor basado en el resultado de la expresión `if`. Ejecute este código para ver qué sucede:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
The value of number is: 5
```

Recuerde que los bloques de código se evalúan al último expresión en ellos, y los números por sí mismos también son expresiones. En este caso, el valor de la expresión `if` completa depende de qué bloque de código se ejecuta. Esto significa que los valores que tienen el potencial de ser resultados de cada rama de la `if` deben ser del mismo tipo; en la Lista 3-2, los resultados de la rama `if` y la rama `else` eran enteros `i32`. Si los tipos no coinciden, como en el siguiente ejemplo, obtendremos un error:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

Cuando intentamos compilar este código, obtendremos un error. Las ramas `if` y `else` tienen tipos de valores incompatibles, y Rust indica exactamente dónde encontrar el problema en el programa:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: `if` and `else` have incompatible types
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ expected integer, found
`&str`
  |                                 |
  |                                 expected because of this
```

La expresión en el bloque `if` se evalúa a un entero, y la expresión en el bloque `else` se evalúa a una cadena. Esto no funcionará porque las variables deben tener un solo tipo, y Rust necesita saber en tiempo de compilación qué tipo es la variable `number`, de manera definitiva. Saber el tipo de `number` permite al compilador verificar que el tipo es válido en todas partes donde usamos `number`. Rust no podría hacer eso si el tipo de `number` solo se determinara en tiempo de ejecución; el compilador sería más complejo y ofrecería menos garantías sobre el código si tuviera que llevar un registro de múltiples tipos hipotéticamente para cualquier variable.
