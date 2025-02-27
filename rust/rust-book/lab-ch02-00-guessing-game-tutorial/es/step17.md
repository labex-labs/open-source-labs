# Manejo de entrada no válida

Para mejorar aún más el comportamiento del juego, en lugar de detener el programa cuando el usuario ingresa un valor no numérico, hagamos que el juego ignore ese valor no numérico para que el usuario pueda seguir adivinando. Podemos hacer eso modificando la línea donde `guess` se convierte de una `String` a un `u32`, como se muestra en la Lista 2-5.

Nombre del archivo: `src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Falló al leer la línea");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("Has adivinado: {guess}");

--snip--
```

Lista 2-5: Ignorar una suposición no numérica y pedir otra suposición en lugar de detener el programa

Cambiamos de una llamada a `expect` a una expresión `match` para pasar de detener el programa en caso de error a manejar el error. Recuerde que `parse` devuelve un tipo `Result` y `Result` es un enum que tiene las variantes `Ok` y `Err`. Estamos usando una expresión `match` aquí, como lo hicimos con el resultado `Ordering` del método `cmp`.

Si `parse` puede convertir correctamente la cadena en un número, devolverá un valor `Ok` que contiene el número resultante. Ese valor `Ok` coincidirá con el patrón del primer brazo, y la expresión `match` simplemente devolverá el valor `num` que `parse` produjo y puso dentro del valor `Ok`. Ese número terminará exactamente donde queremos en la nueva variable `guess` que estamos creando.

Si `parse` _no_ puede convertir la cadena en un número, devolverá un valor `Err` que contiene más información sobre el error. El valor `Err` no coincide con el patrón `Ok(num)` en el primer brazo de `match`, pero coincide con el patrón `Err(_)` en el segundo brazo. El guión bajo, `_`, es un valor genérico; en este ejemplo, estamos diciendo que queremos coincidir con todos los valores `Err`, sin importar qué información tengan dentro. Entonces el programa ejecutará el código del segundo brazo, `continue`, que le dice al programa que vaya a la siguiente iteración del `loop` y pida otra suposición. Entonces, en efecto, el programa ignora todos los errores que `parse` podría encontrar ¡

Ahora todo en el programa debería funcionar como se espera. Intentemoslo:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Adivina el número!
El número secreto es: 61
Por favor, ingresa tu suposición.
10
Has adivinado: 10
Demasiado pequeño!
Por favor, ingresa tu suposición.
99
Has adivinado: 99
Demasiado grande!
Por favor, ingresa tu suposición.
foo
Por favor, ingresa tu suposición.
61
Has adivinado: 61
¡Ganaste!
```

¡Genial! Con un pequeño ajuste final, terminaremos el juego de adivinanza. Recuerde que el programa todavía está imprimiendo el número secreto. Eso funcionó bien para probar, pero arruina el juego. Vamos a eliminar la `println!` que imprime el número secreto. La Lista 2-6 muestra el código final.

Nombre del archivo: `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Adivina el número!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Por favor, ingresa tu suposición.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Falló al leer la línea");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Has adivinado: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Demasiado pequeño!"),
            Ordering::Greater => println!("Demasiado grande!"),
            Ordering::Equal => {
                println!("¡Ganaste!");
                break;
            }
        }
    }
}
```

Lista 2-6: Código completo del juego de adivinanza

En este punto, ha construido con éxito el juego de adivinanza. ¡Felicitaciones!
