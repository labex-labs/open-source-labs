# Dépendances de développement

Parfois, il est nécessaire d'avoir des dépendances uniquement pour les tests (ou les exemples, ou les benchmarks). De telles dépendances sont ajoutées à `Cargo.toml` dans la section `[dev-dependencies]`. Ces dépendances ne sont pas propagées à d'autres packages qui dépendent de ce package.

Un tel exemple est [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html), qui étend les macros standard `assert_eq!` et `assert_ne!` pour fournir une différence colorée.
Fichier `Cargo.toml` :

```toml
# les données standard de la crate sont omises
[dev-dependencies]
pretty_assertions = "1"
```

Fichier `src/lib.rs` :

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // crate pour utilisation exclusivement dans les tests. Ne peut pas être utilisé dans le code non de test.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
