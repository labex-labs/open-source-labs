# ドキュメントテスト

Rust プロジェクトを文書化する主な方法は、ソースコードに注釈を付けることです。ドキュメントコメントは CommonMark Markdown 仕様で書かれ、コードブロックをサポートしています。Rust は正確性を保証するので、これらのコードブロックはコンパイルされ、ドキュメントテストとして使用されます。

````rust
/// 最初の行は関数を説明する短い概要です。
///
/// 次の行は詳細なドキュメントを示しています。コードブロックは
/// 3 つの逆クォートで始まり、内部に暗黙的な `fn main()` と
/// `extern crate <cratename>` があります。`doccomments` クレートをテストしていると仮定します:
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// 通常、ドキュメントコメントには "Examples"、"Panics"、"Failures" のセクションが含まれます。
///
/// 次の関数は 2 つの数を割ります。
///
/// # Examples
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// 2 番目の引数が 0 の場合、関数はパニックを起こします。
///
/// ```rust
/// // 0 での割り算でパニックを起こします
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }

    a / b
}
````

ドキュメント内のコードブロックは、通常の `cargo test` コマンドを実行すると自動的にテストされます:

```shell

```

## ドキュメントテストの目的

ドキュメントテストの主な目的は、機能をテストするための例として機能することです。これは、最も重要なガイドラインの 1 つです。これにより、ドキュメントからの例を完全なコードスニペットとして使用できます。ただし、`?` を使用するとコンパイルが失敗します。なぜなら `main` は `unit` を返すからです。ドキュメントから一部のソース行を非表示にする機能が役に立ちます。`fn try_main() -> Result<(), ErrorType>` を書き、非表示にして、非表示の `main` で `unwrap` します。難しそうですか？ 以下に例があります:

````rust
/// ドキュメントテストで非表示の `try_main` を使用する。
///
/// ```
/// # // 非表示の行は `#` 記号で始まりますが、まだコンパイル可能です！
/// # fn try_main() -> Result<(), String> { // ドキュメントに表示される本体をラップする行
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // try_main からの返却
/// # }
/// # fn main() { // unwrap() する main を開始
/// #    try_main().unwrap(); // try_main を呼び出して unwrap
/// #                         // エラーの場合にテストがパニックを起こすように
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divide-by-zero"))
    } else {
        Ok(a / b)
    }
}
````
