# Encapsulation des erreurs

Une alternative au conditionnement des erreurs consiste à les encapsuler dans votre propre type d'erreur.

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // Nous différons l'implémentation de l'erreur d'analyse pour leur erreur.
    // Fournir des informations supplémentaires nécessite d'ajouter plus de données au type.
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "veuillez utiliser un vecteur avec au moins un élément"),
            // L'erreur encapsulée contient des informations supplémentaires et est disponible
            // via la méthode source().
            DoubleError::Parse(..) =>
                write!(f, "la chaîne de caractères fournie ne peut pas être analysée comme un entier"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // La cause est le type d'erreur d'implémentation sous-jacent. Est implicitement
            // cast en objet de trait `&error::Error`. Cela fonctionne car le
            // type sous-jacent implémente déjà le trait `Error`.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// Implémentez la conversion de `ParseIntError` en `DoubleError`.
// Cela sera automatiquement appelé par `?` si un `ParseIntError`
// doit être converti en un `DoubleError`.
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // Ici, nous utilisons implicitement l'implémentation de `From` de `ParseIntError` (que
    // nous avons définie ci-dessus) pour créer un `DoubleError`.
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("Le premier doublé est {}", n),
        Err(e) => {
            println!("Erreur : {}", e);
            if let Some(source) = e.source() {
                println!("  Causée par : {}", source);
            }
        },
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

Cela ajoute un peu plus de code de base pour gérer les erreurs et peut ne pas être nécessaire dans toutes les applications. Il existe certaines bibliothèques qui peuvent prendre en charge le code de base pour vous.
