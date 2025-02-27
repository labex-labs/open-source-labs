# Variables y Mutabilidad

Como se mencionó en "Almacenar valores con variables", por defecto, las variables son inmutables. Esto es una de las muchas sugerencias que Rust te da para escribir tu código de manera que aproveche la seguridad y la fácil concurrencia que ofrece Rust. Sin embargo, todavía tienes la opción de hacer que tus variables sean mutables. Vamos a explorar cómo y por qué Rust te anima a favorecer la inmutabilidad y por qué a veces es posible que desees optar por la mutabilidad.

Cuando una variable es inmutable, una vez que un valor está vinculado a un nombre, no puedes cambiar ese valor. Para ilustrar esto, genera un nuevo proyecto llamado _variables_ en tu directorio `proyecto` usando `cargo new variables`.

Luego, en tu nuevo directorio `variables`, abre `src/main.rs` y reemplaza su código con el siguiente código, que todavía no se compilará:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("El valor de x es: {x}");
    x = 6;
    println!("El valor de x es: {x}");
}
```

Guarda y ejecuta el programa usando `cargo run`. Deberías recibir un mensaje de error sobre un error de inmutabilidad, como se muestra en esta salida:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: no se puede asignar dos veces a la variable inmutable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         primera asignación a `x`
  |         ayuda: considerar hacer este enlace mutable: `mut x`
3 |     println!("El valor de x es: {x}");
4 |     x = 6;
  |     ^^^^^ no se puede asignar dos veces a la variable inmutable
```

Este ejemplo muestra cómo el compilador te ayuda a encontrar errores en tus programas. Los errores del compilador pueden ser frustrantes, pero en realidad solo significan que tu programa no está haciendo lo que quieres de manera segura todavía; no significan que no seas un buen programador. Los Rustaceos experimentados todavía obtienen errores del compilador.

Recibiste el mensaje de error `no se puede asignar dos veces a la variable inmutable`x\``porque intentaste asignar un segundo valor a la variable inmutable`x\`.

Es importante que obtengamos errores en tiempo de compilación cuando intentamos cambiar un valor que se designa como inmutable porque esta situación puede conducir a errores. Si una parte de nuestro código opera con la suposición de que un valor nunca cambiará y otra parte de nuestro código cambia ese valor, es posible que la primera parte del código no haga lo que se diseñó para hacer. La causa de este tipo de error puede ser difícil de localizar después de los hechos, especialmente cuando la segunda parte del código cambia el valor solo _a veces_. El compilador de Rust garantiza que cuando dices que un valor no cambiará, realmente no cambiará, por lo que no tienes que preocuparte por ello. Tu código es por lo tanto más fácil de entender.

Pero la mutabilidad puede ser muy útil y puede hacer que el código sea más conveniente de escribir. Aunque las variables son inmutables por defecto, puedes hacerlas mutables agregando `mut` al frente del nombre de la variable, como lo hiciste en el Capítulo 2. Agregar `mut` también transmite el propósito a futuros lectores del código al indicar que otras partes del código cambiarán el valor de esta variable.

Por ejemplo, cambiemos `src/main.rs` al siguiente:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("El valor de x es: {x}");
    x = 6;
    println!("El valor de x es: {x}");
}
```

Cuando ejecutamos el programa ahora, obtenemos esto:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
El valor de x es: 5
El valor de x es: 6
```

Estamos permitidos cambiar el valor vinculado a `x` de `5` a `6` cuando se usa `mut`. En última instancia, decidir si usar mutabilidad o no depende de ti y depende de lo que consideres más claro en esa situación particular.
