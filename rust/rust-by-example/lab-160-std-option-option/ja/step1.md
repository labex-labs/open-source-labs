# `Option`

プログラムの一部のエラーをキャッチして、`panic!` を呼び出さないことが望ましい場合があります。これは、`Option` 列挙型を使用して達成できます。

`Option<T>` 列挙型には 2 つのバリアントがあります。

- `None` は、エラーまたは値の欠如を示します。
- `Some(value)` は、型 `T` の `value` をラップするタプル構造体です。

```rust
// `panic!` しない整数の除算
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // エラーは `None` バリアントで表されます
        None
    } else {
        // 結果は `Some` バリアントにラップされます
        Some(dividend / divisor)
    }
}

// 成功しない可能性のある除算を処理するこの関数
fn try_division(dividend: i32, divisor: i32) {
    // `Option` 値は、他の列挙型と同じようにパターンマッチできます
    match checked_division(dividend, divisor) {
        None => println!("{} / {} failed!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // `None` を変数にバインドするには、型注釈が必要です
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // `Some` バリアントをアンラップすると、ラップされた値が抽出されます。
    println!("{:?} unwraps to {:?}", optional_float, optional_float.unwrap());

    // `None` バリアントをアンラップすると `panic!` します
    println!("{:?} unwraps to {:?}", none, none.unwrap());
}
```
