# Alias pour `Result`

Et si on voulait réutiliser un type `Result` spécifique plusieurs fois? Rappelez-vous que Rust nous permet de créer des alias. Commode, n'est-ce pas? Nous pouvons définir un alias pour le `Result` spécifique en question.

Au niveau d'un module, la création d'alias peut être particulièrement utile. Les erreurs trouvées dans un module spécifique ont souvent le même type `Err`, donc un seul alias peut définir de manière concise _tous_ les `Result` associés. C'est si pratique que la bibliothèque `std` en fournit même un : `io::Result`!

Voici un exemple rapide pour montrer la syntaxe :

```rust
use std::num::ParseIntError;

// Définissez un alias générique pour un `Result` avec le type d'erreur `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Utilisez l'alias ci-dessus pour vous référer à notre type `Result` spécifique.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Ici, l'alias nous permet encore une fois de gagner de l'espace.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n est {}", n),
        Err(e) => println!("Erreur : {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
