# Extraire les `Result` des `Option`

La manière la plus simple de gérer différents types d'erreurs est de les emboîter les uns dans les autres.

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    })
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("Le premier doublé est {:?}", double_first(numbers));

    println!("Le premier doublé est {:?}", double_first(empty));
    // Erreur 1 : le vecteur d'entrée est vide

    println!("Le premier doublé est {:?}", double_first(strings));
    // Erreur 2 : l'élément ne peut pas être converti en nombre
}
```

Il y a des cas où nous voudrons arrêter le traitement en cas d'erreur (comme avec `?`) mais continuer quand l'`Option` est `None`. Deux combinateurs sont utiles pour inverser `Result` et `Option`.

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    });

    opt.map_or(Ok(None), |r| r.map(Some))
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("Le premier doublé est {:?}", double_first(numbers));
    println!("Le premier doublé est {:?}", double_first(empty));
    println!("Le premier doublé est {:?}", double_first(strings));
}
```
