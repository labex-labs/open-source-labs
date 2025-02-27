# Implementaciones Predeterminadas

A veces es útil tener un comportamiento predeterminado para algunos o todos los métodos de un trait en lugar de requerir implementaciones para todos los métodos en cada tipo. Entonces, cuando implementamos el trait en un tipo particular, podemos mantener o anular el comportamiento predeterminado de cada método.

En la Lista 10-14, especificamos una cadena predeterminada para el método `summarize` del trait `Summary` en lugar de solo definir la firma del método, como hicimos en la Lista 10-12.

Nombre de archivo: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Leer más...)")
    }
}
```

Lista 10-14: Definiendo un trait `Summary` con una implementación predeterminada del método `summarize`

Para usar la implementación predeterminada para resumir instancias de `NewsArticle`, especificamos un bloque `impl` vacío con `impl Summary for NewsArticle {}`.

Aunque ya no estamos definiendo directamente el método `summarize` en `NewsArticle`, hemos proporcionado una implementación predeterminada y especificado que `NewsArticle` implementa el trait `Summary`. Como resultado, todavía podemos llamar al método `summarize` en una instancia de `NewsArticle`, como esto:

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

Este código imprime `New article available! (Leer más...)`.

Crear una implementación predeterminada no requiere que cambiemos nada en la implementación de `Summary` en `Tweet` en la Lista 10-13. La razón es que la sintaxis para anular una implementación predeterminada es la misma que la sintaxis para implementar un método de trait que no tiene una implementación predeterminada.

Las implementaciones predeterminadas pueden llamar a otros métodos en el mismo trait, incluso si esos otros métodos no tienen una implementación predeterminada. De esta manera, un trait puede proporcionar mucha funcionalidad útil y solo requerir que los implementadores especifiquen una pequeña parte de ella. Por ejemplo, podríamos definir el trait `Summary` para tener un método `summarize_author` cuya implementación es requerida, y luego definir un método `summarize` que tiene una implementación predeterminada que llama al método `summarize_author`:

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Leer más de {}...)",
            self.summarize_author()
        )
    }
}
```

Para usar esta versión de `Summary`, solo necesitamos definir `summarize_author` cuando implementamos el trait en un tipo:

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

Después de definir `summarize_author`, podemos llamar a `summarize` en instancias del struct `Tweet`, y la implementación predeterminada de `summarize` llamará a la definición de `summarize_author` que hemos proporcionado. Debido a que hemos implementado `summarize_author`, el trait `Summary` nos ha dado el comportamiento del método `summarize` sin que tengamos que escribir más código. Aquí está cómo se ve:

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

Este código imprime `1 new tweet: (Leer más de @horse_ebooks...)`.

Tenga en cuenta que no es posible llamar a la implementación predeterminada desde una implementación que anula ese mismo método.
