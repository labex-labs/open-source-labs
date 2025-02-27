# Utiliser Result\<T, E\> dans les tests

Jusqu'à présent, nos tests ont tous provoqué une panique lorsqu'ils ont échoué. Nous pouvons également écrire des tests qui utilisent `Result<T, E>`! Voici le test de la liste 11-1, réécrit pour utiliser `Result<T, E>` et renvoyer une `Err` au lieu de provoquer une panique :

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}
```

La fonction `it_works` a maintenant le type de retour `Result<(), String>`. Dans le corps de la fonction, au lieu d'appeler la macro `assert_eq!`, nous renvoyons `Ok(())` lorsque le test passe et une `Err` avec une `String` à l'intérieur lorsque le test échoue.

Écrire des tests de manière à ce qu'ils renvoient un `Result<T, E>` vous permet d'utiliser l'opérateur question dans le corps des tests, ce qui peut être un moyen pratique d'écrire des tests qui devraient échouer si une opération quelconque à l'intérieur d'eux renvoie une variante `Err`.

Vous ne pouvez pas utiliser l'annotation `#[should_panic]` sur des tests qui utilisent `Result<T, E>`. Pour affirmer qu'une opération renvoie une variante `Err`, _n'utilisez pas_ l'opérateur question sur la valeur `Result<T, E>`. Au lieu de cela, utilisez `assert!(value.is_err())`.

Maintenant que vous connaissez plusieurs façons d'écrire des tests, voyons ce qui se passe lorsque nous exécutons nos tests et explorons les différentes options que nous pouvons utiliser avec `cargo test`.
