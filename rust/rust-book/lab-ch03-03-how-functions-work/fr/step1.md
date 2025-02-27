# Fonctions

Les fonctions sont omniprésentes dans le code Rust. Vous avez déjà vu l'une des fonctions les plus importantes du langage : la fonction `main`, qui est le point d'entrée de nombreux programmes. Vous avez également vu le mot clé `fn`, qui vous permet de déclarer de nouvelles fonctions.

Créez un nouveau projet appelé `functions` :

```bash
cargo new functions
cd functions
```

Le code Rust utilise le _snake case_ comme style conventionnel pour les noms de fonctions et de variables, dans lequel toutes les lettres sont en minuscules et les tirets du bas séparent les mots. Voici un programme qui contient une définition d'une fonction exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Nous définissons une fonction en Rust en entrant `fn` suivi du nom de la fonction et d'un ensemble de parenthèses. Les accolades indiquent au compilateur où commence et se termine le corps de la fonction.

Nous pouvons appeler n'importe quelle fonction que nous avons définie en entrant son nom suivi d'un ensemble de parenthèses. Comme `another_function` est définie dans le programme, elle peut être appelée à l'intérieur de la fonction `main`. Notez que nous avons défini `another_function` _après_ la fonction `main` dans le code source ; nous aurions également pu la définir avant. Rust n'a pas besoin de savoir où vous définissez vos fonctions, seulement qu'elles sont définies quelque part dans une portée visible par l'appelant.

Commencez un nouveau projet binaire nommé _functions_ pour explorer les fonctions plus en détail. Placez l'exemple `another_function` dans `src/main.rs` et exécutez-le. Vous devriez voir la sortie suivante :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

Les lignes s'exécutent dans l'ordre dans lequel elles apparaissent dans la fonction `main`. Tout d'abord, le message "Hello, world!" s'affiche, puis `another_function` est appelée et son message s'affiche.
