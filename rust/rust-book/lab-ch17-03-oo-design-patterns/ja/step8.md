# 型としての状態と動作のエンコード

状態パターンを再考して、異なる種類のトレードオフを得る方法を紹介します。外部コードが状態と遷移をまったく知らないように状態と遷移を完全にカプセル化する代わりに、状態を異なる型にエンコードします。その結果、Rust の型チェックシステムは、コンパイラエラーを発行することで、公開済みの投稿のみが許可される場所で下書き投稿を使用しようとする試みを防ぎます。

リスト 17-11 の`main`の最初の部分を考えてみましょう。

ファイル名：`src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

まだ、`Post::new`を使用して下書き状態の新しい投稿を作成し、投稿のコンテントにテキストを追加する機能を有効にしています。しかし、下書き投稿に空の文字列を返す`content`メソッドを持つ代わりに、下書き投稿には全く`content`メソッドがないようにします。そうすることで、下書き投稿のコンテントを取得しようとすると、メソッドが存在しないことを示すコンパイラエラーが表示されます。その結果、本番環境で下書き投稿のコンテントを偶然に表示することは不可能になります。なぜなら、そのコードはコンパイルされないからです。リスト 17-19 に`Post`構造体と`DraftPost`構造体の定義、およびそれぞれのメソッドを示します。

ファイル名：`src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

リスト 17-19: `content`メソッドを持つ`Post`と`content`メソッドを持たない`DraftPost`

`Post`構造体と`DraftPost`構造体の両方には、ブログ投稿のテキストを格納するプライベートな`content`フィールドがあります。構造体にはもはや`state`フィールドがなくなりました。なぜなら、状態のエンコードを構造体の型に移しているからです。`Post`構造体は公開済みの投稿を表し、`content`メソッドがあり、それが`content`を返します\[2\]。

`Post::new`関数はまだありますが、`Post`のインスタンスを返す代わりに、`DraftPost`のインスタンスを返します\[1\]。`content`はプライベートであり、`Post`を返す関数がないため、現在は`Post`のインスタンスを作成することはできません。

`DraftPost`構造体には`add_text`メソッドがあるため、以前と同じように`content`にテキストを追加できます\[3\]。ただし、`DraftPost`には`content`メソッドが定義されていないことに注意してください！これで、プログラムはすべての投稿が下書き投稿から始まり、下書き投稿のコンテントが表示できないことを保証します。これらの制約を回避しようとするすべての試みは、コンパイラエラーを引き起こします。
