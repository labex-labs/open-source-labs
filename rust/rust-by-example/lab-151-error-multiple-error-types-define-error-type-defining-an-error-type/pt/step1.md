# Definindo um tipo de erro

Às vezes, simplifica o código mascarar todos os diferentes erros com um único tipo de erro. Vamos demonstrar isso com um erro personalizado.

Rust nos permite definir nossos próprios tipos de erro. Em geral, um "bom" tipo de erro:

- Representa diferentes erros com o mesmo tipo
- Apresenta boas mensagens de erro ao usuário
- É fácil de comparar com outros tipos
  - Bom: `Err(EmptyVec)`
  - Ruim: `Err("Please use a vector with at least one element".to_owned())`
- Pode conter informações sobre o erro
  - Bom: `Err(BadChar(c, position))`
  - Ruim: `Err("+ cannot be used here".to_owned())`
- Compõe-se bem com outros erros

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Define our error types. These may be customized for our error handling cases.
// Now we will be able to write our own errors, defer to an underlying error
// implementation, or do something in between.
#[derive(Debug, Clone)]
struct DoubleError;

// Generation of an error is completely separate from how it is displayed.
// There's no need to be concerned about cluttering complex logic with the display style.
//
// Note that we don't store any extra info about the errors. This means we can't state
// which string failed to parse without modifying our types to carry that information.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Change the error to our new type.
        .ok_or(DoubleError)
        .and_then(|s| {
            s.parse::<i32>()
                // Update to the new error type here also.
                .map_err(|_| DoubleError)
                .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
