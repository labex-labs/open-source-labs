# ドキュメント

`cargo doc` を使って `target/doc` にドキュメントを生成します。

`cargo test` を使ってすべてのテスト（ドキュメントテストも含む）を実行し、`cargo test --doc` を使ってドキュメントテストのみを実行します。

これらのコマンドは、必要に応じて適切に `rustdoc`（および `rustc`）を呼び出します。

## ドキュメントコメント

ドキュメントが必要な大規模なプロジェクトにとって、ドキュメントコメントは非常に便利です。`rustdoc` を実行するとき、これらのコメントがドキュメントにコンパイルされます。これらは `///` で表され、\[Markdown\] をサポートしています。

````rust
#![crate_name = "doc"]

/// ここでは人間が表現されています
pub struct Person {
    /// 人には必ず名前が必要です。ジュリエットがそれをどれほど嫌っていようとも
    name: String,
}

impl Person {
    /// 与えられた名前の人を返します
    ///
    /// # 引数
    ///
    /// * `name` - 人の名前を保持する文字列スライス
    ///
    /// # 例
    ///
    /// ```
    /// // コメント内のフェンスの中にrustコードを記述できます
    /// // `rustdoc` に `--test` を渡すと、自動的にテストしてくれます！
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// 親切な挨拶をします！
    ///
    /// 呼び出された `Person` に対して "Hello, [name](Person::name)" と言います。
    pub fn hello(& self) {
        println!("Hello, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

テストを実行するには、まずコードをライブラリとしてビルドし、次に `rustdoc` にライブラリがある場所を伝えて、各ドキュメントテストプログラムにリンクできるようにします。

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## ドキュメント属性

以下は、`rustdoc` とともに使用される最も一般的な `#[doc]` 属性のいくつかの例です。

## `inline`

ドキュメントをインラインにするために使用します。個別のページにリンクする代わりに。

```rust
#[doc(inline)]
pub use bar::Bar;

/// barのドキュメント
mod bar {
    /// Barのドキュメント
    pub struct Bar;
}
```

## `no_inline`

個別のページや他の場所にリンクすることを防ぐために使用します。

```rust
// libcore/preludeからの例
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

これを使用すると、`rustdoc` にこれをドキュメントに含めないように伝えます。

```rust
// futures-rsライブラリからの例
#[doc(hidden)]
pub use self::async_await::*;
```

ドキュメントに関しては、コミュニティによって `rustdoc` が広く使用されています。これが \[stdライブラリのドキュメント\](https://doc.rust-lang.org/std/) を生成するために使用されています。
