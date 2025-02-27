# `Result`

Мы видели, что перечисление `Option` может использоваться в качестве возвращаемого значения функций, которые могут завершиться неудачей, где `None` может быть возвращено для индикации неудачи. Однако, иногда важно выразить _причину_, по которой операция завершилась неудачей. Для этого существует перечисление `Result`.

Перечисление `Result<T, E>` имеет два варианта:

- `Ok(value)`, которое означает, что операция завершилась успешно, и оборачивает `value`, возвращаемое операцией. (`value` имеет тип `T`)
- `Err(why)`, которое означает, что операция завершилась неудачей, и оборачивает `why`, которое (надеюсь) объясняет причину неудачи. (`why` имеет тип `E`)

```rust
mod checked {
    // Математические "ошибки", которые мы хотим ловить
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Эта операция завершилась бы с `ошибкой`, вместо этого давайте вернем причину
            // неудачи, обернутую в `Err`
            Err(MathError::DivisionByZero)
        } else {
            // Эта операция корректна, возвращаем результат, обернутый в `Ok`
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
    // Это трехуровневый пирамидальный match!
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
    // Это завершится с ошибкой?
    println!("{}", op(1.0, 10.0));
}
```
