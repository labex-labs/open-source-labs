# Возвращение типов, реализующих трейты

Мы также можем использовать синтаксис `impl Trait` в позиции возврата, чтобы вернуть значение некоторого типа, который реализует трейт, как показано здесь:

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

С использованием `impl Summary` для типа возврата мы указываем, что функция `returns_summarizable` возвращает какой-то тип, реализующий трейт `Summary`, не именуя конкретный тип. В этом случае `returns_summarizable` возвращает `Tweet`, но код, вызывающий эту функцию, не должен знать об этом.

Возможность указывать тип возврата только по трейту, который он реализует, особенно полезна в контексте замыканий и итераторов, о которых мы говорим в главе 13. Замыкания и итераторы создают типы, которые знает только компилятор, или типы, которые очень длинно задавать. Синтаксис `impl Trait` позволяет кратко указать, что функция возвращает какой-то тип, реализующий трейт `Iterator`, не нужно писать очень длинный тип.

Однако вы можете использовать `impl Trait` только если возвращаете один тип. Например, этот код, который возвращает либо `NewsArticle`, либо `Tweet` с типом возврата, заданным как `impl Summary`, не сработает:

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

Возвращение либо `NewsArticle`, либо `Tweet` не допускается из-за ограничений, связанных с тем, как синтаксис `impl Trait` реализован в компиляторе. Мы рассмотрим, как написать функцию с таким поведением в разделе "Использование объектов трейта, которые допускают значения разных типов".
