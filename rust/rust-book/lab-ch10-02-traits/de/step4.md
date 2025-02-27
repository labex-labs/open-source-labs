# Default Implementations

Manchmal ist es nützlich, standardmäßiges Verhalten für einige oder alle Methoden eines Traits zu haben, anstatt für jede Methode auf jedem Typ Implementierungen erforderlich zu machen. Dann, wenn wir das Trait auf einem bestimmten Typ implementieren, können wir das standardmäßige Verhalten jeder Methode beibehalten oder überschreiben.

In Listing 10-14 geben wir einen Standardstring für die `summarize`-Methode des `Summary`-Traits an, anstatt nur die Methodensignatur zu definieren, wie wir es in Listing 10-12 getan haben.

Dateiname: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

Listing 10-14: Definieren eines `Summary`-Traits mit einer Standardimplementierung der `summarize`-Methode

Um die Standardimplementierung zu verwenden, um Instanzen von `NewsArticle` zu zusammenfassen, geben wir einen leeren `impl`-Block mit `impl Summary for NewsArticle {}` an.

Auch wenn wir die `summarize`-Methode auf `NewsArticle` nicht mehr direkt definieren, haben wir eine Standardimplementierung bereitgestellt und angegeben, dass `NewsArticle` das `Summary`-Trait implementiert. Als Ergebnis können wir immer noch die `summarize`-Methode auf einer Instanz von `NewsArticle` aufrufen, wie folgt:

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

Dieser Code druckt `New article available! (Read more...)`.

Das Erstellen einer Standardimplementierung erfordert nicht, dass wir etwas an der Implementierung von `Summary` auf `Tweet` in Listing 10-13 ändern. Der Grund ist, dass die Syntax zum Überschreiben einer Standardimplementierung die gleiche ist wie die Syntax zur Implementierung einer Trait-Methode, die keine Standardimplementierung hat.

Standardimplementierungen können andere Methoden in demselben Trait aufrufen, auch wenn diese anderen Methoden keine Standardimplementierung haben. Auf diese Weise kann ein Trait viel nützliche Funktionalität bereitstellen und nur die Implementierenden dazu zwingen, einen kleinen Teil davon anzugeben. Beispielsweise könnten wir das `Summary`-Trait definieren, um eine `summarize_author`-Methode zu haben, deren Implementierung erforderlich ist, und dann eine `summarize`-Methode definieren, die eine Standardimplementierung hat, die die `summarize_author`-Methode aufruft:

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

Um diese Version von `Summary` zu verwenden, müssen wir nur `summarize_author` definieren, wenn wir das Trait auf einem Typ implementieren:

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

Nachdem wir `summarize_author` definiert haben, können wir `summarize` auf Instanzen der `Tweet`-Struktur aufrufen, und die Standardimplementierung von `summarize` wird die von uns bereitgestellte Definition von `summarize_author` aufrufen. Da wir `summarize_author` implementiert haben, hat uns das `Summary`-Trait das Verhalten der `summarize`-Methode ohne dass wir mehr Code schreiben mussten. So sieht das aus:

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

Dieser Code druckt `1 new tweet: (Read more from @horse_ebooks...)`.

Beachten Sie, dass es nicht möglich ist, die Standardimplementierung aus einer Überschreibungsimplementierung derselben Methode aufzurufen.
