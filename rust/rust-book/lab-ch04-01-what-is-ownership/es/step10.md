# Valores de retorno y ámbito

Devolver valores también puede transferir la propiedad. La Lista 4-4 muestra un ejemplo de una función que devuelve un valor, con anotaciones similares a las de la Lista 4-3.

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership mueve su valor
                                            // de retorno a s1

        let s2 = String::from("hello");     // s2 entra en el ámbito

        let s3 = takes_and_gives_back(s2);  // s2 se mueve a
                                            // takes_and_gives_back, que también
                                            // mueve su valor de retorno a s3
    } // Aquí, s3 sale del ámbito y se elimina. s2 fue movida, por lo que nada
      // sucede. s1 sale del ámbito y se elimina

    fn gives_ownership() -> String {             // gives_ownership moverá su
                                                 // valor de retorno a la función
                                                 // que la llama

        let some_string = String::from("yours"); // some_string entra en el ámbito

        some_string                              // some_string se devuelve y
                                                 // se mueve hacia la función
                                                 // llamante
    }

    // Esta función toma una String y devuelve una String
    fn takes_and_gives_back(a_string: String) -> String { // a_string entra en
                                                          // el ámbito

        a_string  // a_string se devuelve y se mueve hacia la función
                  // llamante
    }

Lista 4-4: Transferencia de la propiedad de los valores de retorno

La propiedad de una variable sigue el mismo patrón cada vez: asignar un valor a otra variable lo mueve. Cuando una variable que incluye datos en el montón sale del ámbito, el valor se limpiará con `drop` a menos que la propiedad de los datos haya sido transferida a otra variable.

Si bien esto funciona, tomar la propiedad y luego devolver la propiedad con cada función es un poco tedioso. ¿Qué pasa si queremos permitir que una función use un valor pero no tome la propiedad? Es bastante molesto que todo lo que pasamos también tenga que ser pasado de vuelta si queremos usarlo de nuevo, además de cualquier dato resultante del cuerpo de la función que podamos querer devolver también.

Rust nos permite devolver múltiples valores usando una tupla, como se muestra en la Lista 4-5.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() devuelve la longitud de una String

    (s, length)
}
```

Lista 4-5: Devolución de la propiedad de los parámetros

Pero esto es demasiado formal y requiere mucho trabajo para un concepto que debería ser común. Por suerte para nosotros, Rust tiene una característica para usar un valor sin transferir la propiedad, llamada _referencias_.
