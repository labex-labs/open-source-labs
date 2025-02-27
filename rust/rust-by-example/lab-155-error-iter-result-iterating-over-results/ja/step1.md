# `Result` の反復処理

`Iter::map` 操作は失敗する可能性があります。たとえば：

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

これを処理するための戦略を見ていきましょう。

## `filter_map()` で失敗した項目を無視する

`filter_map` は関数を呼び出し、`None` である結果をフィルタリングします。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Results: {:?}", numbers);
}
```

## `map_err()` と `filter_map()` で失敗した項目を収集する

`map_err` はエラーを引数に関数を呼び出すため、前の `filter_map` の解決策に追加することで、反復処理の間にそれらを別の場所に保存することができます。

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## `collect()` で全体の操作を失敗させる

`Result` は `FromIterator` を実装しており、結果のベクトル (`Vec<Result<T, E>>`) をベクトル付きの結果 (`Result<Vec<T>, E>`) に変換できます。`Result::Err` が見つかると、反復処理は終了します。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

同じ手法は `Option` でも使用できます。

## `partition()` ですべての有効な値と失敗を収集する

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

結果を見ると、すべてがまだ `Result` にラップされていることに気付くでしょう。これにはもう少しのボイラープレートが必要です。

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
