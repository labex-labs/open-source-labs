# El Módulo de Pruebas y #\[cfg(test)\]

La anotación `#[cfg(test)]` en el módulo `tests` le dice a Rust que compile y ejecute el código de prueba solo cuando ejecuta `cargo test`, no cuando ejecuta `cargo build`. Esto ahorra tiempo de compilación cuando solo desea compilar la biblioteca y ahorra espacio en el artefacto compilado resultante porque las pruebas no se incluyen. Verá que debido a que las pruebas de integración se encuentran en un directorio diferente, no necesitan la anotación `#[cfg(test)]`. Sin embargo, debido a que las pruebas unitarias se encuentran en los mismos archivos que el código, utilizará `#[cfg(test)]` para especificar que no deben incluirse en el resultado compilado.

Recuerde que cuando generamos el nuevo proyecto `adder` en la primera sección de este capítulo, Cargo generó este código para nosotros:

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Este código es el módulo `tests` generado automáticamente. El atributo `cfg` significa _configuración_ y le dice a Rust que el siguiente elemento solo debe incluirse dada una cierta opción de configuración. En este caso, la opción de configuración es `test`, que es proporcionada por Rust para compilar y ejecutar pruebas. Al utilizar el atributo `cfg`, Cargo compila nuestro código de prueba solo si activamente ejecutamos las pruebas con `cargo test`. Esto incluye cualquier función auxiliar que pueda estar dentro de este módulo, además de las funciones anotadas con `#[test]`.
