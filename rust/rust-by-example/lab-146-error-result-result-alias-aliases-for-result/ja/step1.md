# `Result`のエイリアス

特定の`Result`型を何度も再利用したい場合、どうすればよいでしょうか？Rustはエイリアスを作成できることを思い出してください。便利なことに、問題の特定の`Result`に対してエイリアスを定義することができます。

モジュールレベルでエイリアスを作成すると、特に便利です。特定のモジュールで見つかるエラーは、多くの場合、同じ`Err`型を持っています。したがって、単一のエイリアスですべての関連する`Result`を簡潔に定義することができます。これは非常に便利で、`std`ライブラリでさえそれを提供しています：`io::Result`！

以下は、構文を見せるための簡単な例です：

```rust
use std::num::ParseIntError;

// エラー型が`ParseIntError`の`Result`の汎用エイリアスを定義します。
type AliasedResult<T> = Result<T, ParseIntError>;

// 上記のエイリアスを使用して、特定の`Result`型を参照します。
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// ここでも、エイリアスにより、いくらかのスペースを節約できます。
fn print(result: AliasedResult<i32>) {
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
