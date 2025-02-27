# Ignorer certains tests sauf si spécifiquement demandé

Parfois, quelques tests spécifiques peuvent être très longs à exécuter, donc vous pouvez vouloir les exclure pendant la plupart des exécutions de `cargo test`. Au lieu de lister en tant qu'arguments tous les tests que vous voulez exécuter, vous pouvez au contraire annoter les tests longs à exécuter en utilisant l'attribut `ignore` pour les exclure, comme le montre ici :

Nom de fichier : `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // code qui prend une heure à s'exécuter
}
```

Après `#[test]`, nous ajoutons la ligne `#[ignore]` au test que nous voulons exclure. Maintenant, lorsque nous exécutons nos tests, `it_works` s'exécute, mais `expensive_test` ne s'exécute pas :

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.60s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test expensive_test... ignoré
test it_works... ok

test result: ok. 1 passé ; 0 échoué ; 1 ignoré ; 0 mesuré ; 0
filtré ; terminé en 0.00s
```

La fonction `expensive_test` est listée comme `ignorée`. Si nous voulons exécuter seulement les tests ignorés, nous pouvons utiliser `cargo test -- --ignored` :

```bash
$ cargo test -- --ignored
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test expensive_test... ok

test result: ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 1
filtré ; terminé en 0.00s
```

En contrôlant quels tests s'exécutent, vous pouvez vous assurer que les résultats de `cargo test` seront renvoyés rapidement. Lorsque vous êtes à un stade où il est pertinent de vérifier les résultats des tests `ignorés` et que vous avez le temps d'attendre les résultats, vous pouvez exécuter `cargo test -- --ignored` à la place. Si vous voulez exécuter tous les tests, qu'ils soient ignorés ou non, vous pouvez exécuter `cargo test -- --include-ignored`.
