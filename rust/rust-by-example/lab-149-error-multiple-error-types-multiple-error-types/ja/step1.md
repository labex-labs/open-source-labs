# 複数のエラー型

以前の例は常に非常に便利でした。`Result` は他の `Result` と相互作用し、`Option` は他の `Option` と相互作用します。

時には、`Option` が `Result` と相互作用する必要があり、または `Result<T, Error1>` が `Result<T, Error2>` と相互作用する必要があります。そのような場合、私たちは異なるエラー型を、それらが組み合わせやすく相互作用しやすいように管理したいと考えます。

次のコードでは、`unwrap` の2つのインスタンスが異なるエラー型を生成します。`Vec::first` は `Option` を返し、`parse::<i32>` は `Result<i32, ParseIntError>` を返します。

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // エラー1を生成
    2 * first.parse::<i32>().unwrap() // エラー2を生成
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // エラー1: 入力ベクトルが空です

    println!("The first doubled is {}", double_first(strings));
    // エラー2: 要素が数値にパースできません
}
```

次のセクションでは、この種の問題を処理するためのいくつかの戦略を見ていきます。
