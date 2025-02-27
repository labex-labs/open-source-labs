# エラーを伝播するためのショートカット: 疑問符演算子 `?`

リスト 9-7 は、リスト 9-6 と同じ機能を持つ `read_username_from_file` の実装を示していますが、この実装では疑問符演算子 `?` を使用しています。

ファイル名: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

リスト 9-7: 疑問符演算子 `?` を使ってエラーを呼び出し元のコードに返す関数

`Result` 値の後に置かれた `?` は、リスト 9-6 で `Result` 値を処理するために定義した `match` 式とほぼ同じように動作するように定義されています。`Result` の値が `Ok` の場合、`Ok` 内の値がこの式から返され、プログラムは続行します。値が `Err` の場合、`return` キーワードを使用した場合と同じように、`Err` が関数全体から返され、エラー値が呼び出し元のコードに伝播されます。

リスト 9-6 の `match` 式と `?` 演算子の違いは、`?` 演算子が呼び出されるエラー値が、標準ライブラリの `From` トレイトに定義された `from` 関数を通ることです。この関数は、値をある型から別の型に変換するために使用されます。`?` 演算子が `from` 関数を呼び出すとき、受け取ったエラー型が、現在の関数の戻り値の型で定義されたエラー型に変換されます。これは、関数が 1 つのエラー型を返して、関数が失敗するすべての方法を表す場合に便利です。たとえば、関数が失敗する理由がたくさんあっても、それぞれが異なる理由で失敗する場合でも、1 つのエラー型で表現できるようになります。

たとえば、リスト 9-7 の `read_username_from_file` 関数を変更して、独自に定義した `OurError` というカスタムエラー型を返すようにすることができます。また、`impl From<io::Error> for OurError` を定義して、`io::Error` から `OurError` のインスタンスを構築するようにすれば、`read_username_from_file` の本体での `?` 演算子の呼び出しは `from` を呼び出し、エラー型を変換します。このとき、関数にさらにコードを追加する必要はありません。

リスト 9-7 のコンテキストでは、`File::open` 呼び出しの末尾の `?` は、`Ok` 内の値を `username_file` 変数に返します。エラーが発生した場合、`?` 演算子は関数全体から早期に返され、`Err` 値を呼び出し元のコードに渡します。`read_to_string` 呼び出しの末尾の `?` も同じです。

`?` 演算子は、多くの定型コードを削除し、この関数の実装を簡単にします。また、`?` の直後にメソッド呼び出しをチェーン化することで、さらにコードを短縮することができます。これをリスト 9-8 に示します。

ファイル名: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

リスト 9-8: `?` 演算子の後にメソッド呼び出しをチェーン化する

`username` 内の新しい `String` の作成を関数の先頭に移動しました。この部分は変更されていません。`username_file` 変数を作成する代わりに、`File::open("hello.txt")?` の結果に直接 `read_to_string` の呼び出しをチェーン化しました。`read_to_string` 呼び出しの末尾には依然として `?` があり、`File::open` と `read_to_string` の両方が成功した場合には、エラーを返す代わりに `username` を含む `Ok` 値を返します。機能は再びリスト 9-6 とリスト 9-7 と同じです。これは、書き方が異なり、より使いやすい方法です。

リスト 9-9 は、`fs::read_to_string` を使ってさらに短くする方法を示しています。

ファイル名: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

リスト 9-9: ファイルを開いてから読み取る代わりに `fs::read_to_string` を使用する

文字列を使ってファイルを読み取ることはかなり一般的な操作です。そのため、標準ライブラリには便利な `fs::read_to_string` 関数が用意されています。この関数は、ファイルを開き、新しい `String` を作成し、ファイルの内容を読み取り、その内容をその `String` に入れて返します。もちろん、`fs::read_to_string` を使うと、すべてのエラー処理を説明する機会がなくなるので、最初に長い方法でやってみました。
