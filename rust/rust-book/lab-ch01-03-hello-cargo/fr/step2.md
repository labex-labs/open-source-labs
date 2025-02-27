# Création d'un projet avec Cargo

Créeons un nouveau projet avec Cargo et examinons en quoi il diffère de notre projet original "Hello, world!". Revoyez dans votre répertoire `project` (ou n'importe où vous avez décidé de stocker votre code). Ensuite, sur n'importe quel système d'exploitation, exécutez les commandes suivantes :

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

La première commande crée un nouveau répertoire et un nouveau projet appelé _hello_cargo_. Nous avons nommé notre projet _hello_cargo_, et Cargo crée ses fichiers dans un répertoire du même nom.

Entrez dans le répertoire `hello_cargo` et liste les fichiers. Vous verrez que Cargo a généré deux fichiers et un répertoire pour nous : un fichier `Cargo.toml` et un répertoire `src` contenant un fichier `main.rs`.

Il a également initialisé un nouveau référentiel Git ainsi qu'un fichier _.gitignore_. Les fichiers Git ne seront pas générés si vous exécutez `cargo new` dans un référentiel Git existant ; vous pouvez contourner ce comportement en utilisant `cargo new --vcs=git`.

> Note : Git est un système de contrôle de version courant. Vous pouvez modifier `cargo new` pour utiliser un autre système de contrôle de version ou aucun système de contrôle de version en utilisant le drapeau `--vcs`. Exécutez `cargo new --help` pour voir les options disponibles.

Ouvrez `Cargo.toml` dans votre éditeur de texte favori. Il devrait ressembler au code de la Liste 1-2.

Nom de fichier : `Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

Liste 1-2 : Contenu de `Cargo.toml` généré par `cargo new`

Ce fichier est au format _TOML_ (_Tom's Obvious, Minimal Language_), qui est le format de configuration de Cargo.

La première ligne, `[package]`, est un en-tête de section qui indique que les déclarations suivantes configurent un package. Lorsque nous ajouterons plus d'informations à ce fichier, nous ajouterons d'autres sections.

Les trois lignes suivantes définissent les informations de configuration dont Cargo a besoin pour compiler votre programme : le nom, la version et l'édition de Rust à utiliser. Nous parlerons de la clé `edition` dans l'Annexe E.

La dernière ligne, `[dependencies]`, est le début d'une section où vous pouvez lister toutes les dépendances de votre projet. En Rust, les packages de code sont appelés _crates_. Nous n'aurons pas besoin d'autres crates pour ce projet, mais nous en aurons besoin dans le premier projet du Chapitre 2, donc nous utiliserons cette section de dépendances alors.

Maintenant, ouvrez `src/main.rs` et regardez :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo a généré un programme "Hello, world!" pour vous, tout comme celui que nous avons écrit dans la Liste 1-1! Jusqu'à présent, les différences entre notre projet et le projet généré par Cargo sont que Cargo a placé le code dans le répertoire `src` et que nous avons un fichier de configuration `Cargo.toml` dans le répertoire supérieur.

Cargo s'attend à ce que vos fichiers sources se trouvent à l'intérieur du répertoire `src`. Le répertoire racine du projet est juste pour les fichiers README, les informations de licence, les fichiers de configuration et tout autre élément non lié à votre code. Utiliser Cargo vous aide à organiser vos projets. Il y a un endroit pour tout, et tout est à sa place.

Si vous avez commencé un projet qui ne utilise pas Cargo, comme nous l'avons fait avec le projet "Hello, world!", vous pouvez le convertir en un projet qui utilise Cargo. Déplacez le code du projet dans le répertoire `src` et créez un fichier `Cargo.toml` approprié.
