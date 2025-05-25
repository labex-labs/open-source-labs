# `?`

`match`를 사용하여 결과를 연결하는 것은 코드를 지저분하게 만들 수 있습니다. 다행히 `?` 연산자를 사용하여 코드를 깔끔하게 만들 수 있습니다. `?` 연산자는 `Result`를 반환하는 표현식의 끝에 사용되며, `match` 표현식과 동일합니다. `Err(err)` 분기는 `return Err(From::from(err))`로 조기 반환되고, `Ok(ok)` 분기는 `ok` 표현식으로 확장됩니다.

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

    // 중간 함수
    fn op_(x: f64, y: f64) -> MathResult {
        // `div` 가 "실패"하면 `DivisionByZero` 가 `return` 됩니다
        let ratio = div(x, y)?;

        // `ln` 이 "실패"하면 `NonPositiveLogarithm` 이 `return` 됩니다
        let ln = ln(ratio)?;

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!("{}", match why {
                MathError::NonPositiveLogarithm
                    => "로그 값이 음수 또는 0 인 수",
                MathError::DivisionByZero
                    => "0 으로 나누기",
                MathError::NegativeSquareRoot
                    => "음수의 제곱근",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}
```

`Result`를 매핑/구성하는 다양한 방법에 대한 자세한 내용은 문서를 참조하십시오.
