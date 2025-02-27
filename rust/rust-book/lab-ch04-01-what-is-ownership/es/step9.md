# Propiedad y funciones

La mecánica de pasar un valor a una función es similar a la de asignar un valor a una variable. Pasar una variable a una función hará que se mueva o se copie, al igual que en el caso de la asignación. La Lista 4-3 tiene un ejemplo con algunas anotaciones que muestran dónde entran y salen del ámbito las variables.

    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s entra en el ámbito

        takes_ownership(s);             // el valor de s se mueve a la función...
                                        //... y por lo tanto ya no es válido aquí

        let x = 5;                      // x entra en el ámbito

        makes_copy(x);                  // x se movería a la función,
                                        // pero i32 implementa Copy, por lo que está bien
                                        // seguir usando x después

    } // Aquí, x sale del ámbito, luego s. Sin embargo, debido a que el valor de s
      // fue movido, no pasa nada especial

    fn takes_ownership(some_string: String) { // some_string entra en el ámbito
        println!("{some_string}");
    } // Aquí, some_string sale del ámbito y se llama a `drop`. La memoria
      // subyacente se libera

    fn makes_copy(some_integer: i32) { // some_integer entra en el ámbito
        println!("{some_integer}");
    } // Aquí, some_integer sale del ámbito. No pasa nada especial

Lista 4-3: Funciones con propiedad y ámbito anotados

Si intentáramos usar `s` después de llamar a `takes_ownership`, Rust lanzaría un error en tiempo de compilación. Estas comprobaciones estáticas nos protegen de los errores. Intenta agregar código a `main` que use `s` y `x` para ver dónde se pueden usar y dónde las reglas de propiedad te impiden hacerlo.
