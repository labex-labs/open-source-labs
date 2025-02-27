# Exécuter un sous-ensemble de tests par nom

Parfois, exécuter un ensemble complet de tests peut prendre beaucoup de temps. Si vous travaillez sur du code dans une zone particulière, vous pouvez vouloir exécuter seulement les tests relatifs à ce code. Vous pouvez choisir les tests à exécuter en passant à `cargo test` le nom ou les noms des tests que vous voulez exécuter en tant qu'argument.

Pour démontrer comment exécuter un sous-ensemble de tests, nous allons tout d'abord créer trois tests pour notre fonction `add_two`, comme indiqué dans la Liste 11-11, et choisir lesquels exécuter.

Nom de fichier : `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Liste 11-11 : Trois tests avec trois noms différents

Si nous exécutons les tests sans passer d'arguments, comme nous l'avons vu précédemment, tous les tests seront exécutés en parallèle :

    running 3 tests
    test tests::add_three_and_two... ok
    test tests::add_two_and_two... ok
    test tests::one_hundred... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
