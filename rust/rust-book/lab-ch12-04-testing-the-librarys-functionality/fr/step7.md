# Utiliser la fonction search dans la fonction run

Maintenant que la fonction `search` fonctionne et a été testée, nous devons appeler `search` depuis notre fonction `run`. Nous devons passer la valeur `config.query` et le `contents` que `run` lit à partir du fichier à la fonction `search`. Ensuite, `run` imprimera chaque ligne renvoyée par `search` :

Nom de fichier : `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

Nous utilisons toujours une boucle `for` pour renvoyer chaque ligne de `search` et l'imprimer.

Maintenant, tout le programme devrait fonctionner! Essayons-le, d'abord avec un mot qui devrait renvoyer exactement une ligne du poème d'Emily Dickinson : _frog_.

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

Génial! Maintenant, essayons un mot qui correspondra à plusieurs lignes, comme _body_ :

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

Et finalement, vérifions que nous n'obtenons pas de lignes lorsqu'on cherche un mot qui n'est nulle part dans le poème, tel que _monomorphization_ :

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

Excellent! Nous avons construit notre propre version mini d'un outil classique et avons appris beaucoup sur la structure des applications. Nous avons également appris un peu sur l'entrée et la sortie de fichiers, les durées de vie, les tests et l'analyse de la ligne de commande.

Pour compléter ce projet, nous allons brièvement démontrer comment travailler avec les variables d'environnement et comment imprimer sur la sortie d'erreur standard, qui sont tous deux utiles lorsqu'on écrit des programmes de ligne de commande.
