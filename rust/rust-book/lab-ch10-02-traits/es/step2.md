# Definiendo un Trait

El comportamiento de un tipo está compuesto por los métodos que podemos llamar en ese tipo. Diferentes tipos comparten el mismo comportamiento si podemos llamar a los mismos métodos en todos ellos. Las definiciones de traits son una forma de agrupar firmas de métodos para definir un conjunto de comportamientos necesarios para cumplir algún propósito.

Por ejemplo, digamos que tenemos múltiples structs que almacenan diferentes tipos y cantidades de texto: un struct `NewsArticle` que almacena una noticia en un lugar particular y un `Tweet` que puede tener, como máximo, 280 caracteres, junto con metadatos que indican si es un nuevo tweet, un retweet o una respuesta a otro tweet.

Queremos crear una caja de código de biblioteca de agregador de medios llamada `aggregator` que pueda mostrar resúmenes de datos que pueden estar almacenados en una instancia de `NewsArticle` o `Tweet`. Para hacer esto, necesitamos un resumen de cada tipo y solicitaremos ese resumen llamando al método `summarize` en una instancia. La Lista 10-12 muestra la definición de un trait público `Summary` que expresa este comportamiento.

Nombre de archivo: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

Lista 10-12: Un trait `Summary` que consta del comportamiento proporcionado por un método `summarize`

Aquí, declaramos un trait usando la palabra clave `trait` y luego el nombre del trait, que en este caso es `Summary`. También declaramos el trait como `pub` para que las cajas de código que dependen de esta caja de código puedan también utilizar este trait, como veremos en algunos ejemplos. Dentro de las llaves, declaramos las firmas de los métodos que describen los comportamientos de los tipos que implementan este trait, que en este caso es `fn summarize(&self) -> String`.

Después de la firma del método, en lugar de proporcionar una implementación dentro de las llaves, usamos un punto y coma. Cada tipo que implemente este trait debe proporcionar su propio comportamiento personalizado para el cuerpo del método. El compilador exigirá que cualquier tipo que tenga el trait `Summary` tendrá el método `summarize` definido con exactamente esta firma.

Un trait puede tener múltiples métodos en su cuerpo: las firmas de los métodos se listan una por línea y cada línea termina en un punto y coma.
