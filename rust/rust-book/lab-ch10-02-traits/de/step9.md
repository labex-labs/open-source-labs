# Returning Types That Implement Traits

Wir können auch die `impl Trait`-Syntax an der Rückgabetstelle verwenden, um einen Wert eines Typs zurückzugeben, der ein Trait implementiert, wie hier gezeigt:

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

Indem wir `impl Summary` für den Rückgabetyp verwenden, geben wir an, dass die `returns_summarizable`-Funktion einen Typ zurückgibt, der das `Summary`-Trait implementiert, ohne den konkreten Typ zu nennen. In diesem Fall gibt `returns_summarizable` ein `Tweet` zurück, aber der Code, der diese Funktion aufruft, muss das nicht wissen.

Die Möglichkeit, einen Rückgabetyp nur durch das Trait, das er implementiert, anzugeben, ist besonders nützlich im Zusammenhang mit Closures und Iterators, die wir im Kapitel 13 behandeln. Closures und Iterators erzeugen Typen, von denen nur der Compiler weiß, oder Typen, die sehr lang zu spezifizieren sind. Die `impl Trait`-Syntax ermöglicht es Ihnen, präzise anzugeben, dass eine Funktion einen Typ zurückgibt, der das `Iterator`-Trait implementiert, ohne einen sehr langen Typ schreiben zu müssen.

Wir können `impl Trait` jedoch nur verwenden, wenn wir einen einzelnen Typ zurückgeben. Beispielsweise würde dieser Code, der entweder ein `NewsArticle` oder ein `Tweet` zurückgibt, mit dem Rückgabetyp `impl Summary` nicht funktionieren:

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

Das Zurückgeben von entweder einem `NewsArticle` oder einem `Tweet` ist aufgrund von Einschränkungen bei der Implementierung der `impl Trait`-Syntax im Compiler nicht möglich. Wir werden im Abschnitt "Using Trait Objects That Allow for Values of Different Types" behandeln, wie man eine Funktion mit diesem Verhalten schreibt.
