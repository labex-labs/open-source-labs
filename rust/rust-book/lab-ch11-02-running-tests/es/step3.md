# Mostrar la salida de una función

Por defecto, si una prueba pasa, la biblioteca de pruebas de Rust captura cualquier cosa impresa en la salida estándar. Por ejemplo, si llamamos a `println!` en una prueba y la prueba pasa, no veremos la salida de `println!` en la terminal; solo veremos la línea que indica que la prueba ha pasado. Si una prueba falla, veremos todo lo que se haya impreso en la salida estándar junto con el resto del mensaje de error.

Como ejemplo, en la Lista 11-10 hay una función tontería que imprime el valor de su parámetro y devuelve 10, así como una prueba que pasa y una prueba que falla.

Nombre del archivo: `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Lista 11-10: Pruebas para una función que llama a `println!`

Cuando ejecutamos estas pruebas con `cargo test`, veremos la siguiente salida:

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Tenga en cuenta que en ninguna parte de esta salida vemos `I got the value 4`, que se imprime cuando se ejecuta la prueba que pasa. Esa salida ha sido capturada. La salida de la prueba que falló, `I got the value 8` \[1\], aparece en la sección de la salida resumida de la prueba, que también muestra la causa del fallo de la prueba.

Si también queremos ver los valores impresos para las pruebas que pasan, podemos decirle a Rust que muestre también la salida de las pruebas exitosas con `--show-output`:

```bash
cargo test -- --show-output
```

Cuando ejecutamos de nuevo las pruebas de la Lista 11-10 con la bandera `--show-output`, vemos la siguiente salida:

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
