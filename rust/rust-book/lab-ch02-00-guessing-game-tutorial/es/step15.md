# Permitiendo múltiples suposiciones con bucles

La palabra clave `loop` crea un bucle infinito. Agregaremos un bucle para dar a los usuarios más oportunidades de adivinar el número:

Nombre del archivo: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Adivina el número!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("El número secreto es: {secret_number}");

    loop {
        println!("Por favor, ingresa tu suposición.");
        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Falló al leer la línea");

        let guess: u32 = guess
         .trim()
         .parse()
         .expect("Por favor, escribe un número!");

        println!("Has adivinado: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Demasiado pequeño!"),
            Ordering::Greater => println!("Demasiado grande!"),
            Ordering::Equal => println!("¡Ganaste!"),
        }
    }
}
```

Como puede ver, hemos movido todo desde el prompt de entrada de la suposición en adelante dentro de un bucle. Asegúrese de indentar las líneas dentro del bucle con otras cuatro espacios cada una y ejecutar el programa nuevamente. El programa ahora pedirá otra suposición para siempre, lo que en realidad introduce un nuevo problema. Parece que el usuario no puede salir ¡

El usuario siempre podría interrumpir el programa usando el atajo de teclado ctrl-C. Pero hay otra forma de escapar de este monstruo insaciable, como se mencionó en la discusión de `parse` en "Comparando la suposición con el número secreto": si el usuario ingresa una respuesta no numérica, el programa se detendrá. Podemos aprovechar eso para permitir que el usuario salga, como se muestra aquí:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Adivina el número!
El número secreto es: 59
Por favor, ingresa tu suposición.
45
Has adivinado: 45
Demasiado pequeño!
Por favor, ingresa tu suposición.
60
Has adivinado: 60
Demasiado grande!
Por favor, ingresa tu suposición.
59
Has adivinado: 59
¡Ganaste!
Por favor, ingresa tu suposición.
quit
thread 'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Escribir `quit` cerrará el juego, pero como notará, también lo hará ingresando cualquier otra entrada no numérica. Esto es subóptimo, por decir lo menos; queremos que el juego también se detenga cuando se adivina el número correcto.
