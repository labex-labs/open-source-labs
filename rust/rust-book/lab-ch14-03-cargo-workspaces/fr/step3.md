# Création du second package dans l'espace de travail

Ensuite, créons un autre package membre dans l'espace de travail et appelons-le `add_one`. Modifions le `Cargo.toml` de niveau supérieur pour spécifier le chemin _add_one_ dans la liste `members` :

Nom du fichier : `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

Ensuite, générez un nouveau crâne de bibliothèque nommé `add_one` :

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

Votre répertoire `add` devrait maintenant avoir ces répertoires et fichiers :

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

Dans le fichier `add_one/src/lib.rs`, ajoutons une fonction `add_one` :

Nom du fichier : `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Maintenant, nous pouvons avoir le package `adder` avec notre binaire dépendant du package `add_one` qui contient notre bibliothèque. Tout d'abord, nous devrons ajouter une dépendance de chemin sur `add_one` à _adder/Cargo.toml_ :

Nom du fichier : `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo n'assume pas que les crânes dans un espace de travail dépendront les uns des autres, donc nous devons être explicites sur les relations de dépendance.

Ensuite, utilisons la fonction `add_one` (du crâne `add_one`) dans le crâne `adder`. Ouvrez le fichier `adder/src/main.rs` et ajoutez une ligne `use` en haut pour porter le nouveau crâne de bibliothèque `add_one` dans la portée. Ensuite, modifiez la fonction `main` pour appeler la fonction `add_one`, comme dans la Liste 14-7.

Nom du fichier : `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Liste 14-7 : Utilisation du crâne de bibliothèque `add_one` à partir du crâne `adder`

Construisons l'espace de travail en exécutant `cargo build` dans le répertoire _add_ de niveau supérieur!

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

Pour exécuter le crâne binaire à partir du répertoire `add`, nous pouvons spécifier quel package dans l'espace de travail nous voulons exécuter en utilisant l'argument `-p` et le nom du package avec `cargo run` :

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

Cela exécute le code dans `adder/src/main.rs`, qui dépend du crâne `add_one`.
