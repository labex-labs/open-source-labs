# Retours anticipés

Dans l'exemple précédent, nous avons géré explicitement les erreurs en utilisant des combinateurs. Une autre manière de traiter cette analyse de cas est d'utiliser une combinaison d'instructions `match` et de _retours anticipés_.

C'est-à-dire que nous pouvons simplement arrêter l'exécution de la fonction et renvoyer l'erreur si elle se produit. Pour certains, cette forme de code peut être plus facile à lire et à écrire. Considérez cette version de l'exemple précédent, réécrite en utilisant des retours anticipés :

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

À ce stade, nous avons appris à gérer explicitement les erreurs en utilisant des combinateurs et des retours anticipés. Bien que nous soyons généralement tentés d'éviter les panics, gérer explicitement toutes nos erreurs est fastidieux.

Dans la section suivante, nous présenterons l'opérateur `?` pour les cas où nous avons simplement besoin d'`unwrap` sans risquer de déclencher de panique.
