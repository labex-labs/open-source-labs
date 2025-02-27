# Exécuter un seul test

Nous pouvons passer le nom de n'importe quelle fonction de test à `cargo test` pour exécuter seulement ce test :

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

Seul le test avec le nom `one_hundred` a été exécuté ; les deux autres tests ne correspondent pas à ce nom. La sortie du test nous informe qu'il y avait plus de tests qui n'ont pas été exécutés en affichant `2 filtrés` à la fin.

Nous ne pouvons pas spécifier les noms de plusieurs tests de cette manière ; seule la première valeur donnée à `cargo test` sera utilisée. Mais il existe un moyen d'exécuter plusieurs tests.
