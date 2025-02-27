# `?`

Цепочка результатов с использованием `match` может стать довольно запутанной; к счастью, оператор `?` можно использовать, чтобы снова сделать все красиво. `?` используется в конце выражения, возвращающего `Result`, и эквивалентен выражению `match`, где ветвь `Err(err)` расширяется до раннего `return Err(From::from(err))`, а ветвь `Ok(ok)` расширяется до выражения `ok`.

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

    // Промежуточная функция
    fn op_(x: f64, y: f64) -> MathResult {
        // Если `div` "неудается", то `DivisionByZero` будет `return`ed
        let ratio = div(x, y)?;

        // Если `ln` "неудается", то `NonPositiveLogarithm` будет `return`ed
        let ln = ln(ratio)?;

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!("{}", match why {
                MathError::NonPositiveLogarithm
                    => "логарифм неположительного числа",
                MathError::DivisionByZero
                    => "деление на ноль",
                MathError::NegativeSquareRoot
                    => "квадратный корень из отрицательного числа",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}
```

Обязательно проверьте документацию, так как есть много методов для сопоставления/композиции `Result`.
