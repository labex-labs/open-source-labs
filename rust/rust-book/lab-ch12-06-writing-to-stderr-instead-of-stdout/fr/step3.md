# Imprimer les erreurs sur la sortie d'erreur standard

Nous allons utiliser le code de la Liste 12-24 pour changer la façon dont les messages d'erreur sont imprimés. En raison du refactoring que nous avons effectué plus tôt dans ce chapitre, tout le code qui imprime les messages d'erreur est dans une seule fonction, `main`. La bibliothèque standard fournit la macro `eprintln!` qui imprime sur le flux de sortie d'erreur standard, donc modifions les deux endroits où nous appelions `println!` pour imprimer des erreurs pour utiliser `eprintln!` à la place.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Liste 12-24 : Écrire des messages d'erreur sur la sortie d'erreur standard au lieu de la sortie standard en utilisant `eprintln!`

Exécutons maintenant le programme à nouveau de la même manière, sans aucun argument et en redirigeant la sortie standard avec `>` :

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

Maintenant, nous voyons l'erreur à l'écran et _output.txt_ est vide, ce qui est le comportement que nous attendons des programmes de ligne de commande.

Exécutons le programme à nouveau avec des arguments qui ne provoquent pas d'erreur mais qui redirigent toujours la sortie standard vers un fichier, comme ceci :

```bash
cargo run -- to poem.txt > output.txt
```

Nous n'allons pas voir de sortie sur le terminal, et _output.txt_ contiendra nos résultats :

Nom de fichier : output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

Cela démontre que nous utilisons maintenant la sortie standard pour la sortie réussie et la sortie d'erreur standard pour la sortie d'erreur, comme il se doit.
