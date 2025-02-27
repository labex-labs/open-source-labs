# Tests d'intégration

Les tests unitaires testent un module isolément, un à la fois. Ils sont petits et peuvent tester le code privé. Les tests d'intégration sont externes à votre boîte à outils et utilisent seulement son interface publique, de la même manière que n'importe quel autre code. Leur but est de tester que de nombreuses parties de votre bibliothèque fonctionnent correctement ensemble.

Cargo cherche les tests d'intégration dans le répertoire `tests` à côté de `src`.

Fichier `src/lib.rs` :

```rust
// Définissez ceci dans une boîte à outils appelée `adder`.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Fichier avec le test : `tests/integration_test.rs` :

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

Exécution des tests avec la commande `cargo test` :

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Chaque fichier source Rust dans le répertoire `tests` est compilé comme une boîte à outils séparée. Pour partager du code entre les tests d'intégration, on peut créer un module avec des fonctions publiques, l'importer et l'utiliser dans les tests.

Fichier `tests/common/mod.rs` :

```rust
pub fn setup() {
    // du code de configuration, comme la création de fichiers/dossiers requis,
    // le lancement de serveurs, etc.
}
```

Fichier avec le test : `tests/integration_test.rs`

```rust
// importation du module commun.
mod common;

#[test]
fn test_add() {
    // utilisation du code commun.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

Créer le module sous la forme de `tests/common.rs` fonctionne également, mais n'est pas recommandé car le lanceur de tests traitera le fichier comme une boîte à outils de test et tentera d'exécuter les tests à l'intérieur.
