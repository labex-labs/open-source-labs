# Fixing the Error Handling

Maintenant, nous allons corriger notre gestion des erreurs. Rappelez-vous que tenter d'accéder aux valeurs dans le vecteur `args` à l'index 1 ou index 2 entraînera une panique du programme si le vecteur contient moins de trois éléments. Essayez d'exécuter le programme sans arguments ; cela ressemblera à ceci :

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

La ligne `index out of bounds: the len is 1 but the index is 1` est un message d'erreur destiné aux programmeurs. Cela n'aidera pas nos utilisateurs finaux à comprendre ce qu'ils devraient faire à la place. Corrigeons cela maintenant.
