# Alternativas a usar match con Result\<T, E\>

¡Eso es mucho `match`! La expresión `match` es muy útil pero también muy primitiva. En el Capítulo 13, aprenderás sobre las closures, que se usan con muchos de los métodos definidos en `Result<T, E>`. Estos métodos pueden ser más concisos que usar `match` al manejar valores de `Result<T, E>` en tu código.

Por ejemplo, aquí hay otra forma de escribir la misma lógica que se muestra en la Lista 9-5, esta vez usando closures y el método `unwrap_or_else`:

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

Aunque este código tiene el mismo comportamiento que la Lista 9-5, no contiene ninguna expresión `match` y es más limpio de leer. Vuelve a este ejemplo después de haber leído el Capítulo 13 y consulta el método `unwrap_or_else` en la documentación de la biblioteca estándar. Muchos más de estos métodos pueden limpiar expresiones `match` anidadas enormes cuando estás manejando errores.
