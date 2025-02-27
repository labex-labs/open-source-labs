# 異なる型への変換としての遷移の実装

では、公開済みの投稿をどのようにして得るのでしょうか？ 下書き投稿は、公開される前にレビューと承認を受ける必要があるというルールを強制したいと思います。レビュー待ち状態の投稿もまだコンテントを表示してはいけません。これらの制約を実装するには、もう1つの構造体である`PendingReviewPost`を追加し、`DraftPost`に`request_review`メソッドを定義して`PendingReviewPost`を返し、`PendingReviewPost`に`approve`メソッドを定義して`Post`を返します。リスト17-20に示すようになります。

ファイル名: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

リスト17-20: `DraftPost`の`request_review`を呼び出すことで作成される`PendingReviewPost`と、`PendingReviewPost`を公開済みの`Post`に変換する`approve`メソッド

`request_review`メソッドと`approve`メソッドは`self`の所有権を取得します。そのため、`DraftPost`と`PendingReviewPost`のインスタンスを消費し、それぞれ`PendingReviewPost`と公開済みの`Post`に変換します。このようにすることで、`request_review`を呼び出した後に、余分な`DraftPost`インスタンスが残らなくなります。`PendingReviewPost`構造体には`content`メソッドが定義されておらず、`DraftPost`と同様に、そのコンテントを読もうとするとコンパイラエラーが発生します。定義された`content`メソッドを持つ公開済みの`Post`インスタンスを取得する唯一の方法は、`PendingReviewPost`の`approve`メソッドを呼び出すことであり、`PendingReviewPost`を取得する唯一の方法は、`DraftPost`の`request_review`メソッドを呼び出すことです。これで、ブログ投稿のワークフローを型システムにエンコードしました。

しかし、`main`にもいくつかの小さな変更を加える必要があります。`request_review`メソッドと`approve`メソッドは新しいインスタンスを返すため、呼び出された構造体を変更するわけではありません。そのため、返されたインスタンスを保存するために、より多くの`let post =`のシャドーイング代入を追加する必要があります。また、下書きとレビュー待ちの投稿のコンテントが空文字列であるというアサーションも必要ありません。必要ないのです。それらの状態の投稿のコンテントを使用しようとするコードは、もはやコンパイルできなくなっています。`main`の更新されたコードをリスト17-21に示します。

ファイル名: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

リスト17-21: ブログ投稿のワークフローの新しい実装を使用するための`main`の変更

`main`に再割り当てするために必要な変更は、この実装がもはや完全にオブジェクト指向の状態パターンに従っていないことを意味します。状態間の変換はもはや`Post`の実装内に完全にカプセル化されていません。ただし、型システムとコンパイル時に行われる型チェックのおかげで、現在は無効な状態が不可能になっています！ これにより、未公開の投稿のコンテントを表示するなどの特定のバグが本番環境に到達する前に見つかることが保証されます。

リスト17-21の後の`blog`クレートに対して、このセクションの最初で提案されたタスクを試してみて、このバージョンのコードの設計についてどう思うかを見てみてください。この設計では、一部のタスクは既に完了している場合があります。

Rustはオブジェクト指向のデザインパターンを実装できることがわかりましたが、Rustには状態を型システムにエンコードするなど、他のパターンもあります。これらのパターンには異なるトレードオフがあります。オブジェクト指向のパターンに非常に慣れているかもしれませんが、Rustの機能を生かして問題を再考することで、コンパイル時にいくつかのバグを防ぐなどの利点が得られます。所有権のような特定の機能のために、オブジェクト指向言語にはないため、オブジェクト指向のパターンが常にRustにおける最善の解決策であるとは限りません。
