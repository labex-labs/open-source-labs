# エラーのボックス化

元のエラーを保持しながらシンプルなコードを書く方法の 1 つは、それらを「ボックス化」することです。欠点は、潜在的なエラー型が実行時にのみ判明し、静的には決定されないことです。

標準ライブラリは、`Box` が `From` を介して `Error` トレイトを実装する任意の型からトレイトオブジェクト `Box<Error>` への変換を実装することで、エラーのボックス化を支援します。

```rust
use std::error;
use std::fmt;

// エイリアスを `Box<error::Error>` に変更します。
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // Box に変換
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // Box に変換
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
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
