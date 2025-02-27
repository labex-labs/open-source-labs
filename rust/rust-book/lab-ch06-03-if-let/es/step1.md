# Flujo de control conciso con if let

La sintaxis `if let` te permite combinar `if` y `let` de una manera menos verbosa para manejar valores que coinciden con un patrón mientras ignoras el resto. Considera el programa de la Lista 6-6 que coincide con un valor de `Option<u8>` en la variable `config_max`, pero solo quiere ejecutar código si el valor es la variante `Some`.

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("El máximo está configurado como {max}"),
    _ => (),
}
```

Lista 6-6: Un `match` que solo se preocupa por ejecutar código cuando el valor es `Some`

Si el valor es `Some`, imprimimos el valor en la variante `Some` al enlazar el valor a la variable `max` en el patrón. No queremos hacer nada con el valor `None`. Para satisfacer la expresión `match`, tenemos que agregar `_ => ()` después de procesar solo una variante, lo que es código de plantilla molesto de agregar.

En cambio, podríamos escribir esto de una manera más corta usando `if let`. El siguiente código se comporta de la misma manera que el `match` de la Lista 6-6:

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("El máximo está configurado como {max}");
}
```

La sintaxis `if let` toma un patrón y una expresión separadas por un signo igual. Funciona de la misma manera que un `match`, donde la expresión se le da al `match` y el patrón es su primer brazo. En este caso, el patrón es `Some(max)`, y `max` se enlaza al valor dentro de `Some`. Luego podemos usar `max` en el cuerpo del bloque `if let` de la misma manera que usamos `max` en el brazo `match` correspondiente. El código en el bloque `if let` no se ejecuta si el valor no coincide con el patrón.

Usar `if let` significa menos tecleo, menos sangría y menos código de plantilla. Sin embargo, pierdes la comprobación exhaustiva que impone `match`. Elegir entre `match` e `if let` depende de lo que estés haciendo en tu situación particular y si ganar concisión es un intercambio adecuado por perder la comprobación exhaustiva.

En otras palabras, puedes pensar en `if let` como un azúcar sintáctico para un `match` que ejecuta código cuando el valor coincide con un patrón y luego ignora todos los demás valores.

Podemos incluir un `else` con un `if let`. El bloque de código que va con el `else` es el mismo que el bloque de código que iría con el caso `_` en la expresión `match` que es equivalente al `if let` y `else`. Recuerda la definición del enum `Coin` en la Lista 6-4, donde la variante `Quarter` también contenía un valor de `UsState`. Si quisiéramos contar todas las monedas que no son de cuarto mientras también anunciamos el estado de los cuartos, podríamos hacerlo con una expresión `match`, como esta:

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("Cuarto del estado de {:?}!", state),
    _ => count += 1,
}
```

O podríamos usar una expresión `if let` y `else`, como esta:

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("Cuarto del estado de {:?}!", state);
} else {
    count += 1;
}
```

Si tienes una situación en la que la lógica de tu programa es demasiado verbosa para expresarse usando un `match`, recuerda que `if let` también está en tu caja de herramientas de Rust.
