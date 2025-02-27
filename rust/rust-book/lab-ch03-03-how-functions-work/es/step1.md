# Funciones

Las funciones son muy comunes en el código de Rust. Ya has visto una de las funciones más importantes del lenguaje: la función `main`, que es el punto de entrada de muchos programas. Has visto también la palabra clave `fn`, que te permite declarar nuevas funciones.

Crea un nuevo proyecto llamado `functions`:

```bash
cargo new functions
cd functions
```

El código de Rust utiliza el _snake case_ como el estilo convencional para los nombres de funciones y variables, en el que todas las letras son minúsculas y los guiones bajos separan las palabras. Aquí hay un programa que contiene una definición de función de ejemplo:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Definimos una función en Rust escribiendo `fn` seguido del nombre de la función y un par de paréntesis. Las llaves indican al compilador dónde comienza y termina el cuerpo de la función.

Podemos llamar a cualquier función que hayamos definido escribiendo su nombre seguido de un par de paréntesis. Dado que `another_function` está definida en el programa, se puede llamar desde dentro de la función `main`. Observe que definimos `another_function` _después_ de la función `main` en el código fuente; también podríamos haberla definido antes. Rust no importa dónde defines tus funciones, solo que estén definidas en algún lugar de un ámbito que sea visible para el llamador.

Vamos a comenzar un nuevo proyecto binario llamado _functions_ para explorar las funciones más detenidamente. Coloca el ejemplo de `another_function` en `src/main.rs` y ejecútalo. Deberías ver la siguiente salida:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

Las líneas se ejecutan en el orden en que aparecen en la función `main`. Primero se imprime el mensaje "Hello, world!", y luego se llama a `another_function` y se imprime su mensaje.
