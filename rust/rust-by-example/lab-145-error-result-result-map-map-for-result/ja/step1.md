# `Result` の `map`

前の例の `multiply` でパニックを起こすことは、堅牢なコードにはなりません。一般的には、エラーを呼び出し元に返して、エラーに対する適切な対応方法を決定させたいものです。

まず、扱っているエラーの種類を知る必要があります。`Err` 型を特定するには、`i32` 用の `FromStr` トレイトで実装されている `parse()` を見ます。その結果、`Err` 型は `ParseIntError` として指定されます。

以下の例では、単純な `match` 文が全体的に煩雑なコードにつながります。

```rust
use std::num::ParseIntError;

// 戻り値の型を書き換えることで、`unwrap()` を使わないパターンマッチングを使います。
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // これは依然として合理的な答えを提示します。
    let twenty = multiply("10", "2");
    print(twenty);

    // 以下は、はるかに役立つエラーメッセージを提供します。
    let tt = multiply("t", "2");
    print(tt);
}
```

幸いなことに、`Option` の `map`、`and_then`、および他の多くのコンビネータも `Result` で実装されています。`Result` には完全な一覧が含まれています。

```rust
use std::num::ParseIntError;

// `Option` と同じように、`map()` などのコンビネータを使うことができます。
// この関数は、上の関数と同じで、次のように読み取れます。
// 両方の値が `str` からパースできる場合には乗算し、そうでなければエラーをそのまま渡します。
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // これは依然として合理的な答えを提示します。
    let twenty = multiply("10", "2");
    print(twenty);

    // 以下は、はるかに役立つエラーメッセージを提供します。
    let tt = multiply("t", "2");
    print(tt);
}
```
