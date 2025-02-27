# Présentation de `?`

Parfois, nous voulons simplement la simplicité de `unwrap` sans le risque d'avoir une `panic`. Jusqu'à présent, `unwrap` nous a contraint à imbriquer les appels de plus en plus profondément alors que ce que nous voulions vraiment était d'obtenir la variable _en dehors_. C'est exactement le but de `?`.

Lorsque l'on trouve une `Err`, il y a deux actions valides à prendre :

1.  `panic!` que nous avons déjà décidé d'éviter le plus possible
2.  `return` car une `Err` signifie qu'elle ne peut pas être traitée

`?` est _presque_\[\^†\] exactement équivalent à un `unwrap` qui `return` au lieu de `panic`uer en cas d'`Err`. Voyons comment nous pouvons simplifier l'exemple précédent qui utilisait des combinateurs :

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = first_number_str.parse::<i32>()?;
    let second_number = second_number_str.parse::<i32>()?;

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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

## Le macro `try!`

Avant l'arrivée de `?`, la même fonctionnalité était obtenue avec la macro `try!`. L'opérateur `?` est maintenant recommandé, mais vous pouvez encore trouver `try!` dans du code plus ancien. La même fonction `multiply` de l'exemple précédent ressemblerait à ceci en utilisant `try!` :

```rust
// Pour compiler et exécuter cet exemple sans erreurs, en utilisant Cargo, changez
// la valeur du champ `edition`, dans la section `[package]` du fichier `Cargo.toml`, en "2015".

use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
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
