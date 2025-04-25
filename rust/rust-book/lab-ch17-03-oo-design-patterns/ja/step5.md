# レビュー依頼により投稿の状態が変更される

次に、投稿のレビュー依頼機能を追加する必要があります。これにより、投稿の状態が`Draft`から`PendingReview`に変更されるはずです。リスト 17-15 にこのコードを示します。

ファイル名：`src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

リスト 17-15: `Post`と`State`トレイトに`request_review`メソッドを実装する

`Post`には、`self`への可変参照を取る`request_review`という名前のパブリックメソッドを与えます\[1\]。その後、`Post`の現在の状態に対して内部の`request_review`メソッドを呼び出します\[3\]。この 2 番目の`request_review`メソッドは、現在の状態を消費して新しい状態を返します。

`request_review`メソッドを`State`トレイトに追加します\[4\]。このトレイトを実装するすべての型は、今後`request_review`メソッドを実装する必要があります。メソッドの最初のパラメータとして`self`、`&self`、または`&mut self`ではなく、`self: Box<Self>`があることに注意してください。この構文は、メソッドが`Box`に保持された型で呼び出された場合にのみ有効であることを意味します。この構文は`Box<Self>`の所有権を取得し、古い状態を無効にします。そのため、`Post`の状態値を新しい状態に変換できます。

古い状態を消費するために、`request_review`メソッドは状態値の所有権を取得する必要があります。ここで`Post`の`state`フィールドにある`Option`が役に立ちます。`take`メソッドを呼び出して、`state`フィールドから`Some`値を取り出し、その代わりに`None`を残します。なぜなら、Rust は構造体に未初期化のフィールドを持たせないからです\[2\]。これにより、`state`値を`Post`から移動させて、借用する代わりに所有権を取得できます。その後、投稿の`state`値をこの操作の結果に設定します。

`state`値の所有権を取得するために、`self.state = self.state.request_review();`のようなコードで直接設定する代わりに、一時的に`state`を`None`に設定する必要があります。これにより、`Post`が古い`state`値を新しい状態に変換した後に使用できないようになります。

`Draft`の`request_review`メソッドは、新しい`PendingReview`構造体の新しいボックス化されたインスタンスを返します\[5\]。これは、投稿がレビューを待っている状態を表します。`PendingReview`構造体も`request_review`メソッドを実装していますが、変換は行いません。むしろ、それ自体を返します\[6\]。なぜなら、`PendingReview`状態にある既存の投稿にレビュー依頼を行った場合、それは`PendingReview`状態のままになるからです。

今では、状態パターンの利点がわかり始めました。`Post`の`request_review`メソッドは、その`state`値に関係なく同じです。各状態は独自のルールを担っています。

`Post`の`content`メソッドはそのままにして、空の文字列スライスを返します。今では、`PendingReview`状態と`Draft`状態の両方で`Post`を持つことができますが、`PendingReview`状態でも同じ動作が望まれます。リスト 17-11 は今では\[5\]までの行まで正常に動作します！
