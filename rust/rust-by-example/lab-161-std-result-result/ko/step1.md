# `Result`

`Option` 열거형이 실패할 수 있는 함수에서 반환 값으로 사용될 수 있으며, `None`을 반환하여 실패를 나타낼 수 있다는 것을 살펴보았습니다. 하지만, 때로는 연산이 _왜_ 실패했는지 표현하는 것이 중요합니다. 이를 위해 `Result` 열거형을 사용합니다.

`Result<T, E>` 열거형은 두 가지 변형을 가집니다:

- `Ok(value)`는 연산이 성공했음을 나타내며, 연산에서 반환된 `value`를 감쌉니다. (`value`의 타입은 `T`)
- `Err(why)`는 연산이 실패했음을 나타내며, 실패의 원인을 (희망적으로) 설명하는 `why`를 감쌉니다. (`why`의 타입은 `E`)

```rust
mod checked {
    // Mathematical "errors" we want to catch
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // This operation would `fail`, instead let's return the reason of
            // the failure wrapped in `Err`
            Err(MathError::DivisionByZero)
        } else {
            // This operation is valid, return the result wrapped in `Ok`
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
    // This is a three level match pyramid!
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
    // Will this fail?
    println!("{}", op(1.0, 10.0));
}
```
