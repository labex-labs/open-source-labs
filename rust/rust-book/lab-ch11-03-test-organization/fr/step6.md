# Le répertoire tests

Nous créons un répertoire `tests` au niveau supérieur de notre répertoire de projet, à côté de `src`. Cargo sait chercher les fichiers de test d'intégration dans ce répertoire. Nous pouvons ensuite créer autant de fichiers de test que nous le souhaitons, et Cargo compilera chacun des fichiers comme une crate individuelle.

Créons un test d'intégration. Avec le code de la Liste 11-12 toujours dans le fichier `src/lib.rs`, créez un répertoire `tests`, puis un nouveau fichier nommé `tests/integration_test.rs`. La structure de votre répertoire devrait ressembler à ceci :

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

Entrez le code de la Liste 11-13 dans le fichier `tests/integration_test.rs`.

Nom de fichier : `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

Liste 11-13 : Un test d'intégration d'une fonction dans la crate `adder`

Chaque fichier dans le répertoire `tests` est une crate séparée, donc nous devons inclure notre bibliothèque dans la portée de chaque crate de test. C'est pourquoi nous ajoutons `use adder;` en haut du code, ce que nous n'avions pas besoin pour les tests unitaires.

Nous n'avons pas besoin d'ajouter l'annotation `#[cfg(test)]` à aucun code dans `tests/integration_test.rs`. Cargo traite le répertoire `tests` de manière spéciale et ne compile les fichiers de ce répertoire que lorsque nous exécutons `cargo test`. Exécutez maintenant `cargo test` :

```bash

```

Les trois sections de sortie incluent les tests unitaires, le test d'intégration et les tests de documentation. Notez que si un test dans une section échoue, les sections suivantes ne seront pas exécutées. Par exemple, si un test unitaire échoue, il n'y aura pas de sortie pour les tests d'intégration et de documentation car ces tests ne seront exécutés que si tous les tests unitaires sont passés.

La première section pour les tests unitaires [1] est la même que celle que nous avons vue jusqu'à présent : une ligne pour chaque test unitaire (une nommé `internal` que nous avons ajouté dans la Liste 11-12) puis une ligne de synthèse pour les tests unitaires.

La section des tests d'intégration commence par la ligne `Running tests/integration_test.rs` [2]. Ensuite, il y a une ligne pour chaque fonction de test dans ce test d'intégration [3] et une ligne de synthèse pour les résultats du test d'intégration [4] juste avant le début de la section `Doc-tests adder`.

Chaque fichier de test d'intégration a sa propre section, donc si nous ajoutons plus de fichiers dans le répertoire `tests`, il y aura plus de sections de test d'intégration.

Nous pouvons toujours exécuter une fonction de test d'intégration particulière en spécifiant le nom de la fonction de test en tant qu'argument de `cargo test`. Pour exécuter tous les tests dans un fichier de test d'intégration particulier, utilisez l'argument `--test` de `cargo test` suivi du nom du fichier :

```bash

```

Cette commande exécute seulement les tests dans le fichier `tests/integration_test.rs`.
