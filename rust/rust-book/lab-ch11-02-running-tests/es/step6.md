# Filtrado para ejecutar múltiples pruebas

Podemos especificar una parte del nombre de una prueba, y cualquier prueba cuyo nombre coincida con ese valor se ejecutará. Por ejemplo, dado que dos de los nombres de nuestras pruebas contienen `add`, podemos ejecutarlas dos ejecutando `cargo test add`:

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Este comando ejecutó todas las pruebas con `add` en el nombre y filtró la prueba llamada `one_hundred`. También tenga en cuenta que el módulo en el que aparece una prueba se convierte en parte del nombre de la prueba, por lo que podemos ejecutar todas las pruebas en un módulo filtrando por el nombre del módulo.
