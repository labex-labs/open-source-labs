# Filtrer pour exécuter plusieurs tests

Nous pouvons spécifier une partie du nom d'un test, et tout test dont le nom correspond à cette valeur sera exécuté. Par exemple, puisque deux de nos noms de test contiennent `add`, nous pouvons exécuter ces deux tests en exécutant `cargo test add` :

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Cette commande a exécuté tous les tests dont le nom contient `add` et a filtré le test nommé `one_hundred`. Notez également que le module dans lequel un test apparaît devient une partie du nom du test, de sorte que nous pouvons exécuter tous les tests d'un module en filtrant sur le nom du module.
