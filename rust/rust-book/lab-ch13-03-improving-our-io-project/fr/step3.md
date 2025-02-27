# Utiliser directement l'itérateur renvoyé

Ouvrez le fichier `src/main.rs` de votre projet E/S, qui devrait ressembler à ceci :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

Nous allons tout d'abord modifier le début de la fonction `main` que nous avions dans la liste 12-24 pour le code de la liste 13-18, qui utilise cette fois un itérateur. Cela ne compilera pas tant que nous n'aurons pas mis à jour `Config::build` également.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

Liste 13-18 : Passer la valeur de retour de `env::args` à `Config::build`

La fonction `env::args` renvoie un itérateur! Au lieu de collecter les valeurs de l'itérateur dans un vecteur puis de passer une tranche à `Config::build`, nous passons maintenant la propriété de l'itérateur renvoyé par `env::args` directement à `Config::build`.

Ensuite, nous devons mettre à jour la définition de `Config::build`. Dans le fichier `src/lib.rs` de votre projet E/S, modifions la signature de `Config::build` pour qu'elle ressemble à la liste 13-19. Cela ne compilera toujours pas, car nous devons mettre à jour le corps de la fonction.

Nom de fichier : `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

Liste 13-19 : Mettre à jour la signature de `Config::build` pour attendre un itérateur

La documentation de la bibliothèque standard pour la fonction `env::args` indique que le type de l'itérateur qu'elle renvoie est `std::env::Args`, et que ce type implémente la trait `Iterator` et renvoie des valeurs de type `String`.

Nous avons mis à jour la signature de la fonction `Config::build` de sorte que le paramètre `args` ait un type générique avec les contraintes de trait `impl Iterator<Item = String>` au lieu de `&[String]`. Cette utilisation de la syntaxe `impl Trait` que nous avons discutée dans "Traits en tant que paramètres" signifie que `args` peut être n'importe quel type qui implémente le type `Iterator` et renvoie des éléments de type `String`.

Comme nous prenons la propriété de `args` et que nous allons modifier `args` en itérant dessus, nous pouvons ajouter le mot clé `mut` dans la spécification du paramètre `args` pour le rendre mutable.
