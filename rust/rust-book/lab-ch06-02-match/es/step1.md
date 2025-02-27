# La Estructura de Control de Flujo `match`

Rust tiene una estructura de control de flujo extremadamente poderosa llamada `match` que te permite comparar un valor contra una serie de patrones y luego ejecutar código según el patrón que coincida. Los patrones pueden estar compuestos por valores literales, nombres de variables, comodines y muchas otras cosas; el Capítulo 18 aborda todos los diferentes tipos de patrones y lo que hacen. El poder de `match` proviene de la expresividad de los patrones y del hecho de que el compilador confirma que todos los casos posibles se manejan.

Piensa en una expresión `match` como en una máquina para clasificar monedas: las monedas deslizan por una pista con orificios de diferentes tamaños a lo largo de ella, y cada moneda cae a través del primer orificio que encuentra y en el que encaja. De la misma manera, los valores pasan por cada patrón en un `match`, y en el primer patrón en el que el valor "encaja", el valor cae en el bloque de código asociado para ser utilizado durante la ejecución.

Hablando de monedas, ¡usemoslas como ejemplo con `match`! Podemos escribir una función que tome una moneda estadounidense desconocida y, de manera similar a la máquina contadora, determine de qué moneda se trata y devuelva su valor en centavos, como se muestra en la Lista 6-3.

```rust
1 enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
  2 match coin {
      3 Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

Lista 6-3: Un `enum` y una expresión `match` que tiene las variantes del `enum` como sus patrones

Analicemos el `match` en la función `value_in_cents`. Primero, listamos la palabra clave `match` seguida de una expresión, que en este caso es el valor `coin` \[2\]. Esto parece muy similar a una expresión utilizada con `if`, pero hay una gran diferencia: con `if`, la expresión debe devolver un valor booleano, pero aquí puede devolver cualquier tipo. El tipo de `coin` en este ejemplo es el `enum Coin` que definimos en \[1\].

A continuación están los brazos del `match`. Un brazo tiene dos partes: un patrón y un poco de código. El primer brazo aquí tiene un patrón que es el valor `Coin::Penny` y luego el operador `=>` que separa el patrón y el código a ejecutar \[3\]. El código en este caso es simplemente el valor `1`. Cada brazo está separado del siguiente con una coma.

Cuando se ejecuta la expresión `match`, compara el valor resultante con el patrón de cada brazo, en orden. Si un patrón coincide con el valor, se ejecuta el código asociado a ese patrón. Si ese patrón no coincide con el valor, la ejecución continúa con el siguiente brazo, al igual que en una máquina para clasificar monedas. Podemos tener tantos brazos como necesitemos: en la Lista 6-3, nuestro `match` tiene cuatro brazos.

El código asociado a cada brazo es una expresión, y el valor resultante de la expresión en el brazo coincidente es el valor que se devuelve para la expresión `match` completa.

Normalmente no usamos llaves si el código del brazo del `match` es corto, como es el caso en la Lista 6-3 donde cada brazo solo devuelve un valor. Si quieres ejecutar múltiples líneas de código en un brazo del `match`, debes usar llaves, y entonces la coma que sigue al brazo es opcional. Por ejemplo, el siguiente código imprime "¡Moneda de un centavo, suerte!" cada vez que se llama al método con un `Coin::Penny`, pero todavía devuelve el último valor del bloque, `1`:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
