# contentの動作を変更するためのapproveの追加

`approve`メソッドは`request_review`メソッドと似ています。それは、現在の状態が承認された場合にその状態が持つべき値に`state`を設定します。リスト17-16に示すようになります。

ファイル名: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

リスト17-16: `Post`と`State`トレイトに`approve`メソッドを実装する

`approve`メソッドを`State`トレイトに追加し、`State`を実装する新しい構造体である`Published`状態を追加します。

`PendingReview`の`request_review`と同じように動作します。`Draft`に`approve`メソッドを呼び出した場合、`approve`が`self`を返すため、何の影響もありません\[1\]。`PendingReview`に`approve`を呼び出した場合、`Published`構造体の新しいボックス化されたインスタンスを返します\[2\]。`Published`構造体は`State`トレイトを実装しており、`request_review`メソッドと`approve`メソッドの両方で、それ自体を返します。なぜなら、それらの場合には投稿が`Published`状態のままになるからです。

次に、`Post`の`content`メソッドを更新する必要があります。`content`から返される値が`Post`の現在の状態に依存するようにしたいので、`Post`がその`state`に定義された`content`メソッドに委譲するようにします。リスト17-17に示すようになります。

ファイル名: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

リスト17-17: `Post`の`content`メソッドを更新して、`State`の`content`メソッドに委譲する

これらのルールをすべて`State`を実装する構造体の中に保持することが目的であるため、`state`の値に対して`content`メソッドを呼び出し、投稿インスタンス（つまり、`self`）を引数として渡します。そして、`state`値の`content`メソッドを使用して返される値を返します。

`Option`に対して`as_ref`メソッドを呼び出します。なぜなら、`Option`の中の値の参照が必要であり、値の所有権は必要ないからです。`state`は`Option<Box<dyn State>>`なので、`as_ref`を呼び出すと、`Option<&Box<dyn State>>`が返されます。`as_ref`を呼び出さなければ、エラーが発生します。なぜなら、関数パラメータの借用された`&self`から`state`を移動させることはできないからです。

その後、`unwrap`メソッドを呼び出します。これは、`Post`のメソッドが完了したときに`state`が常に`Some`値を含むことを保証するため、決してパニックにならないことがわかっています。これは、コンパイラがそれを理解できなくても、`None`値が決してあり得ないことを知っている「コンパイラよりも多くの情報を持つケース」の1つです。

この時点で、`&Box<dyn State>`に対して`content`を呼び出すと、`&`と`Box`に対してderef強制が効果します。そのため、`content`メソッドは最終的に`State`トレイトを実装する型に対して呼び出されます。つまり、`content`を`State`トレイト定義に追加する必要があります。そして、どの状態にあるかに応じて返すコンテンツのロジックを置く場所になります。リスト17-18に示すようになります。

ファイル名: `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

リスト17-18: `State`トレイトに`content`メソッドを追加する

`content`メソッドのデフォルト実装を追加して、空の文字列スライスを返すようにします\[1\]。つまり、`Draft`と`PendingReview`構造体に`content`を実装する必要はありません。`Published`構造体は`content`メソッドをオーバーライドして、`post.content`の値を返します\[2\]。

第10章で説明したように、このメソッドには寿命注釈が必要です。`post`の参照を引数として取り、その`post`の一部の参照を返しているので、返される参照の寿命は`post`引数の寿命に関連しています。

これで完了です。リスト17-11のすべてが正常に動作します！ ブログ投稿のワークフローのルールを持つ状態パターンを実装しました。ルールに関連するロジックは状態オブジェクトの中にあり、`Post`全体に散らばっているわけではありません。

> **なぜenumを使わないのか？**
>
> 投稿の状態を変数として持つ`enum`を使わなかった理由が疑問に思われるかもしれません。それは確かに解決策の1つです。試してみて、最終結果を比較して、どちらが好きかを判断してみてください！ `enum`を使う欠点の1つは、`enum`の値をチェックするすべての場所に`match`式やそれに似たものが必要になることです。これは、このトレイトオブジェクトの解決策よりも繰り返しが多くなる可能性があります。
