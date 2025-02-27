# Стандартные реализации

Иногда полезно определить стандартное поведение для некоторых или всех методов в трейте, вместо того чтобы требовать реализацию для всех методов для каждого типа. Затем, когда мы реализуем трейт для конкретного типа, мы можем сохранить или переопределить стандартное поведение каждого метода.

В листинге 10-14 мы задаем стандартную строку для метода `summarize` трейта `Summary`, вместо того чтобы только определить сигнатуру метода, как мы это делали в листинге 10-12.

Имя файла: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

Листинг 10-14: Определение трейта `Summary` с стандартной реализацией метода `summarize`

Для использования стандартной реализации для суммаризации экземпляров `NewsArticle`, мы указываем пустой блок `impl` с `impl Summary for NewsArticle {}`.

Даже если мы больше не определяем метод `summarize` для `NewsArticle` напрямую, мы предоставили стандартную реализацию и указали, что `NewsArticle` реализует трейт `Summary`. В результате мы по-прежнему можем вызвать метод `summarize` для экземпляра `NewsArticle`, вот так:

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

Этот код выводит `New article available! (Read more...)`.

Создание стандартной реализации не требует от нас никаких изменений в реализации `Summary` для `Tweet` в листинге 10-13. Причина заключается в том, что синтаксис для переопределения стандартной реализации такой же, как и синтаксис для реализации метода трейта, для которого нет стандартной реализации.

Стандартные реализации могут вызывать другие методы в том же трейте, даже если эти другие методы не имеют стандартной реализации. Таким образом, трейт может предоставить много полезной функциональности и требовать от реализующих только указать небольшую часть из нее. Например, мы могли бы определить трейт `Summary` чтобы иметь метод `summarize_author`, реализация которого обязательна, а затем определить метод `summarize`, который имеет стандартную реализацию, которая вызывает метод `summarize_author`:

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Read more from {}...)",
            self.summarize_author()
        )
    }
}
```

Для использования этой версии `Summary`, нам нужно только определить `summarize_author`, когда мы реализуем трейт для типа:

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

После того, как мы определили `summarize_author`, мы можем вызвать `summarize` для экземпляров структуры `Tweet`, и стандартная реализация `summarize` вызовет определение `summarize_author`, которое мы предоставили. Поскольку мы реализовали `summarize_author`, трейт `Summary` предоставил нам поведение метода `summarize` не требуя от нас написания дополнительного кода. Вот как это выглядит:

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

Этот код выводит `1 new tweet: (Read more from @horse_ebooks...)`.

Обратите внимание, что невозможно вызвать стандартную реализацию из переопределяющей реализации того же метода.
