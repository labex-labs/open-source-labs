# `Result`

我们已经了解到，`Option` 枚举可以用作可能失败的函数的返回值，其中可以返回 `None` 来表示失败。然而，有时表达操作失败的 _原因_ 很重要。为此，我们有了 `Result` 枚举。

`Result<T, E>` 枚举有两个变体：

- `Ok(value)`，表示操作成功，并包装操作返回的 `value`。（`value` 的类型为 `T`）
- `Err(why)`，表示操作失败，并包装 `why`，它（希望）能解释失败的原因。（`why` 的类型为 `E`）

```rust
mod checked {
    // 我们想要捕获的数学“错误”
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // 此操作会“失败”，相反，让我们返回包装在 `Err` 中的失败原因
            Err(MathError::DivisionByZero)
        } else {
            // 此操作有效，返回包装在 `Ok` 中的结果
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
    // 这是一个三层匹配金字塔！
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
    // 这会失败吗？
    println!("{}", op(1.0, 10.0));
}
```
