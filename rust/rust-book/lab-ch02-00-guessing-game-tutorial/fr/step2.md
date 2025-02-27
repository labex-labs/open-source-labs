# Setting Up a New Project

Pour créer un nouveau projet, accédez au répertoire `project` que vous avez créé au chapitre 1 et créez un nouveau projet avec Cargo, comme ceci :

```bash
cargo new guessing_game
cd guessing_game
```

La première commande, `cargo new`, prend le nom du projet (`guessing_game`) comme premier argument. La deuxième commande change dans le répertoire du nouveau projet.

Regardez le fichier `Cargo.toml` généré :

Nom du fichier : `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# Consultez plus de clés et leurs définitions à
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Comme vous l'avez vu au chapitre 1, `cargo new` génère un programme "Bonjour, le monde!" pour vous. Vérifiez le fichier `src/main.rs` :

Nom du fichier : `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Maintenant, compilons ce programme "Bonjour, le monde!" et exécutons-le dans la même étape en utilisant la commande `cargo run` :

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

La commande `run` est pratique lorsque vous avez besoin d'itérer rapidement sur un projet, comme nous le ferons dans ce jeu, en testant rapidement chaque itération avant de passer à la suivante.

Réouvrez le fichier `src/main.rs`. Vous allez écrire tout le code dans ce fichier.
