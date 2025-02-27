# エラー時のパニックのショートカット: unwrap と expect

`match` を使うのは十分に機能しますが、少し冗長で、意図をうまく伝えることができない場合があります。`Result<T, E>` 型には、さまざまなより具体的なタスクを行うために定義された多くのヘルパーメソッドがあります。`unwrap` メソッドは、リスト 9-4 で書いた `match` 式と同じように実装されたショートカットメソッドです。`Result` 値が `Ok` バリアントの場合、`unwrap` は `Ok` 内の値を返します。`Result` が `Err` バリアントの場合、`unwrap` は代わりに `panic!` マクロを呼び出します。以下は、`unwrap` の動作例です。

ファイル名: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

このコードを _hello.txt_ ファイルがない状態で実行すると、`unwrap` メソッドが行う `panic!` 呼び出しからのエラーメッセージが表示されます。

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

同様に、`expect` メソッドを使うと、`panic!` エラーメッセージも選択できます。`unwrap` の代わりに `expect` を使って、適切なエラーメッセージを提供することで、意図を伝えることができ、パニックの原因を特定する作業が容易になります。`expect` の構文は次のようになります。

ファイル名: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt should be included in this project");
}
```

`expect` を使う方法は `unwrap` と同じです。ファイルハンドルを返すか、`panic!` マクロを呼び出します。`expect` が `panic!` を呼び出す際に使用するエラーメッセージは、`unwrap` が使用する既定の `panic!` メッセージではなく、`expect` に渡すパラメータになります。以下がその様子です。

    thread 'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

本番向きのコードでは、ほとんどの Rust プログラマは `unwrap` の代わりに `expect` を選択し、操作が常に成功するはずの理由に関するより多くのコンテキストを提供します。そうすることで、仮定が誤っていることが判明した場合、デバッグに役立つ情報がより多く得られます。
