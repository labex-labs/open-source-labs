# `map` pour `Result`

Générer une panique dans la fonction `multiply` de l'exemple précédent ne conduit pas à un code robuste. Généralement, nous souhaitons renvoyer l'erreur à l'appelant afin qu'il puisse décider de la manière appropriée de répondre aux erreurs.

Nous devons tout d'abord savoir quel type d'erreur nous sommes en train de gérer. Pour déterminer le type `Err`, nous regardons `parse()`, qui est implémenté avec le trait `FromStr` pour `i32`. Par conséquent, le type `Err` est spécifié comme étant `ParseIntError`.

Dans l'exemple ci-dessous, l'utilisation directe d'une instruction `match` conduit à un code globalement plus lourd.

```rust
use std::num::ParseIntError;

// En réécrivant le type de retour, nous utilisons la correspondance de motifs sans `unwrap()`.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n est {}", n),
        Err(e) => println!("Erreur : {}", e),
    }
}

fn main() {
    // Cela fournit toujours une réponse raisonnable.
    let twenty = multiply("10", "2");
    print(twenty);

    // Celui-ci fournit maintenant un message d'erreur beaucoup plus utile.
    let tt = multiply("t", "2");
    print(tt);
}
```

Heureusement, les fonctions `map`, `and_then` de `Option` et de nombreux autres combinateurs sont également implémentés pour `Result`. `Result` contient une liste complète.

```rust
use std::num::ParseIntError;

// Comme pour `Option`, nous pouvons utiliser des combinateurs tels que `map()`.
// Cette fonction est sinon identique à la précédente et peut être lue comme suit :
// Multipliez si les deux valeurs peuvent être analysées à partir de str, sinon propagez l'erreur.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n est {}", n),
        Err(e) => println!("Erreur : {}", e),
    }
}

fn main() {
    // Cela fournit toujours une réponse raisonnable.
    let twenty = multiply("10", "2");
    print(twenty);

    // Celui-ci fournit maintenant un message d'erreur beaucoup plus utile.
    let tt = multiply("t", "2");
    print(tt);
}
```
