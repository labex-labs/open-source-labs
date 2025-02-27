# Usando Result\<T, E\> en las pruebas

Hasta ahora, todas nuestras pruebas se desbordan cuando fallan. ¡También podemos escribir pruebas que usen `Result<T, E>`! Aquí está la prueba de la Lista 11-1, reescrita para usar `Result<T, E>` y devolver un `Err` en lugar de desbordarse:

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

La función `it_works` ahora tiene el tipo de retorno `Result<(), String>`. En el cuerpo de la función, en lugar de llamar a la macro `assert_eq!`, devolvemos `Ok(())` cuando la prueba pasa y un `Err` con una `String` dentro cuando la prueba falla.

Escribir pruebas para que devuelvan un `Result<T, E>` te permite usar el operador de interrogación en el cuerpo de las pruebas, lo que puede ser una forma conveniente de escribir pruebas que deben fallar si cualquier operación dentro de ellas devuelve una variante `Err`.

No puedes usar la anotación `#[should_panic]` en pruebas que usan `Result<T, E>`. Para afirmar que una operación devuelve una variante `Err`, _no_ uses el operador de interrogación en el valor `Result<T, E>`. En su lugar, usa `assert!(value.is_err())`.

Ahora que conoces varias maneras de escribir pruebas, echemos un vistazo a lo que está sucediendo cuando ejecutamos nuestras pruebas y exploremos las diferentes opciones que podemos usar con `cargo test`.
