# `Result`

Nous avons vu que l'énumération `Option` peut être utilisée comme valeur de retour de fonctions qui peuvent échouer, où `None` peut être renvoyé pour indiquer l'échec. Cependant, parfois il est important d'exprimer _pourquoi_ une opération a échoué. Pour ce faire, nous avons l'énumération `Result`.

L'énumération `Result<T, E>` a deux variantes :

- `Ok(value)` qui indique que l'opération a réussi et encapsule la `value` renvoyée par l'opération. (`value` a le type `T`)
- `Err(why)`, qui indique que l'opération a échoué et encapsule `why`, qui (espérons-le) explique la cause de l'échec. (`why` a le type `E`)

```rust
mod checked {
    // Les "erreurs" mathématiques que nous voulons attraper
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Cette opération aurait `échoué`, au lieu de cela, renvoyons la raison
            // de l'échec encapsulée dans `Err`
            Err(MathError::DivisionByZero)
        } else {
            // Cette opération est valide, renvoyons le résultat encapsulé dans `Ok`
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
    // C'est une pyramide de correspondances de trois niveaux!
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
    // Cela va-t-il échouer?
    println!("{}", op(1.0, 10.0));
}
```
