# `?` の紹介

時には、`unwrap` のシンプルさが欲しいだけで、`panic` する可能性がない場合があります。今まで、`unwrap` は、本当に欲しかったのが変数を取り出すことだったにもかかわらず、深くネストすることを余儀なくされてきました。これこそが `?` の目的です。

`Err` を見つけたとき、取るべき有効なアクションは2つあります。

1. `panic!` で、できる限り避けようとしてきたもの
2. `return` で、`Err` は処理できないことを意味するため

`?` は、`Err` のときに `panic` する代わりに `return` する `unwrap` とほぼ同じです。前のコンビネータを使った例をどのように簡略化できるか見てみましょう。

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

## `try!` マクロ

`?` がある前は、同じ機能を `try!` マクロで実現していました。`?` 演算子が現在推奨されていますが、古いコードを見るときにはまだ `try!` を見つけることがあります。前の例の同じ `multiply` 関数は、`try!` を使ってこのようになります。

```rust
// To compile and run this example without errors, while using Cargo, change the value
// of the `edition` field, in the `[package]` section of the `Cargo.toml` file, to "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
