# Ignorar algunas pruebas a menos que se soliciten específicamente

A veces, algunas pruebas específicas pueden ser muy tardadas en ejecutarse, por lo que es posible que desees excluirlas durante la mayoría de las ejecuciones de `cargo test`. En lugar de enumerar como argumentos todas las pruebas que realmente quieres ejecutar, en su lugar puedes anotar las pruebas tardadas utilizando el atributo `ignore` para excluirlas, como se muestra aquí:

Nombre del archivo: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // código que tarda una hora en ejecutarse
}
```

Después de `#[test]`, agregamos la línea `#[ignore]` a la prueba que queremos excluir. Ahora, cuando ejecutamos nuestras pruebas, `it_works` se ejecuta, pero `expensive_test` no:

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.60s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test expensive_test... ignored
test it_works... ok

test result: ok. 1 passed; 0 failed; 1 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

La función `expensive_test` se lista como `ignored`. Si queremos ejecutar solo las pruebas ignoradas, podemos usar `cargo test -- --ignored`:

```bash
$ cargo test -- --ignored
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test expensive_test... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Al controlar qué pruebas se ejecutan, puedes asegurarte de que los resultados de `cargo test` se devuelvan rápidamente. Cuando llegues a un punto en el que tenga sentido comprobar los resultados de las pruebas `ignored` y tengas tiempo para esperar los resultados, puedes ejecutar `cargo test -- --ignored` en su lugar. Si quieres ejecutar todas las pruebas, ya sean ignoradas o no, puedes ejecutar `cargo test -- --include-ignored`.
