# Encapsulation des erreurs avec `Box`

Un moyen d'écrire un code simple tout en conservant les erreurs originales est d'encapsuler les erreurs avec `Box`. Le inconvénient est que le type d'erreur sous-jacent n'est connu que pendant l'exécution et n'est pas déterminé statiquement.

La bibliothèque standard aide à encapsuler nos erreurs en faisant en sorte que `Box` implémente la conversion de tout type qui implémente le trait `Error` en l'objet trait `Box<Error>`, via `From`.

```rust
use std::error;
use std::fmt;

// Changez l'alias en `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // Convertit en Box
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // Convertit en Box
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
