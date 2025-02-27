# Tests unitaires

Les tests sont des fonctions Rust qui vérifient que le code non de test fonctionne comme prévu. Les corps des fonctions de test effectuent généralement un certain paramétrage, exécutent le code que nous souhaitons tester, puis affirment si les résultats sont ceux que nous attendons.

La plupart des tests unitaires sont placés dans un module `tests` avec l'attribut `#[cfg(test)]`. Les fonctions de test sont marquées avec l'attribut `#[test]`.

Les tests échouent lorsqu'une erreur survient dans la fonction de test. Voici quelques macros d'assistance :

- `assert!(expression)` - génère une erreur si l'expression vaut `false`.
- `assert_eq!(gauche, droite)` et `assert_ne!(gauche, droite)` - testent l'égalité et l'inégalité respectivement des expressions gauche et droite.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Cette fonction d'addition est vraiment mauvaise, son but est de
// échouer dans cet exemple.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // Notez cette habitude pratique : importer des noms du scope externe
    // (pour les tests de module).
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // Cette assertion provoquera une erreur et le test échouera.
        // Notez que les fonctions privées peuvent également être testées!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

Les tests peuvent être exécutés avec `cargo test`.

```shell
$ cargo test

running 2 tests
test tests::test_bad_add... FAILED
test tests::test_add... ok

failures:

---- tests::test_bad_add stdout ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
note: Run with $(RUST_BACKTRACE=1) for a backtrace.

failures:
tests::test_bad_add

test result: FAILED. 1 passed
1 failed
0 ignored
0 measured
0 filtered out
```

## Tests et `?`

Aucun des exemples de tests unitaires précédents n'avait un type de retour. Mais dans Rust 2018, vos tests unitaires peuvent renvoyer `Result<()>`, ce qui vous permet d'utiliser `?` dans eux! Cela peut les rendre beaucoup plus concis.

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("negative floats don't have square roots".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

Consultez "The Edition Guide" pour plus de détails.

## Test des panics

Pour vérifier les fonctions qui devraient provoquer une erreur dans certaines circonstances, utilisez l'attribut `#[should_panic]`. Cet attribut accepte un paramètre optionnel `expected =` avec le texte du message d'erreur. Si votre fonction peut provoquer une erreur de plusieurs manières, cela aide à vous assurer que votre test vérifie la bonne erreur.

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

En exécutant ces tests, nous obtenons :

```shell
$ cargo test

running 3 tests
test tests::test_any_panic... ok
test tests::test_divide... ok
test tests::test_specific_panic... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Exécution de tests spécifiques

Pour exécuter des tests spécifiques, on peut spécifier le nom du test à la commande `cargo test`.

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
2 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

Pour exécuter plusieurs tests, on peut spécifier une partie du nom du test qui correspond à tous les tests qui doivent être exécutés.

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic... ok
test tests::test_specific_panic... ok

test result: ok. 2 passed
0 failed
0 ignored
0 measured
1 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## Ignorer des tests

Les tests peuvent être marqués avec l'attribut `#[ignore]` pour exclure certains tests. Ou pour les exécuter avec la commande `cargo test -- --ignored`

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test... ignored
test tests::test_add... ok
test tests::test_add_hundred... ok

test result: ok. 2 passed
0 failed
1 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

$ cargo test -- --ignored
running 1 test
test tests::ignored_test... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```
