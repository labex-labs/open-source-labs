# Condicionales adicionales con filtros de coincidencia

Un _filtro de coincidencia_ es una condición `if` adicional, especificada después del patrón en un brazo de `match`, que también debe coincidir para que se elija ese brazo. Los filtros de coincidencia son útiles para expresar ideas más complejas que lo que permite un patrón solo.

La condición puede usar variables creadas en el patrón. La Lista 18-26 muestra un `match` donde el primer brazo tiene el patrón `Some(x)` y también tiene un filtro de coincidencia de `if x % 2 == 0` (que será `true` si el número es par).

Nombre de archivo: `src/main.rs`

```rust
let num = Some(4);

match num {
    Some(x) if x % 2 == 0 => println!("El número {x} es par"),
    Some(x) => println!("El número {x} es impar"),
    None => (),
}
```

Lista 18-26: Agregar un filtro de coincidencia a un patrón

Este ejemplo imprimirá `El número 4 es par`. Cuando `num` se compara con el patrón en el primer brazo, coincide porque `Some(4)` coincide con `Some(x)`. Luego, el filtro de coincidencia verifica si el residuo de dividir `x` entre 2 es igual a 0, y como es así, se selecciona el primer brazo.

Si `num` hubiera sido `Some(5)` en lugar de eso, el filtro de coincidencia en el primer brazo habría sido `false` porque el residuo de 5 dividido entre 2 es 1, que no es igual a 0. Rust entonces pasaría al segundo brazo, que coincidiría porque el segundo brazo no tiene un filtro de coincidencia y, por lo tanto, coincide con cualquier variante `Some`.

No hay forma de expresar la condición `if x % 2 == 0` dentro de un patrón, por lo que el filtro de coincidencia nos da la capacidad de expresar esta lógica. La desventaja de esta expresividad adicional es que el compilador no intenta comprobar la exhaustividad cuando se involucran expresiones de filtros de coincidencia.

En la Lista 18-11, mencionamos que podríamos usar filtros de coincidencia para resolver nuestro problema de sombreado de patrones. Recuerde que creamos una nueva variable dentro del patrón en la expresión `match` en lugar de usar la variable fuera del `match`. Esa nueva variable significaba que no podíamos probar contra el valor de la variable externa. La Lista 18-27 muestra cómo podemos usar un filtro de coincidencia para solucionar este problema.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Obtuvo 50"),
        Some(n) if n == y => println!("Coincidió, n = {n}"),
        _ => println!("Caso predeterminado, x = {:?}", x),
    }

    println!("al final: x = {:?}, y = {y}", x);
}
```

Lista 18-27: Usar un filtro de coincidencia para probar la igualdad con una variable externa

Este código ahora imprimirá `Caso predeterminado, x = Some(5)`. El patrón en el segundo brazo de coincidencia no introduce una nueva variable `y` que sombreada la `y` externa, lo que significa que podemos usar la `y` externa en el filtro de coincidencia. En lugar de especificar el patrón como `Some(y)`, que habría sombreado la `y` externa, especificamos `Some(n)`. Esto crea una nueva variable `n` que no sombreada nada porque no hay una variable `n` fuera del `match`.

El filtro de coincidencia `if n == y` no es un patrón y, por lo tanto, no introduce nuevas variables. Esta `y` _es_ la `y` externa en lugar de una nueva `y` sombreada, y podemos buscar un valor que tenga el mismo valor que la `y` externa comparando `n` con `y`.

También puede usar el operador _o_ `|` en un filtro de coincidencia para especificar múltiples patrones; la condición del filtro de coincidencia se aplicará a todos los patrones. La Lista 18-28 muestra la precedencia al combinar un patrón que usa `|` con un filtro de coincidencia. La parte importante de este ejemplo es que el filtro de coincidencia `if y` se aplica a `4`, `5`, _y_ `6`, aunque puede parecer que `if y` solo se aplica a `6`.

Nombre de archivo: `src/main.rs`

```rust
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("sí"),
    _ => println!("no"),
}
```

Lista 18-28: Combinar múltiples patrones con un filtro de coincidencia

La condición de coincidencia establece que el brazo solo coincide si el valor de `x` es igual a `4`, `5` o `6` _y_ si `y` es `true`. Cuando se ejecuta este código, el patrón del primer brazo coincide porque `x` es `4`, pero el filtro de coincidencia `if y` es `false`, por lo que el primer brazo no se elige. El código pasa al segundo brazo, que coincide, y este programa imprime `no`. La razón es que la condición `if` se aplica al patrón completo `4 | 5 | 6`, no solo al último valor `6`. En otras palabras, la precedencia de un filtro de coincidencia en relación con un patrón se comporta así:

```rust
(4 | 5 | 6) if y =>...
```

en lugar de esto:

```rust
4 | 5 | (6 if y) =>...
```

Después de ejecutar el código, el comportamiento de precedencia es evidente: si el filtro de coincidencia se aplicara solo al último valor en la lista de valores especificados usando el operador `|`, el brazo habría coincidido y el programa habría impreso `sí`.
