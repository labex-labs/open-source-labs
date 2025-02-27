# Devolviendo Tipos que Implementan Traits

También podemos usar la sintaxis `impl Trait` en la posición de retorno para devolver un valor de algún tipo que implemente un trait, como se muestra aquí:

```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```

Al usar `impl Summary` para el tipo de retorno, especificamos que la función `returns_summarizable` devuelve algún tipo que implementa el trait `Summary` sin nombrar el tipo concrete. En este caso, `returns_summarizable` devuelve un `Tweet`, pero el código que llama a esta función no necesita saber eso.

La capacidad de especificar un tipo de retorno solo por el trait que implementa es especialmente útil en el contexto de closures e iteradores, que cubrimos en el Capítulo 13. Los closures e iteradores crean tipos que solo el compilador conoce o tipos que son muy largos de especificar. La sintaxis `impl Trait` te permite especificar concisamente que una función devuelve algún tipo que implementa el trait `Iterator` sin necesidad de escribir un tipo muy largo.

Sin embargo, solo puedes usar `impl Trait` si estás devolviendo un solo tipo. Por ejemplo, este código que devuelve ya sea un `NewsArticle` o un `Tweet` con el tipo de retorno especificado como `impl Summary` no funcionaría:

```rust
fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}
```

Devolver ya sea un `NewsArticle` o un `Tweet` no está permitido debido a las restricciones sobre cómo se implementa la sintaxis `impl Trait` en el compilador. Cubriremos cómo escribir una función con este comportamiento en "Usando Objetos de Trait que Permiten Valores de Diferentes Tipos".
