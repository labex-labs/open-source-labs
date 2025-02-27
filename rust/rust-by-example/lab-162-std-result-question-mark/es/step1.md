# `?`

Encadenar resultados utilizando `match` puede quedar bastante desordenado; por suerte, el operador `?` se puede utilizar para volver las cosas bonitas de nuevo. `?` se utiliza al final de una expresión que devuelve un `Result`, y es equivalente a una expresión `match`, donde la rama `Err(err)` se expande a un `return Err(From::from(err))` temprano, y la rama `Ok(ok)` se expande a una expresión `ok`.

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

    // Función intermedia
    fn op_(x: f64, y: f64) -> MathResult {
        // si `div` "falló", entonces `DivisionByZero` será `return`ado
        let ratio = div(x, y)?;

        // si `ln` "falló", entonces `NonPositiveLogarithm` será `return`ado
        let ln = ln(ratio)?;

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!("{}", match why {
                MathError::NonPositiveLogarithm
                    => "logaritmo de número no positivo",
                MathError::DivisionByZero
                    => "división por cero",
                MathError::NegativeSquareRoot
                    => "raíz cuadrada de número negativo",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}
```

Asegúrese de revisar la documentación, ya que hay muchos métodos para mapear/componer `Result`.
