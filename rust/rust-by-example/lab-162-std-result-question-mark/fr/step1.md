# `?`

La chaîne de résultats en utilisant `match` peut devenir assez difficile à lire ; heureusement, l'opérateur `?` peut être utilisé pour remettre les choses dans l'ordre. `?` est utilisé à la fin d'une expression renvoyant un `Result`, et est équivalent à une expression `match`, où la branche `Err(err)` se développe en un `return Err(From::from(err))` précoce, et la branche `Ok(ok)` se développe en une expression `ok`.

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

    // Fonction intermédiaire
    fn op_(x: f64, y: f64) -> MathResult {
        // si `div` "échoue", alors `DivisionByZero` sera `return`é
        let ratio = div(x, y)?;

        // si `ln` "échoue", alors `NonPositiveLogarithm` sera `return`é
        let ln = ln(ratio)?;

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!("{}", match why {
                MathError::NonPositiveLogarithm
                    => "logarithme d'un nombre non positif",
                MathError::DivisionByZero
                    => "division par zéro",
                MathError::NegativeSquareRoot
                    => "racine carrée d'un nombre négatif",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}
```

N'oubliez pas de consulter la documentation, car il existe de nombreuses méthodes pour mapper/composer `Result`.
