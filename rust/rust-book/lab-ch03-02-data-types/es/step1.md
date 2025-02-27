# Tipos de Datos

Todo valor en Rust es de un cierto **tipo de datos**, que le dice a Rust qué tipo de datos se está especificando para que sepa cómo trabajar con esos datos. Veremos dos subconjuntos de tipos de datos: escalares y compuestos.

Tenga en cuenta que Rust es un lenguaje **fuertemente tipado**, lo que significa que debe conocer los tipos de todas las variables en tiempo de compilación. El compilador suele poder inferir qué tipo queremos usar basado en el valor y cómo lo usamos. En casos en los que son posibles muchos tipos, como cuando convertimos un `String` a un tipo numérico usando `parse` en "Comparando la suposición con el número secreto", debemos agregar una anotación de tipo, como esta:

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

Si no agregamos la anotación de tipo `: u32` mostrada en el código anterior, Rust mostrará el siguiente error, lo que significa que el compilador necesita más información de nosotros para saber qué tipo queremos usar:

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

Verá diferentes anotaciones de tipo para otros tipos de datos.
