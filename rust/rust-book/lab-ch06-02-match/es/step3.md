# Coincidencia con `Option<T>`

En la sección anterior, queríamos extraer el valor interno `T` del caso `Some` al usar `Option<T>`; también podemos manejar `Option<T>` usando `match`, como lo hicimos con el `enum Coin`! En lugar de comparar monedas, compararemos las variantes de `Option<T>`, pero la forma en que funciona la expresión `match` sigue siendo la misma.

Digamos que queremos escribir una función que tome una `Option<i32>` y, si hay un valor dentro, sume 1 a ese valor. Si no hay un valor dentro, la función debe devolver el valor `None` y no intentar realizar ninguna operación.

Esta función es muy fácil de escribir, gracias a `match`, y se verá como en la Lista 6-5.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
      1 None => None,
      2 Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five); 3
let none = plus_one(None); 4
```

Lista 6-5: Una función que utiliza una expresión `match` en una `Option<i32>`

Analicemos con más detalle la primera ejecución de `plus_one`. Cuando llamamos a `plus_one(five)` \[3\], la variable `x` en el cuerpo de `plus_one` tendrá el valor `Some(5)`. Luego la comparamos con cada brazo del `match`:

```rust
None => None,
```

El valor `Some(5)` no coincide con el patrón `None` \[1\], así que continuamos con el siguiente brazo:

```rust
Some(i) => Some(i + 1),
```

¿Coincide `Some(5)` con `Some(i)` \[2\]? ¡Por supuesto que sí! Tenemos la misma variante. La `i` se enlaza al valor contenido en `Some`, por lo que `i` toma el valor `5`. Luego se ejecuta el código del brazo del `match`, por lo que sumamos 1 al valor de `i` y creamos un nuevo valor `Some` con nuestro total `6` dentro.

Ahora consideremos la segunda llamada a `plus_one` en la Lista 6-5, donde `x` es `None` \[4\]. Entramos en el `match` y comparamos con el primer brazo \[1\].

¡Coincide! No hay valor al que sumar, así que el programa se detiene y devuelve el valor `None` del lado derecho de `=>`. Debido a que el primer brazo coincidió, no se comparan otros brazos.

Combinar `match` y `enum` es útil en muchas situaciones. Verás este patrón con frecuencia en el código de Rust: hacer coincidir contra un `enum`, enlazar una variable a los datos internos y luego ejecutar código en función de ello. Al principio es un poco complicado, pero una vez que te acostumbras a él, desearás tenerlo en todos los lenguajes. Es consistentemente una de las favoritas de los usuarios.
