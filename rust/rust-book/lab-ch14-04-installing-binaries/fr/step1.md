# Installing Binaries with cargo install

La commande `cargo install` vous permet d'installer et d'utiliser localement des crânes binaires. Cela n'est pas destiné à remplacer les paquets système ; il s'agit d'un moyen pratique pour les développeurs Rust d'installer des outils que d'autres ont partagés sur *https://crates.io*. Notez que vous ne pouvez installer que des packages qui ont des cibles binaires. Une _cible binaire_ est le programme exécutable qui est créé si le crâne a un fichier `src/main.rs` ou un autre fichier spécifié comme binaire, contrairement à une cible de bibliothèque qui n'est pas exécutable par elle-même mais est appropriée pour être incluse dans d'autres programmes. En général, les crânes ont des informations dans le fichier _README_ sur le fait qu'un crâne est une bibliothèque, a une cible binaire ou les deux.

Tous les binaires installés avec `cargo install` sont stockés dans le dossier `bin` de la racine d'installation. Si vous avez installé Rust à l'aide de `rustup.rs` et que vous n'avez pas de configurations personnalisées, ce répertoire sera `$HOME/.cargo/bin`. Assurez-vous que ce répertoire est dans votre `$PATH` pour pouvoir exécuter les programmes que vous avez installés avec `cargo install`.

Par exemple, au chapitre 12, nous avons mentionné qu'il existe une implémentation Rust de l'outil `grep` appelé `ripgrep` pour rechercher des fichiers. Pour installer `ripgrep`, nous pouvons exécuter ce qui suit :

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

L'avant-dernière ligne de la sortie montre l'emplacement et le nom du binaire installé, qui dans le cas de `ripgrep` est `rg`. Tant que le répertoire d'installation est dans votre `$PATH`, comme mentionné précédemment, vous pouvez ensuite exécuter `rg --help` et commencer à utiliser un outil plus rapide et plus Rustique pour rechercher des fichiers!
