# Les sous-modules dans les tests d'intégration

Au fur et à mesure que vous ajoutez plus de tests d'intégration, vous pouvez vouloir créer plus de fichiers dans le répertoire `tests` pour mieux les organiser ; par exemple, vous pouvez regrouper les fonctions de test en fonction de la fonctionnalité qu'elles testent. Comme mentionné précédemment, chaque fichier dans le répertoire `tests` est compilé comme une crate séparée, ce qui est utile pour créer des portées séparées pour imiter plus étroitement la manière dont les utilisateurs finaux utiliseront votre crate. Cependant, cela signifie que les fichiers dans le répertoire `tests` n'ont pas le même comportement que les fichiers dans `src`, comme vous l'avez appris au chapitre 7 sur la manière de séparer le code en modules et en fichiers.

Le comportement différent des fichiers du répertoire `tests` est le plus évident lorsque vous avez un ensemble de fonctions d'aide à utiliser dans plusieurs fichiers de test d'intégration et que vous essayez de suivre les étapes de "Séparation des modules dans différents fichiers" pour les extraire dans un module commun. Par exemple, si nous créons `tests/common.rs` et y plaçons une fonction nommée `setup`, nous pouvons ajouter du code à `setup` que nous souhaitons appeler à partir de plusieurs fonctions de test dans plusieurs fichiers de test :

Nom de fichier : `tests/common.rs`

```rust
pub fn setup() {
    // Le code de configuration spécifique aux tests de votre bibliothèque irait ici
}
```

Lorsque nous exécutons les tests à nouveau, nous verrons une nouvelle section dans la sortie des tests pour le fichier `common.rs`, même si ce fichier ne contient aucune fonction de test et que nous n'avons pas appelé la fonction `setup` depuis nulle part :

    running 1 test
    test tests::internal... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Que `common` apparaisse dans les résultats des tests avec `running 0 tests` affiché pour elle n'est pas ce que nous voulions. Nous voulions simplement partager du code avec les autres fichiers de test d'intégration. Pour éviter que `common` ne soit affiché dans la sortie des tests, au lieu de créer `tests/common.rs`, nous allons créer `tests/common/mod.rs`. Le répertoire de projet ressemble maintenant à ceci :

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

C'est la convention de nommage plus ancienne que Rust comprend également que nous avons mentionnée dans "Chemins de fichiers alternatifs". Nommer le fichier de cette manière indique à Rust de ne pas traiter le module `common` comme un fichier de test d'intégration. Lorsque nous déplaçons le code de la fonction `setup` dans `tests/common/mod.rs` et que nous supprimons le fichier `tests/common.rs`, la section dans la sortie des tests ne s'affichera plus. Les fichiers dans les sous-répertoires du répertoire `tests` ne sont pas compilés comme des crates séparées ni n'ont de sections dans la sortie des tests.

Après avoir créé `tests/common/mod.rs`, nous pouvons l'utiliser à partir de n'importe quel fichier de test d'intégration en tant que module. Voici un exemple d'appel de la fonction `setup` à partir du test `it_adds_two` dans `tests/integration_test.rs` :

Nom de fichier : `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

Notez que la déclaration `mod common;` est la même que la déclaration de module que nous avons démontrée dans la Liste 7-21. Ensuite, dans la fonction de test, nous pouvons appeler la fonction `common::setup()`.
