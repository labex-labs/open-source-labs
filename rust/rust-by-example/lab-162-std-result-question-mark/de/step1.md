# `?`

Das Verkettieren von Ergebnissen mit `match` kann ziemlich unübersichtlich werden; zum Glück kann der `?`-Operator verwendet werden, um die Dinge wieder in Ordnung zu bringen. `?` wird am Ende eines Ausdrucks verwendet, der ein `Result` zurückgibt, und ist äquivalent zu einem `match`-Ausdruck, wobei der `Err(err)`-Zweig zu einem frühen `return Err(From::from(err))` erweitert wird und der `Ok(ok)`-Zweig zu einem `ok`-Ausdruck erweitert wird.

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

    // Zwischenfunktion
    fn op_(x: f64, y: f64) -> MathResult {
        // Wenn `div` "fehlschlägt", dann wird `DivisionByZero` `return`ed
        let ratio = div(x, y)?;

        // Wenn `ln` "fehlschlägt", dann wird `NonPositiveLogarithm` `return`ed
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

Achten Sie darauf, die Dokumentation zu überprüfen, da es viele Methoden gibt, um `Result` zu map/en zu komponieren.
