# El Tipo Slice

Las _rebanadas_ te permiten referirte a una secuencia contigua de elementos en una colección en lugar de la colección completa. Una rebanada es un tipo de referencia, por lo que no tiene propiedad.

Aquí hay un pequeño problema de programación: escribe una función que tome una cadena de palabras separadas por espacios y devuelva la primera palabra que encuentre en esa cadena. Si la función no encuentra un espacio en la cadena, toda la cadena debe ser una sola palabra, por lo que se debe devolver la cadena completa.

Veamos cómo escribir la firma de esta función sin usar rebanadas para entender el problema que resolverán las rebanadas:

```rust
fn first_word(s: &String) ->?
```

La función `first_word` tiene un parámetro de tipo `&String`. No queremos la propiedad, por lo que esto está bien. Pero ¿qué debemos devolver? Realmente no tenemos forma de hablar de _parte_ de una cadena. Sin embargo, podríamos devolver el índice del final de la palabra, indicado por un espacio. Intentemos eso, como se muestra en la Lista 4-7.

Nombre del archivo: `src/main.rs`

```rust
fn first_word(s: &String) -> usize {
  1 let bytes = s.as_bytes();

    for (2 i, &item) in 3 bytes.iter().enumerate() {
      4 if item == b' ' {
            return i;
        }
    }

  5 s.len()
}
```

Lista 4-7: La función `first_word` que devuelve un valor de índice de byte en el parámetro `String`

Debido a que necesitamos recorrer el elemento `String` uno por uno y comprobar si un valor es un espacio, convertiremos nuestro `String` en una matriz de bytes usando el método `as_bytes` \[1\].

A continuación, creamos un iterador sobre la matriz de bytes usando el método `iter` \[3\]. Discutiremos los iteradores en más detalle en el Capítulo 13. Por ahora, sabe que `iter` es un método que devuelve cada elemento en una colección y que `enumerate` envuelve el resultado de `iter` y devuelve cada elemento como parte de una tupla en su lugar. El primer elemento de la tupla devuelta por `enumerate` es el índice y el segundo elemento es una referencia al elemento. Esto es un poco más conveniente que calcular el índice nosotros mismos.

Debido a que el método `enumerate` devuelve una tupla, podemos usar patrones para desestructurar esa tupla. Discutiremos los patrones más en el Capítulo 6. En el bucle `for`, especificamos un patrón que tiene `i` para el índice en la tupla y `&item` para el único byte en la tupla \[2\]. Debido a que obtenemos una referencia al elemento de `.iter().enumerate()`, usamos `&` en el patrón.

Dentro del bucle `for`, buscamos el byte que representa el espacio usando la sintaxis de literales de bytes \[4\]. Si encontramos un espacio, devolvemos la posición. De lo contrario, devolvemos la longitud de la cadena usando `s.len()` \[5\].

Ahora tenemos una forma de encontrar el índice del final de la primera palabra en la cadena, pero hay un problema. Estamos devolviendo un `usize` por sí solo, pero solo es un número significativo en el contexto del `&String`. En otras palabras, como es un valor separado del `String`, no hay garantía de que seguirá siendo válido en el futuro. Considere el programa de la Lista 4-8 que usa la función `first_word` de la Lista 4-7.

    // src/main.rs
    fn main() {
        let mut s = String::from("hello world");

        let word = first_word(&s); // word obtendrá el valor 5

        s.clear(); // esto vacía la String, haciéndola igual a ""

        // word todavía tiene el valor 5 aquí, pero ya no hay más cadena que
        // podamos usar significativamente con el valor 5. ¡word ahora es completamente inválido!
    }

Lista 4-8: Almacenar el resultado de llamar a la función `first_word` y luego cambiar el contenido de la `String`

Este programa se compila sin errores y también lo haría si usáramos `word` después de llamar a `s.clear()`. Debido a que `word` no está conectado al estado de `s` en absoluto, `word` todavía contiene el valor `5`. Podríamos usar ese valor `5` con la variable `s` para intentar extraer la primera palabra, pero esto sería un error porque el contenido de `s` ha cambiado desde que guardamos `5` en `word`.

Tener que preocuparse por que el índice en `word` se desincronice con los datos en `s` es tedioso y propenso a errores. Manejar estos índices es aún más frágil si escribimos una función `second_word`. Su firma tendría que verse así:

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Ahora estamos rastreando un índice de inicio _y_ un índice de final, y tenemos aún más valores que se calcularon a partir de datos en un estado particular pero no están vinculados a ese estado en absoluto. Tenemos tres variables no relacionadas que flotan y que deben mantenerse en sincronía.

Por suerte, Rust tiene una solución a este problema: las rebanadas de cadena.
