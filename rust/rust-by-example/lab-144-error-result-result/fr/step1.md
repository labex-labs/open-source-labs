# `Result`

`Result` est une version plus riche du type `Option` qui décrit des _erreurs_ possibles au lieu d'une _absence_ possible.

C'est-à-dire que `Result<T, E>` peut avoir l'une des deux issues suivantes :

- `Ok(T)` : Un élément `T` a été trouvé
- `Err(E)` : Une erreur a été trouvée avec l'élément `E`

Par convention, le résultat attendu est `Ok` tandis que le résultat inattendu est `Err`.

Comme `Option`, `Result` a de nombreuses méthodes associées. `unwrap()`, par exemple, renvoie soit l'élément `T`, soit provoque une panique (`panic`). Pour la gestion des cas, il existe de nombreux combinateurs entre `Result` et `Option` qui se chevauchent.

En travaillant avec Rust, vous rencontrerez probablement des méthodes qui renvoient le type `Result`, comme la méthode `parse()`. Il n'est pas toujours possible d'analyser une chaîne de caractères en un autre type, donc `parse()` renvoie un `Result` indiquant une éventuelle erreur.

Voyons ce qui se passe lorsque nous analysons avec succès et sans succès une chaîne de caractères avec `parse()` :

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Essayons d'utiliser `unwrap()` pour extraire le nombre. Cela va-t-il nous causer des problèmes?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

Dans le cas d'échec, `parse()` nous laisse avec une erreur sur laquelle `unwrap()` va provoquer une panique (`panic`). De plus, la panique (`panic`) quitte notre programme et fournit un message d'erreur désagréable.

Pour améliorer la qualité de notre message d'erreur, nous devrions être plus précis sur le type de retour et considérer gérer explicitement l'erreur.

## Utilisation de `Result` dans `main`

Le type `Result` peut également être le type de retour de la fonction `main` si cela est spécifié explicitement. Normalement, la fonction `main` sera de la forme :

```rust
fn main() {
    println!("Hello World!");
}
```

Cependant, `main` est également capable d'avoir un type de retour de `Result`. Si une erreur se produit dans la fonction `main`, elle renverra un code d'erreur et affichera une représentation de débogage de l'erreur (en utilisant le trait \[`Debug`\]). L'exemple suivant montre un tel scénario et aborde des aspects couverts dans \[la section suivante\].

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
