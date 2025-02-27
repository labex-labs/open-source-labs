# Generando un número aleatorio

Comencemos a usar `rand` para generar un número que se tenga que adivinar. El siguiente paso es actualizar `src/main.rs`, como se muestra en la Lista 2-3.

Nombre del archivo: `src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Adivina el número!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("El número secreto es: {secret_number}");

    println!("Por favor, ingresa tu suposición.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Falló al leer la línea");

    println!("Has adivinado: {guess}");
}
```

Lista 2-3: Agregando código para generar un número aleatorio

Primero agregamos la línea `use rand::Rng;` \[1\]. El trato `Rng` define métodos que los generadores de números aleatorios implementan, y este trato debe estar en ámbito para que podamos usar esos métodos. El Capítulo 10 cubrirá los tratados en detalle.

Luego, estamos agregando dos líneas en el medio. En la primera línea \[2\], llamamos a la función `rand::thread_rng` que nos da el generador de números aleatorios particular que vamos a usar: uno que es local al hilo de ejecución actual y está sembrado por el sistema operativo. Luego llamamos al método `gen_range` en el generador de números aleatorios. Este método está definido por el trato `Rng` que trajimos al ámbito con la declaración `use rand::Rng;`. El método `gen_range` toma una expresión de rango como argumento y genera un número aleatorio en el rango. El tipo de expresión de rango que estamos usando aquí tiene la forma `start..=end` y es inclusiva en los límites inferior y superior, por lo que necesitamos especificar `1..=100` para solicitar un número entre 1 y 100.

> Nota: No sabrás solo qué tratados usar y qué métodos y funciones llamar de un crado, por lo que cada crado tiene documentación con instrucciones para usarlo. Otra característica genial de Cargo es que ejecutar el comando `cargo doc --open` construirá la documentación proporcionada por todas tus dependencias localmente y la abrirá en tu navegador. Si estás interesado en otra funcionalidad en el crado `rand`, por ejemplo, ejecuta `cargo doc --open` y haz clic en `rand` en la barra lateral izquierda.

La segunda línea nueva \[3\] imprime el número secreto. Esto es útil mientras desarrollamos el programa para poder probarlo, pero lo eliminaremos de la versión final. No es mucho de un juego si el programa imprime la respuesta tan pronto como comienza!

Intenta ejecutar el programa varias veces:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Adivina el número!
El número secreto es: 7
Por favor, ingresa tu suposición.
4
Has adivinado: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Adivina el número!
El número secreto es: 83
Por favor, ingresa tu suposición.
5
Has adivinado: 5
```

Deberías obtener números aleatorios diferentes, y todos deberían ser números entre 1 y 100. ¡Excelente trabajo!
