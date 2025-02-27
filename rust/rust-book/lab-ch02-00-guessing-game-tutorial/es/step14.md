# Comparando la suposición con el número secreto

Ahora que tenemos la entrada del usuario y un número aleatorio, podemos compararlos. Ese paso se muestra en la Lista 2-4. Tenga en cuenta que este código todavía no se compilará, como se explicará.

Nombre del archivo: `src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("Has adivinado: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Demasiado pequeño!"),
        Ordering::Greater => println!("Demasiado grande!"),
        Ordering::Equal => println!("¡Ganaste!"),
    }
}
```

Lista 2-4: Manejar los posibles valores de retorno de la comparación de dos números

Primero agregamos otra declaración `use` \[1\], trayendo un tipo llamado `std::cmp::Ordering` al ámbito desde la biblioteca estándar. El tipo `Ordering` es otro enum y tiene las variantes `Less`, `Greater` y `Equal`. Estos son los tres resultados posibles cuando se comparan dos valores.

Luego agregamos cinco líneas nuevas al final que usan el tipo `Ordering`. El método `cmp` \[3\] compara dos valores y se puede llamar en cualquier cosa que se pueda comparar. Toma una referencia a lo que quieres comparar: aquí está comparando `guess` con `secret_number`. Luego devuelve una variante del enum `Ordering` que trajimos al ámbito con la declaración `use`. Usamos una expresión `match` \[2\] para decidir qué hacer a continuación basado en qué variante de `Ordering` se devolvió desde la llamada a `cmp` con los valores en `guess` y `secret_number`.

Una expresión `match` está compuesta por _ramas_. Una rama consta de un _patrón_ contra el que se debe coincidir, y el código que debe ejecutarse si el valor dado a `match` coincide con el patrón de esa rama. Rust toma el valor dado a `match` y lo revisa en cada patrón de rama por turnos. Los patrones y la construcción `match` son características poderosas de Rust: te permiten expresar una variedad de situaciones que tu código podría encontrar y te aseguran que las manejes todas. Estas características se cubrirán en detalle en el Capítulo 6 y el Capítulo 18, respectivamente.

Veamos un ejemplo con la expresión `match` que usamos aquí. Digamos que el usuario ha adivinado 50 y el número secreto generado aleatoriamente esta vez es 38.

Cuando el código compara 50 con 38, el método `cmp` devolverá `Ordering::Greater` porque 50 es mayor que 38. La expresión `match` obtiene el valor `Ordering::Greater` y comienza a revisar cada patrón de rama. Mira el patrón de la primera rama, `Ordering::Less`, y ve que el valor `Ordering::Greater` no coincide con `Ordering::Less`, por lo que ignora el código en esa rama y pasa a la siguiente rama. El patrón de la siguiente rama es `Ordering::Greater`, que _sí_ coincide con `Ordering::Greater` ¡El código asociado a esa rama se ejecutará y imprimirá `Demasiado grande!` en la pantalla. La expresión `match` termina después de la primera coincidencia exitosa, por lo que no revisará la última rama en este escenario.

Sin embargo, el código en la Lista 2-4 todavía no se compilará. Intentemoslo:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: tipos no coincidentes
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ se esperaba struct `String`, encontrado integer
   |
   = nota: se esperaba referencia `&String`
              se encontró referencia `&{integer}`
```

El núcleo del error indica que hay _tipos no coincidentes_. Rust tiene un sistema de tipos estático fuerte. Sin embargo, también tiene inferencia de tipos. Cuando escribimos `let mut guess = String::new()`, Rust pudo inferir que `guess` debería ser un `String` y no nos hizo escribir el tipo. Por otro lado, `secret_number` es un tipo numérico. Algunos de los tipos numéricos de Rust pueden tener un valor entre 1 y 100: `i32`, un número de 32 bits; `u32`, un número sin signo de 32 bits; `i64`, un número de 64 bits; así como otros. A menos que se especifique lo contrario, Rust por defecto es un `i32`, que es el tipo de `secret_number` a menos que agregues información de tipo en otro lugar que haga que Rust infiera un tipo numérico diferente. La razón del error es que Rust no puede comparar una cadena y un tipo numérico.

En última instancia, queremos convertir la `String` que el programa lee como entrada en un tipo numérico real para que podamos compararla numéricamente con el número secreto. Lo hacemos agregando esta línea al cuerpo de la función `main`:

Nombre del archivo: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Adivina el número!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("El número secreto es: {secret_number}");

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
```

