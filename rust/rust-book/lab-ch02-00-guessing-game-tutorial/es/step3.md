# Procesando una suposición

La primera parte del programa del juego de adivinanza solicitará la entrada del usuario, procesará esa entrada y comprobará que la entrada tenga el formato esperado. Para comenzar, permitiremos que el jugador ingrese una suposición. Ingresa el código de la Lista 2-1 en `src/main.rs`.

Nombre del archivo: `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Adivina el número!");

    println!("Por favor, ingresa tu suposición.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Falló al leer la línea");

    println!("Has adivinado: {guess}");
}
```

Lista 2-1: Código que obtiene una suposición del usuario y la imprime

Este código contiene mucha información, así que repasemoslo línea por línea. Para obtener la entrada del usuario y luego imprimir el resultado como salida, necesitamos traer la librería de entrada/salida `io` al ámbito. La librería `io` proviene de la librería estándar, conocida como `std`:

```rust
use std::io;
```

Por defecto, Rust tiene un conjunto de elementos definidos en la librería estándar que trae al ámbito de cada programa. Este conjunto se llama _preámbulo_, y puedes ver todo lo que contiene en *https://doc.rust-lang.org/std/prelude/index.html*.

Si un tipo que quieres usar no está en el preámbulo, debes traer ese tipo al ámbito explícitamente con una declaración `use`. Usar la librería `std::io` te proporciona una serie de características útiles, incluyendo la capacidad de aceptar la entrada del usuario.

Como viste en el Capítulo 1, la función `main` es el punto de entrada del programa:

```rust
fn main() {
```

La sintaxis `fn` declara una nueva función; los paréntesis, `()`, indican que no hay parámetros; y la llave curva, `{`, inicia el cuerpo de la función.

Como también aprendiste en el Capítulo 1, `println!` es una macro que imprime una cadena en la pantalla:

```rust
println!("Adivina el número!");

println!("Por favor, ingresa tu suposición.");
```

Este código está imprimiendo un mensaje de solicitud que indica de qué se trata el juego y solicita la entrada del usuario.
