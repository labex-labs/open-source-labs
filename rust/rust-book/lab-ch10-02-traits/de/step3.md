# Implementing a Trait on a Type

Jetzt, nachdem wir die gewünschten Signaturen der Methoden des `Summary`-Traits definiert haben, können wir es auf die Typen in unserem Medienaggregator implementieren. Listing 10-13 zeigt eine Implementierung des `Summary`-Traits auf der `NewsArticle`-Struktur, die die Überschrift, den Autor und den Ort verwendet, um den Rückgabewert von `summarize` zu erstellen. Für die `Tweet`-Struktur definieren wir `summarize` als Benutzernamen gefolgt vom gesamten Text des Tweets, unter der Annahme, dass der Tweetinhalt bereits auf 280 Zeichen begrenzt ist.

Dateiname: `src/lib.rs`

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

Listing 10-13: Implementieren des `Summary`-Traits auf den Typen `NewsArticle` und `Tweet`

Das Implementieren eines Traits auf einem Typ ähnelt der Implementierung von regulären Methoden. Der Unterschied besteht darin, dass wir nach `impl` den Namen des Traits schreiben, das wir implementieren möchten, dann das `for`-Schlüsselwort verwenden und anschließend den Namen des Typs angeben, für den wir das Trait implementieren möchten. Innerhalb des `impl`-Blocks schreiben wir die Methodensignaturen, die die Trait-Definition definiert hat. Anstatt nach jeder Signatur ein Semikolon hinzuzufügen, verwenden wir geschweifte Klammern und füllen den Methodenkörper mit dem spezifischen Verhalten aus, das wir für die Methoden des Traits für den bestimmten Typ haben möchten.

Jetzt, nachdem die Bibliothek das `Summary`-Trait auf `NewsArticle` und `Tweet` implementiert hat, können die Benutzer der Kiste die Trait-Methoden auf Instanzen von `NewsArticle` und `Tweet` auf die gleiche Weise aufrufen, wie wir reguläre Methoden aufrufen. Der einzige Unterschied besteht darin, dass der Benutzer das Trait sowie die Typen in den Geltungsbereich bringen muss. Hier ist ein Beispiel dafür, wie eine binäre Kiste unsere `aggregator`-Bibliothekskiste verwenden könnte:

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

Dieser Code druckt `1 new tweet: horse_ebooks: of course, as you probably already know, people`.

Andere Kisten, die von der `aggregator`-Kiste abhängen, können auch das `Summary`-Trait in den Geltungsbereich bringen, um `Summary` auf ihren eigenen Typen zu implementieren. Eine Einschränkung, die zu beachten ist, besteht darin, dass wir ein Trait nur auf einem Typ implementieren können, wenn entweder das Trait oder der Typ oder beide unserem Kasten lokal sind. Beispielsweise können wir Standardbibliotheks-Traits wie `Display` auf einem benutzerdefinierten Typ wie `Tweet` als Teil der Funktionalität unserer `aggregator`-Kiste implementieren, da der Typ `Tweet` unserem `aggregator`-Kasten lokal ist. Wir können auch `Summary` auf `Vec<T>` in unserer `aggregator`-Kiste implementieren, da das Trait `Summary` unserem `aggregator`-Kasten lokal ist.

Wir können jedoch externe Traits auf externe Typen nicht implementieren. Beispielsweise können wir das `Display`-Trait auf `Vec<T>` innerhalb unserer `aggregator`-Kiste nicht implementieren, da `Display` und `Vec<T>` beide in der Standardbibliothek definiert sind und unserem `aggregator`-Kasten nicht lokal sind. Diese Einschränkung ist Teil einer Eigenschaft namens _Kohärenz_, genauer gesagt der _Waisenregel_, die so benannt ist, weil der Elterntyp nicht vorhanden ist. Diese Regel gewährleistet, dass der Code anderer Leute Ihren Code nicht brechen kann und umgekehrt. Ohne die Regel könnten zwei Kisten das gleiche Trait für den gleichen Typ implementieren, und Rust würde nicht wissen, welche Implementierung zu verwenden.
