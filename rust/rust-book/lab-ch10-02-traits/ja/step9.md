# トレイトを実装する戻り値の型

戻り値の位置でも`impl Trait`構文を使って、トレイトを実装するある型の値を返すことができます。次のようになります。

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

戻り値の型として`impl Summary`を使うことで、`returns_summarizable`関数が具体的な型を指定せずに`Summary`トレイトを実装するある型を返すことを指定します。この場合、`returns_summarizable`は`Tweet`を返しますが、この関数を呼び出すコードはそれを知る必要はありません。

実装するトレイトだけで戻り値の型を指定できる機能は、第13章で扱うクロージャと反復子のコンテキストで特に役立ちます。クロージャと反復子は、コンパイラだけが知る型や指定するのに非常に長い型を作成します。`impl Trait`構文を使うと、反復子トレイトを実装するある型を関数が返すことを簡潔に指定でき、非常に長い型を書き出す必要がなくなります。

ただし、戻り値が1つの型の場合にのみ`impl Trait`を使うことができます。たとえば、戻り値の型を`impl Summary`と指定して`NewsArticle`または`Tweet`を返すこのコードは動作しません。

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

コンパイラにおける`impl Trait`構文の実装方法に関する制限のため、`NewsArticle`または`Tweet`を返すことは許可されていません。「異なる型の値を許容するトレイトオブジェクトの使用」でこの動作を持つ関数を書く方法について説明します。
