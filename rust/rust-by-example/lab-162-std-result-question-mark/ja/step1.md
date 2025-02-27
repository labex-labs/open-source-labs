# `?`

`match` を使って結果をチェーン化するとかなり汚くなります。幸いにも、`?` 演算子を使うことでもう一度きれいにすることができます。`?` は `Result` を返す式の末尾で使用され、`match` 式に相当します。ここで、`Err(err)` ブランチは早期の `return Err(From::from(err))` に展開され、`Ok(ok)` ブランチは `ok` 式に展開されます。

```rust
mod checked {
    #[derive(Debug)]
    enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    type MathResult = Result<f64, MathError>;

    fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            Err(MathError::DivisionByZero)
        } else {
            Ok(x / y)
        }
    }

    fn sqrt(x: f64) -> MathResult {
        if x < 0.0 {
            Err(MathError::NegativeSquareRoot)
        } else {
            Ok(x.sqrt())
        }
    }

    fn ln(x: f64) -> MathResult {
        if x <= 0.0 {
            Err(MathError::NonPositiveLogarithm)
        } else {
            Ok(x.ln())
        }
    }

    // 中間関数
    fn op_(x: f64, y: f64) -> MathResult {
        // `div` が「失敗」した場合、`DivisionByZero` が `return` されます
        let ratio = div(x, y)?;

        // `ln` が「失敗」した場合、`NonPositiveLogarithm` が `return` されます
        let ln = ln(ratio)?;

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!("{}", match why {
                MathError::NonPositiveLogarithm
                    => "logarithm of non-positive number",
                MathError::DivisionByZero
                    => "division by zero",
                MathError::NegativeSquareRoot
                    => "square root of negative number",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}
```

`Result` をマッピング/合成する方法はたくさんあるので、ドキュメントを確認することを忘れないでください。
