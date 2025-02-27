# Probando la igualdad con las macros assert_eq! y assert_ne!

Una forma común de verificar la funcionalidad es probar la igualdad entre el resultado del código que se está probando y el valor que esperas que devuelva el código. Podrías hacer esto usando la macro `assert!` y pasándole una expresión que use el operador `==`. Sin embargo, esta es una prueba tan común que la biblioteca estándar proporciona un par de macros: `assert_eq!` y `assert_ne!`, para realizar esta prueba de manera más conveniente. Estas macros comparan dos argumentos para ver si son iguales o diferentes, respectivamente. También imprimirán los dos valores si la afirmación falla, lo que hace más fácil ver _por qué_ la prueba falló; en cambio, la macro `assert!` solo indica que obtuvo un valor `false` para la expresión `==`, sin imprimir los valores que dieron lugar al valor `false`.

En la Lista 11-7, escribimos una función llamada `add_two` que suma `2` a su parámetro, luego probamos esta función usando la macro `assert_eq!`.

Nombre de archivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Lista 11-7: Probando la función `add_two` usando la macro `assert_eq!`

Veamos si pasa!

    running 1 test
    test tests::it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Le pasamos `4` como argumento a `assert_eq!`, que es igual al resultado de llamar a `add_two(2)`. La línea para esta prueba es `test tests::it_adds_two... ok`, y el texto `ok` indica que nuestra prueba pasó.

Vamos a introducir un error en nuestro código para ver cómo se ve `assert_eq!` cuando falla. Cambia la implementación de la función `add_two` para que en lugar de sumar `2`, sume `3`:

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

Ejecuta las pruebas nuevamente:

    running 1 test
    test tests::it_adds_two... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

¡Nuestra prueba detectó el error! La prueba `it_adds_two` falló, y el mensaje nos dice que la afirmación que falló fue `assertion failed: `(left == right)\``\[1\] y cuáles son los valores de`left`\[2\] y`right`\[3\]. Este mensaje nos ayuda a comenzar a depurar: el argumento`left`era`4`pero el argumento`right`, donde teníamos `add_two(2)`, era `5`. Puedes imaginar que esto sería especialmente útil cuando tenemos muchas pruebas en marcha.

Tenga en cuenta que en algunos lenguajes y marcos de prueba, los parámetros de las funciones de afirmación de igualdad se llaman `expected` y `actual`, y el orden en el que especificamos los argumentos importa. Sin embargo, en Rust, se llaman `left` y `right`, y el orden en el que especificamos el valor que esperamos y el valor que produce el código no importa. Podríamos escribir la afirmación en esta prueba como `assert_eq!(add_two(2), 4)`, lo que resultaría en el mismo mensaje de error que muestra `assertion failed: `(left == right)\``.

La macro `assert_ne!` pasará si los dos valores que le damos no son iguales y fallará si son iguales. Esta macro es más útil en casos en los que no estamos seguros de qué valor _será_, pero sabemos qué valor definitivamente _no debería ser_. Por ejemplo, si estamos probando una función que está garantizada de cambiar su entrada de alguna manera, pero la forma en que la entrada se cambia depende del día de la semana en el que ejecutamos nuestras pruebas, lo mejor que se puede afirmar es que la salida de la función no es igual a la entrada.

En el fondo, las macros `assert_eq!` y `assert_ne!` usan los operadores `==` y `!=`, respectivamente. Cuando las afirmaciones fallan, estas macros imprimen sus argumentos usando el formato de depuración, lo que significa que los valores que se están comparando deben implementar los tratos `PartialEq` y `Debug`. Todos los tipos primitivos y la mayoría de los tipos de la biblioteca estándar implementan estos tratos. Para los structs y los enums que defines tú mismo, necesitarás implementar `PartialEq` para afirmar la igualdad de esos tipos. También necesitarás implementar `Debug` para imprimir los valores cuando la afirmación falla. Debido a que ambos tratos son tratos derivables, como se mencionó en la Lista 5-12, esto por lo general es tan sencillo como agregar la anotación `#[derive(PartialEq, Debug)]` a la definición de tu struct o enum. Consulte el Apéndice C para obtener más detalles sobre estos y otros tratos derivables.
