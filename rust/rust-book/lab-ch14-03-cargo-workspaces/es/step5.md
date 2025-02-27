# Agregar una prueba a un espacio de trabajo

Para otra mejora, agreguemos una prueba de la función `add_one::add_one` dentro del crate `add_one`:

Nombre del archivo: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Ahora ejecute `cargo test` en el directorio `add` de nivel superior. Ejecutar `cargo test` en un espacio de trabajo estructurado como este ejecutará las pruebas para todos los crates en el espacio de trabajo:

```bash
$ cargo test
   Compilando add_one v0.1.0 (file:///projects/add/add_one)
   Compilando adder v0.1.0 (file:///projects/add/adder)
    Compilación finalizada [prueba + información de depuración] en 0.27s
     Ejecutando pruebas unitarias src/lib.rs (target/debug/deps/add_one-f0253159197f7841)

ejecutando 1 prueba
test tests::it_works... ok

resultado de la prueba: ok. 1 pasado; 0 fallidos; 0 ignorados; 0 medidos; 0 filtrados;
finalizado en 0.00s

     Ejecutando pruebas unitarias src/main.rs (target/debug/deps/adder-49979ff40686fa8e)

ejecutando 0 pruebas

resultado de la prueba: ok. 0 pasados; 0 fallidos; 0 ignorados; 0 medidos; 0 filtrados;
finalizado en 0.00s

   Pruebas de documentación add_one

ejecutando 0 pruebas

resultado de la prueba: ok. 0 pasados; 0 fallidos; 0 ignorados; 0 medidos; 0 filtrados;
finalizado en 0.00s
```

La primera sección de la salida muestra que la prueba `it_works` en el crate `add_one` pasó. La siguiente sección muestra que se encontraron cero pruebas en el crate `adder`, y luego la última sección muestra que se encontraron cero pruebas de documentación en el crate `add_one`.

También podemos ejecutar las pruebas para un crate en particular en un espacio de trabajo desde el directorio de nivel superior usando la bandera `-p` y especificando el nombre del crate que queremos probar:

```bash
$ cargo test -p add_one
    Compilación finalizada [prueba + información de depuración] en 0.00s
     Ejecutando pruebas unitarias src/lib.rs (target/debug/deps/add_one-b3235fea9a156f74)

ejecutando 1 prueba
test tests::it_works... ok

resultado de la prueba: ok. 1 pasado; 0 fallidos; 0 ignorados; 0 medidos; 0 filtrados;
finalizado en 0.00s

   Pruebas de documentación add_one

ejecutando 0 pruebas

resultado de la prueba: ok. 0 pasados; 0 fallidos; 0 ignorados; 0 medidos; 0 filtrados;
finalizado en 0.00s
```

Esta salida muestra que `cargo test` solo ejecutó las pruebas para el crate `add_one` y no ejecutó las pruebas del crate `adder`.

Si publica los crates en el espacio de trabajo en *https://crates.io*, cada crate en el espacio de trabajo debe ser publicado por separado. Al igual que `cargo test`, podemos publicar un crate en particular en nuestro espacio de trabajo usando la bandera `-p` y especificando el nombre del crate que queremos publicar.

Para más práctica, agregue un crate `add_two` a este espacio de trabajo de manera similar al crate `add_one`!

A medida que su proyecto crece, considere usar un espacio de trabajo: proporciona componentes individuales más fáciles de entender y más pequeños que un gran bloque de código. Además, mantener los crates en un espacio de trabajo puede facilitar la coordinación entre los crates si a menudo se modifican al mismo tiempo.
