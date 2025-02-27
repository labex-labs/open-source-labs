# Itération sur des `Result`

Une opération `Iter::map` peut échouer, par exemple :

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Résultats : {:?}", numbers);
}
```

Examillons les stratégies pour gérer ceci.

## Ignorer les éléments ayant échoué avec `filter_map()`

`filter_map` appelle une fonction et filtre les résultats qui sont `None`.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Résultats : {:?}", numbers);
}
```

## Collecter les éléments ayant échoué avec `map_err()` et `filter_map()`

`map_err` appelle une fonction avec l'erreur, donc en l'ajoutant à la solution `filter_map` précédente, nous pouvons les sauvegarder de côté pendant l'itération.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Nombres : {:?}", numbers);
    println!("Erreurs : {:?}", errors);
}
```

## Faire échouer l'opération entière avec `collect()`

`Result` implémente `FromIterator` de sorte qu'un vecteur de résultats (`Vec<Result<T, E>>`) peut être converti en un résultat avec un vecteur (`Result<Vec<T>, E>`). Une fois qu'un `Result::Err` est trouvé, l'itération se terminera.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Résultats : {:?}", numbers);
}
```

La même technique peut être utilisée avec `Option`.

## Collecter toutes les valeurs valides et les échecs avec `partition()`

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Nombres : {:?}", numbers);
    println!("Erreurs : {:?}", errors);
}
```

Lorsque vous examinez les résultats, vous remarquerez que tout est toujours encapsulé dans `Result`. Un peu plus de boilerplate est nécessaire pour cela.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Nombres : {:?}", numbers);
    println!("Erreurs : {:?}", errors);
}
```
