# Escribiendo una Prueba Fallida para la Función de Búsqueda Sin Distinguir Mayúsculas y Minúsculas

Primero agregamos una nueva función `search_case_insensitive` que se llamará cuando la variable de entorno tenga un valor. Continuaremos siguiendo el proceso TDD, por lo que el primer paso es nuevamente escribir una prueba fallida. Agregaremos una nueva prueba para la nueva función `search_case_insensitive` y renombraremos nuestra antigua prueba de `one_result` a `case_sensitive` para aclarar las diferencias entre las dos pruebas, como se muestra en la Lista 12-20.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Lista 12-20: Agregando una nueva prueba fallida para la función sin distinguir mayúsculas y minúsculas que vamos a agregar

Tenga en cuenta que también hemos editado el `contenido` de la antigua prueba. Hemos agregado una nueva línea con el texto `"Duct tape."` usando una _D_ mayúscula que no debe coincidir con la consulta `"duct"` cuando estamos buscando de manera sensible a las mayúsculas y minúsculas. Cambiar la antigua prueba de esta manera ayuda a garantizar que no rompamos accidentalmente la funcionalidad de búsqueda sensible a las mayúsculas y minúsculas que ya hemos implementado. Esta prueba ahora debería pasar y debería continuar pasando mientras trabajamos en la búsqueda sin distinguir mayúsculas y minúsculas.

La nueva prueba para la búsqueda sin distinguir mayúsculas y minúsculas utiliza `"rUsT"` como su consulta. En la función `search_case_insensitive` que vamos a agregar, la consulta `"rUsT"` debería coincidir con la línea que contiene `"Rust:"` con una _R_ mayúscula y coincidir con la línea `"Trust me."` aunque ambas tengan un casing diferente de la consulta. Esta es nuestra prueba fallida, y fallará en compilar porque aún no hemos definido la función `search_case_insensitive`. Siéntase libre de agregar una implementación esqueleto que siempre devuelva un vector vacío, de manera similar a la que hicimos para la función `search` en la Lista 12-16 para ver que la prueba compile y falle.
