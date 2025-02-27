# Comprobando desbordamientos con should_panic

Además de comprobar los valores de retorno, es importante comprobar que nuestro código maneje las condiciones de error como esperamos. Por ejemplo, considere el tipo `Guess` que creamos en la Lista 9-13. Otro código que utiliza `Guess` depende de la garantía de que las instancias de `Guess` contendrán solo valores entre 1 y 100. Podemos escribir una prueba que asegure que intentar crear una instancia de `Guess` con un valor fuera de ese rango provoque un desbordamiento.

Hacemos esto agregando el atributo `should_panic` a nuestra función de prueba. La prueba pasa si el código dentro de la función se desborda; la prueba falla si el código dentro de la función no se desborda.

La Lista 11-8 muestra una prueba que comprueba que las condiciones de error de `Guess::new` ocurran cuando esperamos que ocurran.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Lista 11-8: Probando que una condición causará un desbordamiento

Colocamos el atributo `#[should_panic]` después del atributo `#[test]` y antes de la función de prueba a la que se aplica. Echemos un vistazo al resultado cuando esta prueba pasa:

    running 1 test
    test tests::greater_than_100 - should panic... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

¡Parece bien! Ahora vamos a introducir un error en nuestro código eliminando la condición de que la función `new` se desborde si el valor es mayor que 100:

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Cuando ejecutamos la prueba de la Lista 11-8, fallará:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

En este caso no obtenemos un mensaje muy útil, pero cuando miramos la función de prueba, vemos que está anotada con `#[should_panic]`. El fallo que obtuvimos significa que el código en la función de prueba no causó un desbordamiento.

Las pruebas que usan `should_panic` pueden ser imprecisas. Una prueba `should_panic` pasará incluso si la prueba se desborda por un motivo diferente al que esperábamos. Para hacer que las pruebas `should_panic` sean más precisas, podemos agregar un parámetro opcional `expected` al atributo `should_panic`. El harness de pruebas se asegurará de que el mensaje de error contenga el texto proporcionado. Por ejemplo, considere el código modificado de `Guess` en la Lista 11-9 donde la función `new` se desborda con mensajes diferentes dependiendo de si el valor es demasiado pequeño o demasiado grande.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Lista 11-9: Probando un `desbordamiento` con un mensaje de desbordamiento que contiene una subcadena especificada

Esta prueba pasará porque el valor que ponemos en el parámetro `expected` del atributo `should_panic` es una subcadena del mensaje con el que se desborda la función `Guess::new`. Podríamos haber especificado el mensaje de desbordamiento completo que esperamos, que en este caso sería `Guess value must be less than or equal to 100, got 200`. Lo que elijas especificar depende de cuánto del mensaje de desbordamiento es único o dinámico y de qué tan precisa quieres que sea tu prueba. En este caso, una subcadena del mensaje de desbordamiento es suficiente para asegurar que el código en la función de prueba ejecuta el caso `else if value > 100`.

Para ver lo que sucede cuando una prueba `should_panic` con un mensaje `expected` falla, vamos a introducir nuevamente un error en nuestro código intercambiando los cuerpos de los bloques `if value < 1` y `else if value > 100`:

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

Esta vez cuando ejecutamos la prueba `should_panic`, fallará:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

El mensaje de error indica que esta prueba sí se desbordó como esperábamos, pero el mensaje de desbordamiento no incluyó la cadena esperada `'Guess value must be less than or equal to 100'`. El mensaje de desbordamiento que obtuvimos en este caso fue `Guess value must be greater than or equal to 1, got 200`. Ahora podemos empezar a averiguar dónde está nuestro error.
