# Le module tests et #\[cfg(test)\]

L'annotation `#[cfg(test)]` sur le module `tests` indique à Rust de compiler et d'exécuter le code de test seulement lorsque vous exécutez `cargo test`, et non lorsque vous exécutez `cargo build`. Cela économise le temps de compilation lorsque vous ne voulez que construire la bibliothèque et économise de l'espace dans l'artefact compilé résultant car les tests ne sont pas inclus. Vous verrez que puisque les tests d'intégration sont dans un répertoire différent, ils n'ont pas besoin de l'annotation `#[cfg(test)]`. Cependant, puisque les tests unitaires sont dans les mêmes fichiers que le code, vous utiliserez `#[cfg(test)]` pour spécifier qu'ils ne devraient pas être inclus dans le résultat compilé.

Rappelez-vous que lorsque nous avons généré le nouveau projet `adder` dans la première section de ce chapitre, Cargo a généré ce code pour nous :

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Ce code est le module `tests` généré automatiquement. L'attribut `cfg` signifie _configuration_ et indique à Rust que l'élément suivant ne devrait être inclus que si une certaine option de configuration est donnée. Dans ce cas, l'option de configuration est `test`, qui est fournie par Rust pour compiler et exécuter les tests. En utilisant l'attribut `cfg`, Cargo compile notre code de test seulement si nous exécutons activement les tests avec `cargo test`. Cela inclut toutes les fonctions d'aide qui pourraient être dans ce module, en plus des fonctions annotées avec `#[test]`.
