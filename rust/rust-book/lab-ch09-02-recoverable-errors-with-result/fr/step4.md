# Shortcuts for Panic on Error: unwrap and expect

Utiliser `match` fonctionne assez bien, mais cela peut être un peu verbeux et ne communique pas toujours bien l'intention. Le type `Result<T, E>` a de nombreuses méthodes d'aide définies dessus pour effectuer diverses tâches plus spécifiques. La méthode `unwrap` est une méthode raccourcie implémentée de la même manière que l'expression `match` que nous avons écrite dans la liste 9-4. Si la valeur `Result` est la variante `Ok`, `unwrap` renverra la valeur à l'intérieur de `Ok`. Si le `Result` est la variante `Err`, `unwrap` appellera la macro `panic!` pour nous. Voici un exemple d'utilisation de `unwrap` :

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

Si nous exécutons ce code sans le fichier _hello.txt_, nous verrons un message d'erreur provenant de l'appel à `panic!` que la méthode `unwrap` effectue :

    thread'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

De manière similaire, la méthode `expect` nous permet également de choisir le message d'erreur de `panic!`. En utilisant `expect` au lieu de `unwrap` et en fournissant de bons messages d'erreur, vous pouvez exprimer votre intention et faciliter la recherche de la source d'une panique. La syntaxe de `expect` est la suivante :

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt should be included in this project");
}
```

Nous utilisons `expect` de la même manière que `unwrap` : pour renvoyer le pointeur de fichier ou appeler la macro `panic!`. Le message d'erreur utilisé par `expect` dans son appel à `panic!` sera le paramètre que nous passons à `expect`, plutôt que le message d'erreur par défaut que `unwrap` utilise. Voici à quoi cela ressemble :

    thread'main' panicked at 'hello.txt should be included in this project: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

Dans un code de production de qualité, la plupart des Rustaceans choisissent `expect` plutôt que `unwrap` et donnent plus de contexte sur pourquoi on s'attend à ce que l'opération réussisse toujours. Ainsi, si vos hypothèses se révèlent jamais fausses, vous avez plus d'informations pour le débogage.
