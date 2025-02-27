# 早期リターン

前の例では、コンビネータを使ってエラーを明示的に処理しました。このようなケース分析を行う別の方法は、`match` 文と _早期リターン_ を組み合わせることです。

つまり、エラーが発生した場合には、単に関数の実行を停止してエラーを返すことができます。この形式のコードは、読みやすさと書きやすさの両方において、一部の人にとってはより簡単です。前の例のこのバージョンを早期リターンを使って書き直したものを見てみましょう：

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

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

この時点で、コンビネータと早期リターンを使ってエラーを明示的に処理する方法を学びました。一般的にはパニックを避けたいのですが、すべてのエラーを明示的に処理するのは面倒です。

次のセクションでは、単に `unwrap` するだけで `panic` を引き起こす可能性のない場合に `?` 演算子を紹介します。
