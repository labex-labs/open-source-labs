# Manejando posibles errores con Result

Todavía estamos trabajando en esta línea de código. Ahora estamos discutiendo una tercera línea de texto, pero ten en cuenta que todavía es parte de una sola línea lógica de código. La siguiente parte es este método:

```rust
.expect("Failed to read line");
```

Podríamos haber escrito este código como:

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

Sin embargo, una línea larga es difícil de leer, por lo que es mejor dividirla. A menudo es prudente introducir un salto de línea y otros espacios en blanco para ayudar a dividir las líneas largas cuando llamas a un método con la sintaxis `.method_name()`. Ahora vamos a discutir lo que hace esta línea.

Como se mencionó anteriormente, `read_line` coloca lo que el usuario ingresa en la cadena que le pasamos, pero también devuelve un valor de tipo `Result`. `Result` es una _enumeración_, a menudo llamada _enum_, que es un tipo que puede estar en uno de varios posibles estados. Llamamos a cada estado posible una _variante_.

El Capítulo 6 cubrirá los enums con más detalle. El propósito de estos tipos `Result` es codificar información de manejo de errores.

Las variantes de `Result` son `Ok` y `Err`. La variante `Ok` indica que la operación tuvo éxito, y dentro de `Ok` está el valor generado con éxito. La variante `Err` significa que la operación falló, y `Err` contiene información sobre cómo o por qué la operación falló.

Los valores del tipo `Result`, al igual que los valores de cualquier tipo, tienen métodos definidos en ellos. Una instancia de `Result` tiene un método `expect` que puedes llamar. Si esta instancia de `Result` es un valor `Err`, `expect` hará que el programa se detenga y muestre el mensaje que le pasaste como argumento a `expect`. Si el método `read_line` devuelve un `Err`, probablemente sea el resultado de un error proveniente del sistema operativo subyacente. Si esta instancia de `Result` es un valor `Ok`, `expect` tomará el valor de retorno que está almacenando `Ok` y te devolverá solo ese valor para que puedas usarlo. En este caso, ese valor es el número de bytes de la entrada del usuario.

Si no llamas a `expect`, el programa se compilará, pero recibirás una advertencia:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust advierte que no has usado el valor `Result` devuelto por `read_line`, lo que indica que el programa no ha manejado un posible error.

La forma correcta de suprimir la advertencia es escribir realmente código de manejo de errores, pero en nuestro caso solo queremos detener este programa cuando ocurra un problema, por lo que podemos usar `expect`. Aprenderás sobre cómo recuperarse de errores en el Capítulo 9.
