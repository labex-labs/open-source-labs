# Accediendo a los caracteres individuales de una cadena

En muchos otros lenguajes de programación, acceder a los caracteres individuales de una cadena mediante su índice es una operación válida y común. Sin embargo, si intentas acceder a partes de una `String` usando la sintaxis de índice en Rust, obtendrás un error. Considere el código no válido de la Lista 8-19.

```rust
let s1 = String::from("hello");
let h = s1[0];
```

Lista 8-19: Intentando usar la sintaxis de índice con una `String`

Este código generará el siguiente error:

```bash
error[E0277]: el tipo `String` no puede ser indexado por `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` no puede ser indexado por `{integer}`
  |
  = ayuda: el trato `Index<{integer}>` no está implementado para
`String`
```

El error y la nota cuentan la historia: las cadenas de Rust no admiten indexación. Pero, ¿por qué no? Para responder a esa pregunta, necesitamos discutir cómo Rust almacena las cadenas en memoria.