Creamos una variable llamada `guess`. Pero espera, ¿no tiene el programa ya una variable llamada `guess`? Lo tiene, pero afortunadamente Rust permite que sobrescribamos el valor anterior de `guess` con uno nuevo. El _sobreescritura_ nos permite reutilizar el nombre de variable `guess` en lugar de obligarnos a crear dos variables únicas, como `guess_str` y `guess`, por ejemplo. Cubriremos esto con más detalle en el Capítulo 3, pero por ahora, sabe que esta característica se usa a menudo cuando quieres convertir un valor de un tipo a otro tipo.

Asociamos esta nueva variable a la expresión `guess.trim().parse()`. La `guess` en la expresión se refiere a la variable original `guess` que contenía la entrada como una cadena. El método `trim` en una instancia de `String` eliminará cualquier espacio en blanco al principio y al final, lo que debemos hacer para poder comparar la cadena con el `u32`, que solo puede contener datos numéricos. El usuario debe presionar enter para satisfacer `read_line` e ingresar su suposición, lo que agrega un carácter de nueva línea a la cadena. Por ejemplo, si el usuario escribe `5` y presiona enter, `guess` se ve así: `5\n`. El `\n` representa "nueva línea". (En Windows, presionar enter resulta en un retorno de carro y una nueva línea, `\r\n`.) El método `trim` elimina `\n` o `\r\n`, resultando en solo `5`.

El método `parse` en cadenas convierte una cadena a otro tipo. Aquí, lo usamos para convertir de una cadena a un número. Necesitamos decirle a Rust el tipo numérico exacto que queremos usando `let guess: u32`. El dos puntos (`:`) después de `guess` le dice a Rust que anotaremos el tipo de la variable. Rust tiene algunos tipos numéricos integrados; el `u32` que se ve aquí es un entero sin signo de 32 bits. Es una buena opción predeterminada para un número positivo pequeño. Aprenderás sobre otros tipos numéricos en el Capítulo 3.

Además, la anotación `u32` en este programa de ejemplo y la comparación con `secret_number` significa que Rust inferirá que `secret_number` también debería ser un `u32`. Entonces, ahora la comparación será entre dos valores del mismo tipo ¡

El método `parse` solo funcionará en caracteres que se pueden convertir lógicamente en números y, por lo tanto, puede causar fácilmente errores. Si, por ejemplo, la cadena contuviera `A`👍`%`, no habría forma de convertir eso en un número. Debido a que podría fallar, el método `parse` devuelve un tipo `Result`, al igual que el método `read_line` (discutido anteriormente en "Manejar el fracaso potencial con Result"). Vamos a tratar este `Result` de la misma manera usando el método `expect` nuevamente. Si `parse` devuelve una variante `Err` de `Result` porque no pudo crear un número a partir de la cadena, la llamada a `expect` detendrá el juego y imprimirá el mensaje que le demos. Si `parse` puede convertir correctamente la cadena a un número, devolverá la variante `Ok` de `Result`, y `expect` devolverá el número que queremos del valor `Ok`.

Ahora ejecutemos el programa:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Adivina el número!
El número secreto es: 58
Por favor, ingresa tu suposición.
  76
Has adivinado: 76
Demasiado grande!
```

¡Genial! Aunque se agregaron espacios antes de la suposición, el programa todavía pudo determinar que el usuario adivinó 76. Ejecute el programa varias veces para verificar el comportamiento diferente con diferentes tipos de entrada: adivine el número correctamente, adivine un número que sea demasiado alto y adivine un número que sea demasiado bajo.

Ya tenemos la mayor parte del juego funcionando, pero el usuario solo puede hacer una suposición. Cambiemos eso agregando un bucle ¡
