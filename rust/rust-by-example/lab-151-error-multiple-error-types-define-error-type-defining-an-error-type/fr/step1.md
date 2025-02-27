# Définition d'un type d'erreur

Parfois, il est simplifié le code en masquant toutes les différentes erreurs avec un seul type d'erreur. Nous allons le montrer avec une erreur personnalisée.

Rust nous permet de définir nos propres types d'erreur. En général, un "bon" type d'erreur :

- Représente différentes erreurs avec le même type
- Présente de bons messages d'erreur à l'utilisateur
- Est facile à comparer avec d'autres types
  - Bon : `Err(EmptyVec)`
  - Mauvais : `Err("Please use a vector with at least one element".to_owned())`
- Peut conserver des informations sur l'erreur
  - Bon : `Err(BadChar(c, position))`
  - Mauvais : `Err("+ cannot be used here".to_owned())`
- Se compose bien avec d'autres erreurs

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Définissons nos types d'erreur. Ils peuvent être personnalisés pour nos cas de gestion d'erreurs.
// Maintenant, nous serons en mesure d'écrire nos propres erreurs, nous référer à une implémentation d'erreur sous-jacente
// ou faire quelque chose au milieu.
#[derive(Debug, Clone)]
struct DoubleError;

// La génération d'une erreur est complètement séparée de la manière dont elle est affichée.
// Il n'est pas nécessaire de s'inquiéter de brouiller une logique complexe avec le style d'affichage.
//
// Notez que nous ne stockons aucune information supplémentaire sur les erreurs. Cela signifie que nous ne pouvons pas indiquer
// quelle chaîne a échoué à être analysée sans modifier nos types pour transporter cette information.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Changez l'erreur en notre nouveau type.
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // Mettez à jour également le nouveau type d'erreur ici.
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
