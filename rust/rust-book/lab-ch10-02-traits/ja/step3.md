# 型にトレイトを実装する

これで、`Summary` トレイトのメソッドの望ましいシグネチャを定義したので、メディアアグリゲータの型に対してそれを実装することができます。リスト10-13は、見出し、著者、場所を使って `summarize` の返却値を作成する `NewsArticle` 構造体に対する `Summary` トレイトの実装を示しています。`Tweet` 構造体については、ツイートの内容が既に280文字に制限されていると仮定して、`summarize` をユーザー名に続けてツイートの全文として定義します。

ファイル名: `src/lib.rs`

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

リスト10-13: `NewsArticle` 型と `Tweet` 型に対する `Summary` トレイトの実装

型にトレイトを実装することは、通常のメソッドを実装することと似ています。違いは、`impl` の後に、実装したいトレイト名を書き、その後に `for` キーワードを使って、トレイトを実装したい型の名前を指定することです。`impl` ブロックの中には、トレイト定義で定義されたメソッドのシグネチャを書きます。各シグネチャの後にセミコロンを追加する代わりに、波括弧を使って、トレイトのメソッドが特定の型に対して持つべき特定の振る舞いでメソッド本体を埋めます。

ライブラリが `NewsArticle` と `Tweet` に対して `Summary` トレイトを実装したので、クレートのユーザーは、通常のメソッドを呼ぶのと同じ方法で、`NewsArticle` と `Tweet` のインスタンスに対してトレイトメソッドを呼ぶことができます。唯一の違いは、ユーザーがトレイトと型の両方をスコープに持たなければならないことです。ここでは、バイナリクレートが私たちの `aggregator` ライブラリクレートをどのように使うかの例を示します。

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

このコードは `1 new tweet: horse_ebooks: of course, as you probably already know, people` を出力します。

`aggregator` クレートに依存する他のクレートも、独自の型に対して `Summary` を実装するために、`Summary` トレイトをスコープに持つことができます。留意すべき制限は、トレイトまたは型のどちらか一方、または両方が私たちのクレートにローカルである場合にのみ、型に対してトレイトを実装できるということです。たとえば、`Tweet` のようなカスタム型に対して `Display` のような標準ライブラリのトレイトを実装することができます。これは、私たちの `aggregator` クレートの機能の一部として、型 `Tweet` が私たちの `aggregator` クレートにローカルであるためです。また、私たちの `aggregator` クレートの中で `Vec<T>` に対して `Summary` を実装することもできます。これは、トレイト `Summary` が私たちの `aggregator` クレートにローカルであるためです。

しかし、外部の型に対して外部のトレイトを実装することはできません。たとえば、私たちの `aggregator` クレートの中で `Vec<T>` に対して `Display` トレイトを実装することはできません。なぜなら、`Display` と `Vec<T>` の両方が標準ライブラリに定義されており、私たちの `aggregator` クレートにはローカルではないからです。この制限は、「整合性」と呼ばれる特性の一部であり、より具体的には「孤立則」と呼ばれています。この名前の由来は、親型が存在しないためです。このルールは、他人のコードが自分のコードを破壊しないように、逆も同様に保証します。このルールがなければ、2つのクレートが同じ型に対して同じトレイトを実装することができ、Rustはどの実装を使うかを知ることができません。
