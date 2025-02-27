# Écriture et exécution d'un programme Rust

Ensuite, créez un nouveau fichier source et appelez-le `main.rs`. Les fichiers Rust se terminent toujours par l'extension `.rs`. Si vous utilisez plusieurs mots dans votre nom de fichier, la convention est d'utiliser un tiret pour les séparer. Par exemple, utilisez `hello_world.rs` plutôt que `helloworld.rs`.

Maintenant, ouvrez le fichier `main.rs` que vous venez de créer et entrez le code de la Liste 1-1.

Nom de fichier : `main.rs`

```rust
fn main() {
    println!("Bonjour, le monde!");
}
```

Liste 1-1 : Un programme qui imprime `Bonjour, le monde!`

Enregistrez le fichier et revenez à votre fenêtre de terminal dans le répertoire `~/project/hello_world`. Sur Linux ou macOS, entrez les commandes suivantes pour compiler et exécuter le fichier :

```bash
$ rustc main.rs
$./main
Bonjour, le monde!
```

Indépendamment de votre système d'exploitation, la chaîne de caractères `Bonjour, le monde!` devrait s'afficher dans le terminal. Si vous ne voyez pas cette sortie, reportez-vous à "Dépannage" pour trouver des moyens de vous aider.

Si `Bonjour, le monde!` s'est effectivement affiché, félicitations! Vous avez officiellement écrit un programme Rust. Cela vous fait un programmeur Rust - bienvenue!
