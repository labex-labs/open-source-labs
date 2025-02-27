# Anotaciones de lifetimes en firmas de funciones

Para usar anotaciones de lifetimes en las firmas de funciones, necesitamos declarar los parámetros de _lifetime_ genéricos dentro de corchetes angulares entre el nombre de la función y la lista de parámetros, al igual que lo hicimos con los parámetros de _tipo_ genéricos.

Queremos que la firma exprese la siguiente restricción: la referencia devuelta será válida siempre que ambos parámetros lo sean. Esta es la relación entre los lifetimes de los parámetros y el valor de retorno. Nombraremos el lifetime `'a` y luego lo agregaremos a cada referencia, como se muestra en la Lista 10-21.

Nombre de archivo: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Lista 10-21: La definición de la función `longest` que especifica que todas las referencias en la firma deben tener el mismo lifetime `'a`

Este código debería compilar y producir el resultado que queremos cuando lo usamos con la función `main` de la Lista 10-19.

La firma de la función ahora le dice a Rust que para algún lifetime `'a`, la función toma dos parámetros, ambos de los cuales son trozos de cadena que viven al menos durante el lifetime `'a`. La firma de la función también le dice a Rust que el trozo de cadena devuelto por la función vivirá al menos durante el lifetime `'a`. En la práctica, significa que el lifetime de la referencia devuelta por la función `longest` es el mismo que el más corto de los lifetimes de los valores a los que se refieren los argumentos de la función. Estas relaciones son lo que queremos que Rust use al analizar este código.

Recuerde, cuando especificamos los parámetros de lifetime en esta firma de función, no estamos cambiando los lifetimes de ningún valor pasado o devuelto. En cambio, estamos especificando que el verificador de préstamos debe rechazar cualquier valor que no adhiera a estas restricciones. Tenga en cuenta que la función `longest` no necesita saber exactamente cuánto tiempo vivirán `x` e `y`, solo que algún ámbito puede sustituir `'a` que satisfaga esta firma.

Cuando se anotan lifetimes en funciones, las anotaciones van en la firma de la función, no en el cuerpo de la función. Las anotaciones de lifetimes se convierten en parte del contrato de la función, al igual que los tipos en la firma. Tener firmas de funciones que contengan el contrato de lifetime significa que el análisis que hace el compilador de Rust puede ser más simple. Si hay un problema con la forma en que se anota una función o la forma en que se llama a ella, los errores del compilador pueden apuntar a la parte de nuestro código y las restricciones con más precisión. Si, en cambio, el compilador de Rust hiciera más inferencias sobre lo que pretendemos que sean las relaciones de los lifetimes, el compilador solo podría apuntar a un uso de nuestro código muchos pasos alejados de la causa del problema.

Cuando pasamos referencias concretas a `longest`, el lifetime concreto que se sustituye por `'a` es la parte del ámbito de `x` que se superpone con el ámbito de `y`. En otras palabras, el lifetime genérico `'a` obtendrá el lifetime concreto que es igual al más corto de los lifetimes de `x` e `y`. Debido a que hemos anotado la referencia devuelta con el mismo parámetro de lifetime `'a`, la referencia devuelta también será válida durante la duración del más corto de los lifetimes de `x` e `y`.

Veamos cómo las anotaciones de lifetime restringen la función `longest` al pasar referencias con lifetimes concretos diferentes. La Lista 10-22 es un ejemplo sencillo.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

Lista 10-22: Usando la función `longest` con referencias a valores de `String` que tienen lifetimes concretos diferentes

En este ejemplo, `string1` es válido hasta el final del ámbito externo, `string2` es válido hasta el final del ámbito interno y `result` se refiere a algo que es válido hasta el final del ámbito interno. Ejecute este código y verá que el verificador de préstamos aprueba; se compilará y se imprimirá `The longest string is long string is long`.

A continuación, probemos un ejemplo que muestra que el lifetime de la referencia en `result` debe ser el lifetime más corto de los dos argumentos. Moveremos la declaración de la variable `result` fuera del ámbito interno pero dejaremos la asignación del valor a la variable `result` dentro del ámbito con `string2`. Luego moveremos el `println!` que usa `result` hacia fuera del ámbito interno, después de que haya terminado el ámbito interno. El código de la Lista 10-23 no se compilará.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

Lista 10-23: Intentando usar `result` después de que `string2` haya salido de ámbito

Cuando intentamos compilar este código, obtenemos este error:

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

El error muestra que para que `result` sea válido para la declaración `println!`, `string2` debería ser válido hasta el final del ámbito externo. Rust lo sabe porque anotamos los lifetimes de los parámetros y valores de retorno de la función usando el mismo parámetro de lifetime `'a`.

Como humanos, podemos ver este código y ver que `string1` es más larga que `string2`, y por lo tanto, `result` contendrá una referencia a `string1`. Debido a que `string1` aún no ha salido de ámbito, una referencia a `string1` todavía será válida para la declaración `println!`. Sin embargo, el compilador no puede ver que la referencia es válida en este caso. Hemos dicho a Rust que el lifetime de la referencia devuelta por la función `longest` es el mismo que el más corto de los lifetimes de las referencias pasadas. Por lo tanto, el verificador de préstamos no permite el código de la Lista 10-23 como posiblemente tener una referencia no válida.

Intente diseñar más experimentos que varíen los valores y lifetimes de las referencias pasadas a la función `longest` y cómo se usa la referencia devuelta. Haga hipótesis sobre si sus experimentos pasarán el verificador de préstamos antes de compilar; luego verifique si está en lo correcto.
