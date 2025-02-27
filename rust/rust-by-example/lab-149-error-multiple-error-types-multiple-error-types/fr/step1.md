# Plusieurs types d'erreurs

Les exemples précédents ont toujours été très pratiques ; les `Result` interagissent avec d'autres `Result` et les `Option` interagissent avec d'autres `Option`.

Parfois, une `Option` doit interagir avec une `Result`, ou une `Result<T, Error1>` doit interagir avec une `Result<T, Error2>`. Dans ces cas, nous voulons gérer nos différents types d'erreurs de manière à les rendre composables et faciles à interagir.

Dans le code suivant, deux instances de `unwrap` génèrent différents types d'erreurs. `Vec::first` renvoie une `Option`, tandis que `parse::<i32>` renvoie une `Result<i32, ParseIntError>` :

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Génère l'erreur 1
    2 * first.parse::<i32>().unwrap() // Génère l'erreur 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("Le premier doublé est {}", double_first(numbers));

    println!("Le premier doublé est {}", double_first(empty));
    // Erreur 1 : le vecteur d'entrée est vide

    println!("Le premier doublé est {}", double_first(strings));
    // Erreur 2 : l'élément ne peut pas être analysé en tant que nombre
}
```

Dans les sections suivantes, nous verrons plusieurs stratégies pour résoudre ce genre de problèmes.
