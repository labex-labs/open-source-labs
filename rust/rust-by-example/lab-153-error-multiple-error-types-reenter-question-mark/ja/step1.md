# `?` のその他の使い方

前の例では、`parse` を呼び出したときの即時の反応が、ライブラリのエラーをボックス化されたエラーに `map` することであることに注意してください。

```rust
.and_then(|s| s.parse::<i32>())
 .map_err(|e| e.into())
```

これは単純で一般的な操作なので、省略できると便利です。残念ながら、`and_then` は十分に柔軟でないため、省略できません。ただし、代わりに `?` を使うことができます。

`?` は以前、`unwrap` または `return Err(err)` として説明されていました。これは概ね正しいです。実際の意味は `unwrap` または `return Err(From::from(err))` です。`From::from` は異なる型間の変換ユーティリティなので、エラーが戻り型に変換可能な場合に `?` を使うと、自動的に変換されます。

ここでは、前の例を `?` を使って書き直します。結果として、エラー型に対して `From::from` が実装されている場合、`map_err` は消えます。

```rust
use std::error;
use std::fmt;

// エイリアスを `Box<dyn error::Error>` に変更します。
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// 以前と同じ構造ですが、すべての `Result` と `Options` をチェーン化する代わりに、
// 内側の値をすぐに取り出すために `?` を使います。
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
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

これは実際にはかなりクリーンになっています。元の `panic` と比較すると、`unwrap` の呼び出しを `?` に置き換えるのと非常に似ていますが、戻り型が `Result` であることが違います。その結果、最上位で破壊的に解釈する必要があります。
