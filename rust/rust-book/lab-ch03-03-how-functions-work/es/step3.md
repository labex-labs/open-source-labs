# Declaraciones y expresiones

Los cuerpos de las funciones están compuestos por una serie de declaraciones que, opcionalmente, terminan en una expresión. Hasta ahora, las funciones que hemos visto no han incluido una expresión final, pero has visto una expresión como parte de una declaración. Debido a que Rust es un lenguaje basado en expresiones, esta es una distinción importante de entender. Otros lenguajes no tienen las mismas distinciones, así que veamos qué son las declaraciones y las expresiones y cómo sus diferencias afectan los cuerpos de las funciones.

- **Declaraciones**: son instrucciones que realizan alguna acción y no devuelven un valor.
- **Expresiones**: se evalúan a un valor resultante. Echemos un vistazo a algunos ejemplos.

En realidad, ya hemos utilizado declaraciones y expresiones. Crear una variable y asignarle un valor con la palabra clave `let` es una declaración. En la Lista 3-1, `let y = 6;` es una declaración.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

Lista 3-1: Una declaración de función `main` que contiene una declaración

Las definiciones de funciones también son declaraciones; el ejemplo completo anterior es una declaración en sí misma.

Las declaraciones no devuelven valores. Por lo tanto, no puedes asignar una declaración `let` a otra variable, como intenta hacer el siguiente código; obtendrás un error:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

Cuando ejecutas este programa, el error que obtendrás se parece a esto:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

La declaración `let y = 6` no devuelve un valor, por lo que no hay nada a lo que `x` pueda enlazarse. Esto es diferente de lo que sucede en otros lenguajes, como C y Ruby, donde la asignación devuelve el valor de la asignación. En esos lenguajes, puedes escribir `x = y = 6` y que tanto `x` como `y` tengan el valor `6`; eso no es así en Rust.

Las expresiones se evalúan a un valor y forman la mayor parte del resto del código que escribirás en Rust. Considera una operación matemática, como `5 + 6`, que es una expresión que se evalúa al valor `11`. Las expresiones pueden ser parte de declaraciones: en la Lista 3-1, el `6` en la declaración `let y = 6;` es una expresión que se evalúa al valor `6`. Llamar a una función es una expresión. Llamar a una macro es una expresión. Un nuevo bloque de ámbito creado con llaves es una expresión, por ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

La expresión \[2\] es un bloque que, en este caso, se evalúa a `4`. Ese valor se enlaza a `y` como parte de la declaración `let` \[1\]. Observe la línea sin punto y coma al final \[3\], que es diferente de la mayoría de las líneas que has visto hasta ahora. Las expresiones no incluyen punto y coma al final. Si agregas un punto y coma al final de una expresión, la conviertes en una declaración y entonces no devolverá un valor. Tien esto en cuenta cuando explores los valores de retorno de funciones y expresiones a continuación.
