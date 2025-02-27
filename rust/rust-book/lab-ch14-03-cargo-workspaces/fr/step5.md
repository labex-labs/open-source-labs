# Ajout d'un test à un espace de travail

Pour une autre amélioration, ajoutons un test de la fonction `add_one::add_one` dans le crâne `add_one` :

Nom du fichier : `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Maintenant, exécutez `cargo test` dans le répertoire `add` de niveau supérieur. Exécuter `cargo test` dans un espace de travail structuré comme celui-ci exécutera les tests pour tous les crânes de l'espace de travail :

```bash
$ cargo test
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.27s
     Running unittests src/lib.rs (target/debug/deps/add_one-f0253159197f7841)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

     Running unittests src/main.rs (target/debug/deps/adder-49979ff40686fa8e)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

La première section de la sortie montre que le test `it_works` dans le crâne `add_one` a réussi. La section suivante montre qu'aucun test n'a été trouvé dans le crâne `adder`, et la dernière section montre qu'aucun test de documentation n'a été trouvé dans le crâne `add_one`.

Nous pouvons également exécuter les tests pour un crâne particulier dans un espace de travail à partir du répertoire de niveau supérieur en utilisant le drapeau `-p` et en spécifiant le nom du crâne que nous voulons tester :

```bash
$ cargo test -p add_one
    Finished test [unoptimized + debuginfo] target(s) in 0.00s
     Running unittests src/lib.rs (target/debug/deps/add_one-b3235fea9a156f74)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

Cette sortie montre que `cargo test` n'a exécuté que les tests pour le crâne `add_one` et n'a pas exécuté les tests du crâne `adder`.

Si vous publiez les crânes de l'espace de travail sur *https://crates.io*, chaque crâne de l'espace de travail devra être publié séparément. Comme `cargo test`, nous pouvons publier un crâne particulier de notre espace de travail en utilisant le drapeau `-p` et en spécifiant le nom du crâne que nous voulons publier.

Pour plus de pratique, ajoutez un crâne `add_two` à cet espace de travail de manière similaire au crâne `add_one`!

Au fur et à mesure que votre projet grandit, envisagez d'utiliser un espace de travail : il fournit des composants individuels plus faciles à comprendre et plus petits qu'un gros bloc de code. De plus, garder les crânes dans un espace de travail peut faciliter la coordination entre les crânes si elles sont souvent modifiées en même temps.
