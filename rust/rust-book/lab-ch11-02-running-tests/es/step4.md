# Ejecutar un subconjunto de pruebas por nombre

A veces, ejecutar una suite completa de pruebas puede tomar mucho tiempo. Si estás trabajando en código en un área particular, es posible que desees ejecutar solo las pruebas relacionadas con ese código. Puedes elegir qué pruebas ejecutar pasando a `cargo test` el nombre o nombres de la(s) prueba(s) que quieres ejecutar como argumento.

Para demostrar cómo ejecutar un subconjunto de pruebas, primero crearemos tres pruebas para nuestra función `add_two`, como se muestra en la Lista 11-11, y luego elegiremos cuáles ejecutar.

Nombre del archivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Lista 11-11: Tres pruebas con tres nombres diferentes

Si ejecutamos las pruebas sin pasar ningún argumento, como vimos anteriormente, todas las pruebas se ejecutarán en paralelo:

    running 3 tests
    test tests::add_three_and_two... ok
    test tests::add_two_and_two... ok
    test tests::one_hundred... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
