# Commentaires de documentation en tant que tests

Ajouter des blocs de code exemple dans vos commentaires de documentation peut aider à démontrer comment utiliser votre bibliothèque, et ce faisant présente un avantage supplémentaire : exécuter `cargo test` exécutera les exemples de code de votre documentation en tant que tests! Rien n'est mieux que de la documentation avec des exemples. Mais rien n'est pire que des exemples qui ne fonctionnent pas parce que le code a changé depuis que la documentation a été écrite. Si nous exécutons `cargo test` avec la documentation de la fonction `add_one` de la liste 14-1, nous verrons une section dans les résultats des tests qui ressemblera à ceci :

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5)... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

Maintenant, si nous modifions soit la fonction soit l'exemple de sorte que l'`assert_eq!` dans l'exemple génère une panique et que nous exécutons `cargo test` à nouveau, nous verrons que les tests de documentation détectent que l'exemple et le code sont désynchronisés l'un par rapport à l'autre!
