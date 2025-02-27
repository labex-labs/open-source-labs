# `Result`

Hemos visto que el enum `Option` se puede usar como valor de retorno de funciones que pueden fallar, donde se puede devolver `None` para indicar el fracaso. Sin embargo, a veces es importante expresar _por qué_ una operación falló. Para hacer esto tenemos el enum `Result`.

El enum `Result<T, E>` tiene dos variantes:

- `Ok(value)` que indica que la operación tuvo éxito y envuelve el `value` devuelto por la operación. (`value` tiene tipo `T`)
- `Err(why)`, que indica que la operación falló y envuelve `why`, que (esperemos) explica la causa del fracaso. (`why` tiene tipo `E`)

```rust
mod checked {
    // "Errores" matemáticos que queremos capturar
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Esta operación `fallaría`, en lugar de eso, devolvemos la razón del
            // fracaso envuelta en `Err`
            Err(MathError::DivisionByZero)
        } else {
            // Esta operación es válida, devolvemos el resultado envuelto en `Ok`
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
    // ¡Este es un triángulo de coincidencias de tres niveles!
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
    // ¿Esto fallará?
    println!("{}", op(1.0, 10.0));
}
```
