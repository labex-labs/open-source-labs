# `Result`

失敗する可能性のある関数の返り値として`Option`列挙型を使用できることを見てきました。そこでは、失敗を示すために`None`を返すことができます。しかし、時には操作が失敗した「理由」を表現することが重要です。このために、`Result`列挙型が用意されています。

`Result<T, E>`列挙型には 2 つのバリアントがあります。

- `Ok(value)`は操作が成功したことを示し、操作で返された`value`をラップします。(`value`は型`T`を持ちます)
- `Err(why)`は操作が失敗したことを示し、失敗の原因を (おそらく) 説明する`why`をラップします。(`why`は型`E`を持ちます)

```rust
mod checked {
    // キャッチしたい数学的な「エラー」
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // この操作は「失敗」します。代わりに、`Err` にラップされた失敗の理由を返しましょう
            Err(MathError::DivisionByZero)
        } else {
            // この操作は有効です。`Ok` にラップされた結果を返します
            Ok(x / y)
        }
    }

    pub fn sqrt(x: f64) -> MathResult {
        if x < 0.0 {
            Err(MathError::NegativeSquareRoot)
        } else {
            Ok(x.sqrt())
        }
    }

    pub fn ln(x: f64) -> MathResult {
        if x <= 0.0 {
            Err(MathError::NonPositiveLogarithm)
        } else {
            Ok(x.ln())
        }
    }
}

// `op(x, y)` === `sqrt(ln(x / y))`
fn op(x: f64, y: f64) -> f64 {
    // これは 3 段階のマッチピラミッドです！
    match checked::div(x, y) {
        Err(why) => panic!("{:?}", why),
        Ok(ratio) => match checked::ln(ratio) {
            Err(why) => panic!("{:?}", why),
            Ok(ln) => match checked::sqrt(ln) {
                Err(why) => panic!("{:?}", why),
                Ok(sqrt) => sqrt,
            },
        },
    }
}

fn main() {
    // これは失敗しますか？
    println!("{}", op(1.0, 10.0));
}
```
