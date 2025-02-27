# Ejecutar una sola prueba

Podemos pasar el nombre de cualquier función de prueba a `cargo test` para ejecutar solo esa prueba:

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

Solo se ejecutó la prueba con el nombre `one_hundred`; las otras dos pruebas no coincidían con ese nombre. La salida de la prueba nos informa de que teníamos más pruebas que no se ejecutaron al mostrar `2 filtradas` al final.

No podemos especificar los nombres de múltiples pruebas de esta manera; solo se usará el primer valor dado a `cargo test`. Pero hay una forma de ejecutar múltiples pruebas.
