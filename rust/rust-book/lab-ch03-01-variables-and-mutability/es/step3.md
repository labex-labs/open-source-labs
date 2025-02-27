# Sombreado

Como viste en el tutorial del juego de adivinanza del Capítulo 2, puedes declarar una nueva variable con el mismo nombre que una variable anterior. Los Rustaceans dicen que la primera variable es _sombreada_ por la segunda, lo que significa que la segunda variable es lo que el compilador verá cuando uses el nombre de la variable. En efecto, la segunda variable sombreada la primera, tomando cualquier uso del nombre de la variable para sí misma hasta que ya sea ella misma sombreada o el ámbito termine. Podemos sombrear una variable usando el mismo nombre de la variable y repitiendo el uso de la palabra clave `let` de la siguiente manera:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("El valor de x en el ámbito interno es: {x}");
    }

    println!("El valor de x es: {x}");
}
```

Este programa primero asocia `x` a un valor de `5`. Luego crea una nueva variable `x` repitiendo `let x =`, tomando el valor original y sumando `1` para que el valor de `x` sea entonces `6`. Luego, dentro de un ámbito interno creado con llaves, la tercera declaración `let` también sombrea `x` y crea una nueva variable, multiplicando el valor anterior por `2` para dar a `x` un valor de `12`. Cuando ese ámbito finaliza, el sombreado interno termina y `x` vuelve a ser `6`. Cuando ejecutamos este programa, se mostrará lo siguiente:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
El valor de x en el ámbito interno es: 12
El valor de x es: 6
```

El sombreado es diferente de marcar una variable como `mut` porque obtendremos un error en tiempo de compilación si accidentalmente intentamos volver a asignar a esta variable sin usar la palabra clave `let`. Al usar `let`, podemos realizar algunas transformaciones en un valor pero que la variable sea inmutable después de que se hayan completado esas transformaciones.

La otra diferencia entre `mut` y el sombreado es que, ya que estamos efectivamente creando una nueva variable cuando usamos de nuevo la palabra clave `let`, podemos cambiar el tipo del valor pero reutilizar el mismo nombre. Por ejemplo, digamos que nuestro programa le pide a un usuario que muestre cuántos espacios quiere entre algunos textos ingresando caracteres de espacio, y luego queremos almacenar esa entrada como un número:

```rust
let spaces = "   ";
let spaces = spaces.len();
```

La primera variable `spaces` es de tipo cadena y la segunda variable `spaces` es de tipo número. El sombreado así nos ahorra tener que inventar diferentes nombres, como `spaces_str` y `spaces_num`; en cambio, podemos reutilizar el nombre más simple `spaces`. Sin embargo, si intentamos usar `mut` para esto, como se muestra aquí, obtendremos un error en tiempo de compilación:

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

El error dice que no se nos permite mutar el tipo de una variable:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: tipos no coincidentes
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- debido a este valor se esperaba
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ esperado `&str`, encontrado `usize`
```

Ahora que hemos explorado cómo funcionan las variables, veamos más tipos de datos que pueden tener.
