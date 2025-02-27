# Tests

Comme nous le savons, les tests sont essentiels pour tout logiciel! Rust offre un support de première classe pour les tests unitaires et d'intégration ([voir ce chapitre](https://doc.rust-lang.org/book/ch11-00-testing.html) dans le TRPL).

Dans les chapitres sur les tests liés ci-dessus, nous voyons comment écrire des tests unitaires et des tests d'intégration. Sur le plan organisationnel, nous pouvons placer les tests unitaires dans les modules qu'ils testent et les tests d'intégration dans leur propre répertoire `tests/` :

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

Chaque fichier dans `tests` est un [test d'intégration](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests) distinct, c'est-à-dire un test destiné à tester votre bibliothèque comme si elle était appelée à partir d'une crate dépendante.

Le chapitre sur les tests détaile les trois styles de tests différents : Unitaires, Doc et d'Intégration.

`cargo` fournit naturellement un moyen simple d'exécuter tous vos tests!

```shell
$ cargo test
```

Vous devriez voir une sortie comme celle-ci :

```shell
$ cargo test
   Compiling blah v0.1.0 (file:///nobackup/blah)
    Finished dev [unoptimized + debuginfo] target(s) in 0.89 secs
     Running target/debug/deps/blah-d3b32b97275ec472

running 3 tests
test test_bar... ok
test test_baz... ok
test test_foo_bar... ok
test test_foo... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

Vous pouvez également exécuter les tests dont le nom correspond à un motif :

```shell
$ cargo test test_foo
```

```shell
$ cargo test test_foo
   Compiling blah v0.1.0 (file:///nobackup/blah)
    Finished dev [unoptimized + debuginfo] target(s) in 0.35 secs
     Running target/debug/deps/blah-d3b32b97275ec472

running 2 tests
test test_foo... ok
test test_foo_bar... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out
```

Un mot d'avertissement : Cargo peut exécuter plusieurs tests en parallèle, assurez-vous donc qu'ils ne se chevauchent pas.

Un exemple de problèmes causés par cette concurrence est si deux tests écrivent dans un fichier, comme ci-dessous :

```rust
#[cfg(test)]
mod tests {
    // Importe les modules nécessaires
    use std::fs::OpenOptions;
    use std::io::Write;

    // Ce test écrit dans un fichier
    #[test]
    fn test_file() {
        // Ouvre le fichier ferris.txt ou le crée s'il n'existe pas.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Impossible d'ouvrir ferris.txt");

        // Affiche "Ferris" 5 fois.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Impossible d'écrire dans ferris.txt");
        }
    }

    // Ce test essaie d'écrire dans le même fichier
    #[test]
    fn test_file_also() {
        // Ouvre le fichier ferris.txt ou le crée s'il n'existe pas.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Impossible d'ouvrir ferris.txt");

        // Affiche "Corro" 5 fois.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Impossible d'écrire dans ferris.txt");
        }
    }
}
```

Bien que l'intention soit d'obtenir ceci :

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

Voici ce qui est effectivement écrit dans `ferris.txt` :

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
