# デフォルト実装

あるトレイトの一部またはすべてのメソッドに対して、すべての型に対するすべてのメソッドの実装を要求する代わりに、デフォルトの振る舞いを持つことが便利な場合があります。そして、特定の型に対してトレイトを実装する際には、各メソッドのデフォルトの振る舞いを維持または上書きすることができます。

リスト10-12で行ったように、メソッドのシグネチャのみを定義する代わりに、リスト10-14では、`Summary` トレイトの `summarize` メソッドに対してデフォルトの文字列を指定しています。

ファイル名: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

リスト10-14: `summarize` メソッドのデフォルト実装を持つ `Summary` トレイトの定義

`NewsArticle` のインスタンスを要約するためにデフォルト実装を使用するには、`impl Summary for NewsArticle {}` という空の `impl` ブロックを指定します。

`NewsArticle` で直接 `summarize` メソッドを定義しなくなったとしても、デフォルト実装を提供し、`NewsArticle` が `Summary` トレイトを実装することを指定しています。その結果、以下のように、`NewsArticle` のインスタンスでも依然として `summarize` メソッドを呼び出すことができます。

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

このコードは `New article available! (Read more...)` を出力します。

デフォルト実装を作成することで、リスト10-13の `Tweet` に対する `Summary` の実装については何も変更する必要はありません。その理由は、デフォルト実装を上書きする構文が、デフォルト実装のないトレイトメソッドを実装する構文と同じであるためです。

デフォルト実装は、同じトレイト内の他のメソッドを呼び出すことができます。たとえそれらの他のメソッドにデフォルト実装がなくてもです。このように、トレイトは多くの便利な機能を提供し、実装者にその一部のみを指定するように要求するだけです。たとえば、`Summary` トレイトに、実装が必要な `summarize_author` メソッドを持たせ、その後、`summarize_author` メソッドを呼び出すデフォルト実装を持つ `summarize` メソッドを定義することができます。

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

このバージョンの `Summary` を使用するには、型に対してトレイトを実装する際に `summarize_author` のみを定義すればよいです。

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

`summarize_author` を定義した後、`Tweet` 構造体のインスタンスで `summarize` を呼び出すことができ、`summarize` のデフォルト実装が私たちが提供した `summarize_author` の定義を呼び出します。`summarize_author` を実装したため、`Summary` トレイトは、私たちにもうコードを書かなくても `summarize` メソッドの振る舞いを与えてくれます。これがどのように見えるかは以下の通りです。

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

このコードは `1 new tweet: (Read more from @horse_ebooks...)` を出力します。

同じメソッドの上書き実装からデフォルト実装を呼び出すことはできないことに注意してください。
