# Crear tipos personalizados para validación

Vamos a llevar la idea de utilizar el sistema de tipos de Rust para asegurarnos de tener un valor válido un paso más allá y ver cómo crear un tipo personalizado para validación. Recuerda el juego de adivinanzas del Capítulo 2 en el que nuestro código preguntaba al usuario que adivinara un número entre 1 y 100. Nunca validamos que la suposición del usuario estuviera entre esos números antes de comprobarla contra nuestro número secreto; solo validamos que la suposición era positiva. En este caso, las consecuencias no eran muy graves: nuestra salida de "Demasiado alto" o "Demasiado bajo" todavía sería correcta. Pero sería una mejora útil para guiar al usuario hacia suposiciones válidas y tener un comportamiento diferente cuando el usuario adivina un número fuera de rango en comparación con cuando el usuario escribe, por ejemplo, letras en lugar de números.

Una forma de hacer esto sería analizar la suposición como un `i32` en lugar de solo un `u32` para permitir números potencialmente negativos, y luego agregar una comprobación para que el número esté en el rango, como sigue:

Nombre de archivo: `src/main.rs`

```rust
loop {
    --snip--

    let guess: i32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => continue,
    };

    if guess < 1 || guess > 100 {
        println!("El número secreto estará entre 1 y 100.");
        continue;
    }

    match guess.cmp(&secret_number) {
        --snip--
}
```

La expresión `if` comprueba si nuestro valor está fuera de rango, le informa al usuario sobre el problema y llama a `continue` para iniciar la siguiente iteración del bucle y pedir otra suposición. Después de la expresión `if`, podemos continuar con las comparaciones entre `guess` y el número secreto sabiendo que `guess` está entre 1 y 100.

Sin embargo, esta no es una solución ideal: si fuera absolutamente crítico que el programa solo operara con valores entre 1 y 100, y tuviera muchas funciones con este requisito, tener una comprobación como esta en cada función sería tediosa (y podría afectar el rendimiento).

En lugar de eso, podemos crear un nuevo tipo y poner las validaciones en una función para crear una instancia del tipo en lugar de repetir las validaciones en todos lados. De esa manera, es seguro para las funciones utilizar el nuevo tipo en sus firmas y utilizar con confianza los valores que reciben. La Lista 9-13 muestra una forma de definir un tipo `Guess` que solo creará una instancia de `Guess` si la función `new` recibe un valor entre 1 y 100.

Nombre de archivo: `src/lib.rs`

```rust
1 pub struct Guess {
    value: i32,
}

impl Guess {
  2 pub fn new(value: i32) -> Guess {
      3 if value < 1 || value > 100 {
          4 panic!(
                "El valor de la suposición debe estar entre 1 y 100, se obtuvo {}.",
                value
            );
        }

      5 Guess { value }
    }

  6 pub fn value(&self) -> i32 {
        self.value
    }
}
```

Lista 9-13: Un tipo `Guess` que solo continuará con valores entre 1 y 100

Primero definimos un struct llamado `Guess` que tiene un campo llamado `value` que almacena un `i32` \[1\]. Aquí es donde se almacenará el número.

Luego implementamos una función asociada llamada `new` en `Guess` que crea instancias de valores `Guess` \[2\]. La función `new` está definida para tener un parámetro llamado `value` de tipo `i32` y para devolver un `Guess`. El código en el cuerpo de la función `new` prueba `value` para asegurarse de que esté entre 1 y 100 \[3\]. Si `value` no pasa esta prueba, hacemos una llamada a `panic!` \[4\], lo que alertará al programador que está escribiendo el código llamador de que tiene un error que necesita corregir, porque crear un `Guess` con un `value` fuera de este rango violaría el contrato en el que se basa `Guess::new`. Las condiciones en las que `Guess::new` podría causar un bloqueo deben discutirse en su documentación de API pública; cubriremos las convenciones de documentación que indican la posibilidad de un `panic!` en la documentación de API que crees en el Capítulo 14. Si `value` pasa la prueba, creamos un nuevo `Guess` con su campo `value` establecido en el parámetro `value` y devolvemos el `Guess` \[5\].

A continuación, implementamos un método llamado `value` que presta `self`, no tiene ningún otro parámetro y devuelve un `i32` \[6\]. Este tipo de método a veces se llama _getter_ porque su propósito es obtener algunos datos de sus campos y devolverlos. Este método público es necesario porque el campo `value` del struct `Guess` es privado. Es importante que el campo `value` sea privado para que el código que utiliza el struct `Guess` no se permita establecer `value` directamente: el código fuera del módulo _debe_ utilizar la función `Guess::new` para crear una instancia de `Guess`, lo que garantiza que no hay forma de que un `Guess` tenga un `value` que no haya sido comprobado por las condiciones en la función `Guess::new`.

Una función que tiene un parámetro o devuelve solo números entre 1 y 100 podría entonces declarar en su firma que toma o devuelve un `Guess` en lugar de un `i32` y no necesitaría hacer ninguna comprobación adicional en su cuerpo.
