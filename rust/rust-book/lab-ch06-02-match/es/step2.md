# Patrones que se asocian a Valores

Otra característica útil de los brazos del `match` es que pueden enlazarse a las partes de los valores que coinciden con el patrón. Así es como podemos extraer valores de las variantes del `enum`.

Como ejemplo, cambiemos una de las variantes de nuestro `enum` para que contenga datos dentro de ella. De 1999 a 2008, la moneeda estadounidense de 25 centavos tenía diferentes diseños para cada una de las 50 estados en un lado. Ninguna otra moneda tenía diseños de estados, por lo que solo las monedas de 25 centavos tienen este valor extra. Podemos agregar esta información a nuestro `enum` cambiando la variante `Quarter` para incluir un valor de `UsState` almacenado dentro de ella, como se ha hecho en la Lista 6-4.

```rust
#[derive(Debug)] // para que podamos inspeccionar el estado en un momento
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

Lista 6-4: Un `enum Coin` en el que la variante `Quarter` también contiene un valor de `UsState`

Imaginemos que un amigo está intentando recolectar las 50 monedas de 25 centavos de los estados. Mientras clasificamos nuestro cambio suelto por tipo de moneda, también llamaremos el nombre del estado asociado a cada moneda de 25 centavos para que si es una que nuestro amigo no tiene, puedan agregarla a su colección.

En la expresión `match` de este código, agregamos una variable llamada `state` al patrón que coincide con los valores de la variante `Coin::Quarter`. Cuando un `Coin::Quarter` coincide, la variable `state` se enlazará al valor del estado de esa moneda de 25 centavos. Luego podemos usar `state` en el código de ese brazo, como sigue:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

Si llamáramos a `value_in_cents(Coin::Quarter(UsState::Alaska))`, `coin` sería `Coin::Quarter(UsState::Alaska)`. Cuando comparamos ese valor con cada uno de los brazos del `match`, ninguno de ellos coincide hasta que llegamos a `Coin::Quarter(state)`. En ese momento, el enlace para `state` será el valor `UsState::Alaska`. Luego podemos usar ese enlace en la expresión `println!`, obteniendo así el valor interno de estado de la variante `Coin` para `Quarter`.
