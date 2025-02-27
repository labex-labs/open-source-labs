# `Option` から `Result` を抜き出す

混合エラー型を扱う最も基本的な方法は、それらを相互に埋め込むことです。

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    })
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(numbers));

    println!("The first doubled is {:?}", double_first(empty));
    // エラー 1: 入力ベクトルが空です

    println!("The first doubled is {:?}", double_first(strings));
    // エラー 2: 要素が数値にパースできません
}
```

エラーが発生したときに処理を停止する場合（`?` を使う場合など）がありますが、`Option` が `None` の場合は処理を続けたいときもあります。`Result` と `Option` を入れ替えるのに便利なコンビネータがいくつかあります。

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    });

    opt.map_or(Ok(None), |r| r.map(Some))
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(numbers));
    println!("The first doubled is {:?}", double_first(empty));
    println!("The first doubled is {:?}", double_first(strings));
}
```
