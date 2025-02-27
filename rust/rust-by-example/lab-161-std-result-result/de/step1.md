# `Result`

Wir haben gesehen, dass die `Option`-Enumeration als Rückgabewert von Funktionen verwendet werden kann, die fehlschlagen können, wobei `None` zurückgegeben werden kann, um ein Fehlerzustand anzuzeigen. Manchmal ist es jedoch wichtig, _warum_ eine Operation fehlschlägt zu erklären. Dazu haben wir die `Result`-Enumeration.

Die `Result<T, E>`-Enumeration hat zwei Varianten:

- `Ok(value)`, was angibt, dass die Operation erfolgreich war, und umschließt den von der Operation zurückgegebenen `value`. (`value` hat den Typ `T`)
- `Err(why)`, was angibt, dass die Operation fehlgeschlagen ist, und umschließt `why`, das (hoffentlich) die Ursache des Fehlers erklärt. (`why` hat den Typ `E`)

```rust
mod checked {
    // Mathematische "Fehler", die wir fangen möchten
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Diese Operation würde `fehlschlagen`, stattdessen geben wir den Grund
            // des Fehlers in `Err` zurück
            Err(MathError::DivisionByZero)
        } else {
            // Diese Operation ist gültig, geben wir das Ergebnis in `Ok` zurück
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
    // Dies ist eine dreistufige Match-Pyramide!
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
    // Wird dies fehlschlagen?
    println!("{}", op(1.0, 10.0));
}
```
