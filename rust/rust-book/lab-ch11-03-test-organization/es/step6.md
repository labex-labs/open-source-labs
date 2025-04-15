# El Directorio tests

Creamos un directorio `tests` en el nivel superior de nuestro directorio de proyecto, junto a `src`. Cargo sabe buscar archivos de prueba de integración en este directorio. Luego podemos crear tantos archivos de prueba como queramos, y Cargo compilará cada archivo como un crat individual.

Vamos a crear una prueba de integración. Con el código de la Lista 11-12 todavía en el archivo `src/lib.rs`, cree un directorio `tests` y cree un nuevo archivo llamado `tests/integration_test.rs`. Su estructura de directorios debería verse así:

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

Ingrese el código de la Lista 11-13 en el archivo `tests/integration_test.rs`.

Nombre de archivo: `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

Lista 11-13: Una prueba de integración de una función en el crat `adder`

Cada archivo en el directorio `tests` es un crat separado, por lo que necesitamos traer nuestra biblioteca al alcance de cada crat de prueba. Por eso agregamos `use adder;` al principio del código, lo que no necesitamos en las pruebas unitarias.

No necesitamos anotar ningún código en `tests/integration_test.rs` con `#[cfg(test)]`. Cargo trata el directorio `tests` de manera especial y solo compila los archivos de este directorio cuando ejecutamos `cargo test`. Ejecute `cargo test` ahora:

```bash
[object Object]
```

Las tres secciones de salida incluyen las pruebas unitarias, la prueba de integración y las pruebas de documentación. Tenga en cuenta que si alguna prueba en una sección falla, no se ejecutarán las siguientes secciones. Por ejemplo, si una prueba unitaria falla, no habrá ninguna salida para las pruebas de integración y de documentación porque esas pruebas solo se ejecutarán si todas las pruebas unitarias pasan.

La primera sección para las pruebas unitarias \[1\] es la misma que la que hemos estado viendo: una línea para cada prueba unitaria (una llamada `internal` que agregamos en la Lista 11-12) y luego una línea resumen para las pruebas unitarias.

La sección de pruebas de integración comienza con la línea `Running tests/integration_test.rs` \[2\]. A continuación, hay una línea para cada función de prueba en esa prueba de integración \[3\] y una línea resumen para los resultados de la prueba de integración \[4\] justo antes de que comience la sección `Doc-tests adder`.

Cada archivo de prueba de integración tiene su propia sección, por lo que si agregamos más archivos en el directorio `tests`, habrá más secciones de prueba de integración.

Todavía podemos ejecutar una función de prueba de integración específica especificando el nombre de la función de prueba como argumento para `cargo test`. Para ejecutar todas las pruebas en un archivo de prueba de integración particular, use el argumento `--test` de `cargo test` seguido del nombre del archivo:

```bash
[object Object]
```

Este comando solo ejecuta las pruebas en el archivo `tests/integration_test.rs`.
