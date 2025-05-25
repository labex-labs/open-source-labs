# Retornando Tipos que Implementam Traits

Também podemos usar a sintaxe `impl Trait` na posição de retorno para retornar um valor de algum tipo que implementa um trait, como mostrado aqui:

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

Ao usar `impl Summary` para o tipo de retorno, especificamos que a função `returns_summarizable` retorna algum tipo que implementa o trait `Summary` sem nomear o tipo concreto. Neste caso, `returns_summarizable` retorna um `Tweet`, mas o código que chama esta função não precisa saber disso.

A capacidade de especificar um tipo de retorno apenas pelo trait que ele implementa é especialmente útil no contexto de closures e iteradores, que abordamos no Capítulo 13. Closures e iteradores criam tipos que apenas o compilador conhece ou tipos que são muito longos para especificar. A sintaxe `impl Trait` permite que você especifique concisamente que uma função retorna algum tipo que implementa o trait `Iterator` sem precisar escrever um tipo muito longo.

No entanto, você só pode usar `impl Trait` se estiver retornando um único tipo. Por exemplo, este código que retorna um `NewsArticle` ou um `Tweet` com o tipo de retorno especificado como `impl Summary` não funcionaria:

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

Retornar um `NewsArticle` ou um `Tweet` não é permitido devido a restrições em torno de como a sintaxe `impl Trait` é implementada no compilador. Abordaremos como escrever uma função com este comportamento em "Usando Objetos de Trait que Permitem Valores de Diferentes Tipos".
