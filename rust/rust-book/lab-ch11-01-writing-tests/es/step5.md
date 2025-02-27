# Agregando mensajes de error personalizados

También puedes agregar un mensaje personalizado para que se imprima con el mensaje de error como argumentos opcionales a las macros `assert!`, `assert_eq!` y `assert_ne!`. Cualquier argumento especificado después de los argumentos requeridos se pasa a la macro `format!` (discutida en "Concatenación con el operador + o la macro format!"), por lo que puedes pasar una cadena de formato que contenga marcadores de posición `{}` y valores para ir en esos marcadores de posición. Los mensajes personalizados son útiles para documentar lo que significa una afirmación; cuando una prueba falla, tendrás una mejor idea de cuál es el problema con el código.

Por ejemplo, supongamos que tenemos una función que saluda a las personas por nombre y queremos probar que el nombre que pasamos a la función aparezca en la salida:

Nombre de archivo: `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

Los requisitos de este programa aún no han sido acordados, y estamos bastante seguros de que el texto `Hello` al principio del saludo cambiará. Decidimos que no queremos tener que actualizar la prueba cuando los requisitos cambien, por lo que en lugar de comprobar la igualdad exacta con el valor devuelto por la función `greeting`, simplemente afirmaremos que la salida contiene el texto del parámetro de entrada.

Ahora vamos a introducir un error en este código cambiando `greeting` para excluir `name` para ver cómo se ve el error de prueba predeterminado:

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

Ejecutar esta prueba produce lo siguiente:

    running 1 test
    test tests::greeting_contains_name... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

Este resultado solo indica que la afirmación falló y en qué línea está la afirmación. Un mensaje de error más útil imprimiría el valor de la función `greeting`. Vamos a agregar un mensaje de error personalizado compuesto por una cadena de formato con un marcador de posición lleno con el valor real que obtuvimos de la función `greeting`:

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

Ahora cuando ejecutamos la prueba, obtendremos un mensaje de error más informativo:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

Podemos ver el valor que realmente obtuvimos en la salida de la prueba, lo que nos ayudaría a depurar lo que sucedió en lugar de lo que esperábamos que sucediera.
