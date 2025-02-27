# `Result`

`Result` は、`Option` 型の拡張版で、値の存在しない可能性ではなく、潜在的な _エラー_ を表します。

すなわち、`Result<T, E>` は 2 つの結果のいずれかを持つことができます。

- `Ok(T)`: 要素 `T` が見つかりました
- `Err(E)`: 要素 `E` でエラーが見つかりました

慣例として、期待される結果は `Ok` で、予期しない結果は `Err` です。

`Option` と同様に、`Result` には多くの関連メソッドがあります。たとえば、`unwrap()` は要素 `T` を返すか、`panic` します。ケースの処理には、`Result` と `Option` の間に重複する多くのコンビネータがあります。

Rust を使っているとき、`parse()` メソッドのように `Result` 型を返すメソッドに遭遇することが多いでしょう。文字列を他の型にパースできるとは限らないため、`parse()` は失敗の可能性を示す `Result` を返します。

文字列の `parse()` に成功した場合と失敗した場合を見てみましょう。

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // `unwrap()` を使って数値を取得してみましょう。エラーになりますか？
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

失敗した場合、`parse()` は `unwrap()` による `panic` のためのエラーを残します。また、`panic` はプログラムを終了し、不快なエラー メッセージを表示します。

エラー メッセージの品質を向上させるには、戻り値の型をもっと具体的にし、エラーを明示的に処理することを検討する必要があります。

## `main` での `Result` の使用

`Result` 型は、明示的に指定することで `main` 関数の戻り値とすることもできます。通常、`main` 関数は次の形式になります。

```rust
fn main() {
    println!("Hello World!");
}
```

しかし、`main` は `Result` の戻り値型も持つことができます。`main` 関数内でエラーが発生した場合、エラー コードを返し、エラーのデバッグ表現を表示します (`[`Debug`]` トレイトを使用)。次の例はそのようなシナリオを示し、[次のセクション] で扱う内容に触れています。

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
