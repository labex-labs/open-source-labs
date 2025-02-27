# Bucle a través de una colección con `for`

Puedes elegir usar la construcción `while` para iterar sobre los elementos de una colección, como una matriz. Por ejemplo, el bucle en la Lista 3-4 imprime cada elemento de la matriz `a`.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```

Lista 3-4: Iterando a través de cada elemento de una colección usando un bucle `while`

Aquí, el código cuenta hacia arriba a través de los elementos de la matriz. Comienza en el índice `0`, y luego itera hasta llegar al último índice de la matriz (es decir, cuando `index < 5` ya no es `true`). Ejecutar este código imprimirá cada elemento de la matriz:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32s
     Running `target/debug/loops`
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
```

Los cinco valores de la matriz aparecen en la terminal, como se esperaba. Aunque `index` llegará a un valor de `5` en algún momento, el bucle se detiene antes de intentar obtener un sexto valor de la matriz.

Sin embargo, este enfoque es propenso a errores; podríamos hacer que el programa se detenga abruptamente si el valor del índice o la condición de prueba es incorrecta. Por ejemplo, si cambias la definición de la matriz `a` para que tenga cuatro elementos pero olvidas actualizar la condición a `while index < 4`, el código se detendrá abruptamente. También es lento, porque el compilador agrega código en tiempo de ejecución para realizar la comprobación condicional de si el índice está dentro de los límites de la matriz en cada iteración a través del bucle.

Como alternativa más concisa, puedes usar un bucle `for` y ejecutar un código para cada elemento de una colección. Un bucle `for` se ve como el código en la Lista 3-5.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```

Lista 3-5: Iterando a través de cada elemento de una colección usando un bucle `for`

Cuando ejecutamos este código, veremos la misma salida que en la Lista 3-4. Lo más importante es que ahora hemos aumentado la seguridad del código y eliminado la posibilidad de errores que podrían resultar de exceder el final de la matriz o no ir lo suficiente lejos y omitir algunos elementos.

Usando el bucle `for`, no tendrías que recordar cambiar cualquier otro código si cambias el número de valores en la matriz, como harías con el método usado en la Lista 3-4.

La seguridad y concisión de los bucles `for` los convierten en la construcción de bucle más comúnmente utilizada en Rust. Incluso en situaciones en las que quieres ejecutar un código un número determinado de veces, como en el ejemplo de cuenta atrás que usó un bucle `while` en la Lista 3-3, la mayoría de los rustianos usarían un bucle `for`. La forma de hacer eso sería usar un `Range`, proporcionado por la biblioteca estándar, que genera todos los números secuencialmente comenzando desde un número y terminando antes de otro número.

Así se vería el cuenta atrás usando un bucle `for` y otro método que aún no hemos mencionado, `rev`, para invertir el rango:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```

Este código es un poco más bonito, ¿no?
