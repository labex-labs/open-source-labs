# エラーのラップ

エラーをボクシングする代わりに、独自のエラー型にエラーをラップすることができます。

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // それらのエラーのエラー実装に委譲します。
    // 追加情報を提供するには、型に追加のデータを追加する必要があります。
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "please use a vector with at least one element"),
            // ラップされたエラーには追加情報が含まれており、
            // source() メソッドを介して利用できます。
            DoubleError::Parse(..) =>
                write!(f, "the provided string could not be parsed as int"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // 原因は基礎となる実装エラー型です。暗黙的に
            // トレイトオブジェクト `&error::Error` にキャストされます。これは、
            // 基礎となる型が既に `Error` トレイトを実装しているため機能します。
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// `ParseIntError` から `DoubleError` への変換を実装します。
// `ParseIntError` が `DoubleError` に変換される必要がある場合、
// `?` によってこれが自動的に呼び出されます。
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // ここでは、`DoubleError` を作成するために、
    // `From` の `ParseIntError` 実装（上で定義したもの）を暗黙的に使用しています。
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
        Err(e) => {
            println!("Error: {}", e);
            if let Some(source) = e.source() {
                println!("  Caused by: {}", source);
            }
        },
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```

これはエラーを処理するための少し多くの定型コードを追加しますが、すべてのアプリケーションで必要とされるわけではありません。定型コードを代わりに処理してくれるライブラリもいくつかあります。
