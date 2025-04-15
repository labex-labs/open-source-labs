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
[object Object]
```

La función `expensive_test` se lista como `ignored`. Si queremos ejecutar solo las pruebas ignoradas, podemos usar `cargo test -- --ignored`:

```bash
[object Object]
```

Al controlar qué pruebas se ejecutan, puedes asegurarte de que los resultados de `cargo test` se devuelvan rápidamente. Cuando llegues a un punto en el que tenga sentido comprobar los resultados de las pruebas `ignored` y tengas tiempo para esperar los resultados, puedes ejecutar `cargo test -- --ignored` en su lugar. Si quieres ejecutar todas las pruebas, ya sean ignoradas o no, puedes ejecutar `cargo test -- --include-ignored`.
