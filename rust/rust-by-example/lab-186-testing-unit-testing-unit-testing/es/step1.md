# Pruebas unitarias

Las pruebas son funciones de Rust que verifican que el código no de prueba funcione de la manera esperada. Los cuerpos de las funciones de prueba generalmente realizan alguna configuración, ejecutan el código que queremos probar y luego afirman si los resultados son los que esperamos.

La mayoría de las pruebas unitarias van en un módulo `tests` con el atributo `#[cfg(test)]`. Las funciones de prueba se marcan con el atributo `#[test]`.

Las pruebas fallan cuando algo en la función de prueba produce un `panic`. Hay algunas macros auxiliares:

- `assert!(expresión)` - produce un `panic` si la expresión evalúa a `false`.
- `assert_eq!(izquierda, derecha)` y `assert_ne!(izquierda, derecha)` - prueban la igualdad y desigualdad de las expresiones izquierda y derecha respectivamente.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Esta es una función de suma muy mala, su propósito es fallar en este
// ejemplo.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // Observe esta práctica útil: importar nombres del ámbito externo (para las pruebas de módulo).
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // Esta afirmación se activará y la prueba fallará.
        // Tenga en cuenta que las funciones privadas también se pueden probar!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

Las pruebas se pueden ejecutar con `cargo test`.

```shell
$ cargo test

running 2 tests
test tests::test_bad_add... FAILED
test tests::test_add... ok

fallures:

---- tests::test_bad_add stdout ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
note: Run with $(RUST_BACKTRACE=1) for a backtrace.

fallures:
tests::test_bad_add

test result: FAILED. 1 passed
1 failed
0 ignored
0 measured
0 filtered out
```

## Pruebas y `?`

Ninguno de los ejemplos de pruebas unitarias anteriores tenía un tipo de retorno. Pero en Rust 2018, sus pruebas unitarias pueden devolver `Result<()>`, lo que le permite utilizar `?` en ellas. Esto puede hacerlas mucho más concisas.

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("negative floats don't have square roots".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

Vea "The Edition Guide" para obtener más detalles.

## Pruebas de `panic`

Para comprobar funciones que deben producir un `panic` en ciertas circunstancias, use el atributo `#[should_panic]`. Este atributo acepta un parámetro opcional `expected =` con el texto del mensaje de `panic`. Si su función puede producir un `panic` de múltiples maneras, ayuda a asegurarse de que su prueba esté probando el `panic` correcto.

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

Ejecutar estas pruebas nos da:

```shell
$ cargo test

running 3 tests
test tests::test_any_panic... ok
test tests::test_divide... ok
test tests::test_specific_panic... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Ejecutar pruebas específicas

Para ejecutar pruebas específicas, se puede especificar el nombre de la prueba en el comando `cargo test`.

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
2 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Para ejecutar múltiples pruebas, se puede especificar una parte del nombre de la prueba que coincida con todas las pruebas que deben ejecutarse.

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic... ok
test tests::test_specific_panic... ok

test result: ok. 2 passed
0 failed
0 ignored
0 measured
1 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Ignorar pruebas

Las pruebas se pueden marcar con el atributo `#[ignore]` para excluir algunas pruebas. O para ejecutarlas con el comando `cargo test -- --ignored`

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test... ignored
test tests::test_add... ok
test tests::test_add_hundred... ok

test result: ok. 2 passed
0 failed
1 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

$ cargo test -- --ignored
running 1 test
test tests::ignored_test... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```
