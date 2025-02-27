# 投稿の定義と下書き状態での新しいインスタンスの作成

さて、ライブラリの実装を始めましょう！ コンテンツを保持するパブリックな`Post`構造体が必要だとわかっているので、まずは構造体の定義と、`Post`のインスタンスを作成する関連するパブリックな`new`関数から始めます。リスト17-12に示すようになります。また、`Post`のすべての状態オブジェクトが持たなければならない動作を定義するプライベートな`State`トレイトも作成します。

そして、`Post`はプライベートなフィールド`state`の中の`Option<T>`の中に`Box<dyn State>`のトレイトオブジェクトを保持して、状態オブジェクトを保持します。少し後で`Option<T>`が必要な理由がわかります。

ファイル名: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

リスト17-12: `Post`構造体と新しい`Post`インスタンスを作成する`new`関数、`State`トレイト、および`Draft`構造体の定義

`State`トレイトは、異なる投稿状態で共有される動作を定義します。状態オブジェクトは`Draft`、`PendingReview`、および`Published`で、すべてが`State`トレイトを実装します。今のところ、トレイトにはメソッドはありません。投稿が始まる状態である`Draft`状態だけを定義して始めます。

新しい`Post`を作成するとき、その`state`フィールドを`Some`値に設定します。この`Some`値は`Box`を保持しています\[1\]。この`Box`は`Draft`構造体の新しいインスタンスを指しています。これにより、新しい`Post`インスタンスを作成するたびに、それが下書きとして始まることが保証されます。`Post`の`state`フィールドはプライベートなので、他の状態で`Post`を作成する方法はありません！ `Post::new`関数では、`content`フィールドを新しい空の`String`に設定します\[2\]。
