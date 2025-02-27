# Testing de integración

Las pruebas unitarias prueban un módulo de forma aislada, una a la vez: son pequeñas y pueden probar código privado. Las pruebas de integración son externas a su crate y utilizan solo su interfaz pública de la misma manera que cualquier otro código. Su propósito es probar que muchas partes de su biblioteca funcionen correctamente juntas.

Cargo busca las pruebas de integración en el directorio `tests` junto a `src`.

Archivo `src/lib.rs`:

```rust
// Definir esto en un crate llamado `adder`.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Archivo con la prueba: `tests/integration_test.rs`:

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

Ejecutar las pruebas con el comando `cargo test`:

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Cada archivo fuente de Rust en el directorio `tests` se compila como un crate independiente. Para compartir código entre las pruebas de integración, podemos crear un módulo con funciones públicas, importándolo y usándolo dentro de las pruebas.

Archivo `tests/common/mod.rs`:

```rust
pub fn setup() {
    // algún código de configuración, como crear archivos/directorios necesarios, iniciar
    // servidores, etc.
}
```

Archivo con la prueba: `tests/integration_test.rs`

```rust
// importando el módulo común.
mod common;

#[test]
fn test_add() {
    // usando el código común.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

Crear el módulo como `tests/common.rs` también funciona, pero no se recomienda porque el ejecutor de pruebas tratará el archivo como un crate de prueba e intentará ejecutar las pruebas dentro de él.
