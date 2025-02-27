# Implementando un Trait en un Tipo

Ahora que hemos definido las firmas deseadas de los métodos del trait `Summary`, podemos implementarlo en los tipos de nuestro agregador de medios. La Lista 10-13 muestra una implementación del trait `Summary` en el struct `NewsArticle` que utiliza el titular, el autor y la ubicación para crear el valor de retorno de `summarize`. Para el struct `Tweet`, definimos `summarize` como el nombre de usuario seguido del texto completo del tweet, suponiendo que el contenido del tweet ya está limitado a 280 caracteres.

Nombre de archivo: `src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

Lista 10-13: Implementando el trait `Summary` en los tipos `NewsArticle` y `Tweet`

Implementar un trait en un tipo es similar a implementar métodos regulares. La diferencia es que después de `impl`, ponemos el nombre del trait que queremos implementar, luego usamos la palabra clave `for`, y luego especificamos el nombre del tipo para el que queremos implementar el trait. Dentro del bloque `impl`, ponemos las firmas de los métodos que la definición del trait ha definido. En lugar de agregar un punto y coma después de cada firma, usamos llaves y llenamos el cuerpo del método con el comportamiento específico que queremos que los métodos del trait tengan para el tipo particular.

Ahora que la biblioteca ha implementado el trait `Summary` en `NewsArticle` y `Tweet`, los usuarios de la caja de código pueden llamar a los métodos del trait en instancias de `NewsArticle` y `Tweet` de la misma manera que llamamos a métodos regulares. La única diferencia es que el usuario debe traer el trait al ámbito, así como los tipos. Aquí hay un ejemplo de cómo una caja de código binaria podría usar nuestra caja de código de biblioteca `aggregator`:

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

Este código imprime `1 new tweet: horse_ebooks: of course, as you probably already know, people`.

Otras cajas de código que dependen de la caja de código `aggregator` también pueden traer el trait `Summary` al ámbito para implementar `Summary` en sus propios tipos. Una restricción a tener en cuenta es que solo podemos implementar un trait en un tipo si el trait o el tipo, o ambos, son locales a nuestra caja de código. Por ejemplo, podemos implementar traits de la biblioteca estándar como `Display` en un tipo personalizado como `Tweet` como parte de la funcionalidad de nuestra caja de código `aggregator` porque el tipo `Tweet` es local a nuestra caja de código `aggregator`. También podemos implementar `Summary` en `Vec<T>` en nuestra caja de código `aggregator` porque el trait `Summary` es local a nuestra caja de código `aggregator`.

Pero no podemos implementar traits externos en tipos externos. Por ejemplo, no podemos implementar el trait `Display` en `Vec<T>` dentro de nuestra caja de código `aggregator` porque `Display` y `Vec<T>` están ambos definidos en la biblioteca estándar y no son locales a nuestra caja de código `aggregator`. Esta restricción es parte de una propiedad llamada _coherencia_, y más específicamente la _regla de los huérfanos_, así llamada porque el tipo padre no está presente. Esta regla asegura que el código de otras personas no pueda romper tu código y viceversa. Sin la regla, dos cajas de código podrían implementar el mismo trait para el mismo tipo, y Rust no sabría qué implementación usar.
