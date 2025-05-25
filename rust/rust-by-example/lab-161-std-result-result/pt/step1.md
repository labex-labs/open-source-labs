# `Result`

Vimos que o tipo enumerado `Option` pode ser usado como valor de retorno de funções que podem falhar, onde `None` pode ser retornado para indicar falha. No entanto, às vezes é importante expressar _por que_ uma operação falhou. Para isso, temos o tipo enumerado `Result`.

O tipo enumerado `Result<T, E>` possui duas variantes:

- `Ok(valor)`, que indica que a operação teve sucesso e encapsula o `valor` retornado pela operação. (`valor` tem tipo `T`)
- `Err(motivo)`, que indica que a operação falhou e encapsula `motivo`, que (esperançosamente) explica a causa da falha. (`motivo` tem tipo `E`)

```rust
mod checked {
    // "Erros" matemáticos que queremos capturar
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Esta operação falharia; em vez disso, vamos retornar o motivo da
            // falha encapsulado em `Err`
            Err(MathError::DivisionByZero)
        } else {
            // Esta operação é válida; vamos retornar o resultado encapsulado em `Ok`
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
    // Esta é uma pirâmide de correspondência de três níveis!
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
    // Esta operação falhará?
    println!("{}", op(1.0, 10.0));
}
```
