# Afficher la sortie de la fonction

Par défaut, si un test réussit, la bibliothèque de tests de Rust capture tout ce qui est imprimé sur la sortie standard. Par exemple, si nous appelons `println!` dans un test et que le test réussit, nous ne verrons pas la sortie de `println!` dans le terminal ; nous verrons seulement la ligne indiquant que le test a réussi. Si un test échoue, nous verrons tout ce qui a été imprimé sur la sortie standard avec le reste du message d'erreur.

Par exemple, la Liste 11-10 a une fonction stupide qui imprime la valeur de son paramètre et renvoie 10, ainsi qu'un test qui réussit et un test qui échoue.

Nom de fichier : `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Liste 11-10 : Tests pour une fonction qui appelle `println!`

Lorsque nous exécutons ces tests avec `cargo test`, nous verrons la sortie suivante :

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Remarquez que nulle part dans cette sortie, nous ne voyons pas `I got the value 4`, qui est imprimé lorsque le test qui réussit est exécuté. Cette sortie a été capturée. La sortie du test qui a échoué, `I got the value 8` \[1\], apparaît dans la section de la sortie du résumé des tests, qui montre également la cause de l'échec du test.

Si nous voulons également voir les valeurs imprimées pour les tests réussis, nous pouvons demander à Rust de montrer également la sortie des tests réussis avec `--show-output` :

```bash
cargo test -- --show-output
```

Lorsque nous exécutons à nouveau les tests de la Liste 11-10 avec le drapeau `--show-output`, nous voyons la sortie suivante :

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
