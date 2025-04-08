# Escribiendo una prueba que falla

Como ya no los necesitamos, eliminemos las declaraciones `println!` de `src/lib.rs` y `src/main.rs` que usamos para comprobar el comportamiento del programa. Luego, en `src/lib.rs`, agregaremos un módulo `tests` con una función de prueba, como hicimos en el Capítulo 11. La función de prueba especifica el comportamiento que queremos que tenga la función `search`: tomará una consulta y el texto a buscar, y devolverá solo las líneas del texto que contengan la consulta. La Lista 12-15 muestra esta prueba, que aún no se compilará.

Nombre del archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

Lista 12-15: Creando una prueba que falla para la función `search` que deseamos tener

Esta prueba busca la cadena `"duct"`. El texto que estamos buscando tiene tres líneas, solo una de las cuales contiene `"duct"` (ten en cuenta que la barra invertida después de la comilla doble de apertura le dice a Rust que no coloque un carácter de nueva línea al principio del contenido de este literal de cadena). Assertivamos que el valor devuelto por la función `search` contiene solo la línea que esperamos.

Todavía no podemos ejecutar esta prueba y verla fallar porque la prueba ni siquiera se compila: ¡la función `search` aún no existe! De acuerdo con los principios del TDD, agregaremos solo el código suficiente para que la prueba se compile y se ejecute agregando una definición de la función `search` que siempre devuelva un vector vacío, como se muestra en la Lista 12-16. Entonces, la prueba debería compilarse y fallar porque un vector vacío no coincide con un vector que contiene la línea `"safe, fast, productive."`.

Nombre del archivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

Lista 12-16: Definiendo solo lo suficiente de la función `search` para que nuestra prueba se compile

Tenga en cuenta que necesitamos definir una vida explícita `'a` en la firma de `search` y usar esa vida con el argumento `contents` y el valor de retorno. Recuerde en el Capítulo 10 que los parámetros de vida especifican qué vida del argumento está conectada a la vida del valor de retorno. En este caso, indicamos que el vector devuelto debe contener rebanadas de cadena que hagan referencia a rebanadas del argumento `contents` (en lugar del argumento `query`).

En otras palabras, le decimos a Rust que los datos devueltos por la función `search` vivirán durante tanto tiempo como los datos pasados a la función `search` en el argumento `contents`. ¡Esto es importante! Los datos referenciados _por_ una rebanada deben ser válidos para que la referencia sea válida; si el compilador asume que estamos haciendo rebanadas de cadena de `query` en lugar de `contents`, hará su comprobación de seguridad incorrectamente.

Si olvidamos las anotaciones de vida y tratamos de compilar esta función, obtendremos este error:

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust no puede posiblemente saber cuál de los dos argumentos necesitamos, por lo que debemos decirlo explícitamente. Debido a que `contents` es el argumento que contiene todo nuestro texto y queremos devolver las partes de ese texto que coinciden, sabemos que `contents` es el argumento que debe estar conectado al valor de retorno usando la sintaxis de vida.

Otros lenguajes de programación no requieren que conecten los argumentos con los valores de retorno en la firma, pero esta práctica se tornará más fácil con el tiempo. Puede que desee comparar este ejemplo con los ejemplos en "Validando Referencias con Lifetimes".

Ahora ejecutemos la prueba:

```bash

```

Genial, la prueba falla, exactamente como esperábamos. ¡Vamos a hacer que la prueba pase!
