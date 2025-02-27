# Submódulos en Pruebas de Integración

A medida que agregas más pruebas de integración, es posible que desees crear más archivos en el directorio `tests` para ayudar a organizarlos; por ejemplo, puedes agrupar las funciones de prueba por la funcionalidad que están probando. Como se mencionó anteriormente, cada archivo en el directorio `tests` se compila como un crat separado, lo que es útil para crear ámbitos separados y imitar más de cerca la forma en que los usuarios finales utilizarán tu crat. Sin embargo, esto significa que los archivos en el directorio `tests` no comparten el mismo comportamiento que los archivos en `src`, como aprendiste en el Capítulo 7 sobre cómo separar el código en módulos y archivos.

El comportamiento diferente de los archivos del directorio `tests` es más evidente cuando tienes un conjunto de funciones auxiliares para usar en múltiples archivos de prueba de integración y tratas de seguir los pasos de "Separando Módulos en Diferentes Archivos" para extraerlas a un módulo común. Por ejemplo, si creamos `tests/common.rs` y ponemos una función llamada `setup` en él, podemos agregar un poco de código a `setup` que queramos llamar desde múltiples funciones de prueba en múltiples archivos de prueba:

Nombre de archivo: `tests/common.rs`

```rust
pub fn setup() {
    // código de configuración específico de las pruebas de tu biblioteca iría aquí
}
```

Cuando ejecutamos las pruebas nuevamente, veremos una nueva sección en la salida de las pruebas para el archivo `common.rs`, aunque este archivo no contiene ninguna función de prueba ni llamamos a la función `setup` desde ningún lugar:

    running 1 test
    test tests::internal... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Que `common` aparezca en los resultados de las pruebas con `running 0 tests` mostrado para él no es lo que queríamos. Solo queríamos compartir un poco de código con los otros archivos de prueba de integración. Para evitar que `common` aparezca en la salida de las pruebas, en lugar de crear `tests/common.rs`, crearemos `tests/common/mod.rs`. El directorio del proyecto ahora se ve así:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

Esta es la antigua convención de nombres que Rust también entiende que mencionamos en "Rutas Alternativas de Archivos". Nombra el archivo de esta manera para decirle a Rust que no trate el módulo `common` como un archivo de prueba de integración. Cuando movemos el código de la función `setup` a `tests/common/mod.rs` y eliminamos el archivo `tests/common.rs`, la sección en la salida de las pruebas ya no aparecerá. Los archivos en subdirectorios del directorio `tests` no se compilan como crates separados ni tienen secciones en la salida de las pruebas.

Después de crear `tests/common/mod.rs`, podemos usarlo desde cualquiera de los archivos de prueba de integración como un módulo. Aquí hay un ejemplo de llamar a la función `setup` desde la prueba `it_adds_two` en `tests/integration_test.rs`:

Nombre de archivo: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

Tenga en cuenta que la declaración `mod common;` es la misma que la declaración de módulo que demostramos en la Lista 7-21. Luego, en la función de prueba, podemos llamar a la función `common::setup()`.
