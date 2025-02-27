# Répéter du code avec `loop`

Le mot-clé `loop` indique à Rust d'exécuter un bloc de code à l'infini ou jusqu'à ce que vous lui disiez explicitement de s'arrêter.

Par exemple, modifiez le fichier `src/main.rs` dans votre répertoire `boucles` pour qu'il ressemble à ceci :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    loop {
        println!("encore!");
    }
}
```

Lorsque nous exécutons ce programme, nous verrons `encore!` affiché à l'infini jusqu'à ce que nous arrêtions le programme manuellement. La plupart des terminaux prennent en charge le raccourci clavier ctrl-C pour interrompre un programme qui est bloqué dans une boucle infinie. Essayez-le :

```bash
$ cargo run
   Compiling boucles v0.1.0 (file:///projets/boucles)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s
     Running `target/debug/boucles`
encore!
encore!
encore!
encore!
^Cencore!
```

Le symbole `^C` représente le moment où vous avez appuyé sur ctrl-C. Vous pouvez ou non voir le mot `encore!` affiché après le `^C`, selon où le code se trouvait dans la boucle lorsqu'il a reçu le signal d'interruption.

Heureusement, Rust fournit également un moyen de sortir d'une boucle en utilisant du code. Vous pouvez placer le mot-clé `break` à l'intérieur de la boucle pour dire au programme quand arrêter d'exécuter la boucle. Rappelez-vous que nous avons fait cela dans le jeu de devinette dans "Quitter après avoir deviné correctement" pour quitter le programme lorsque l'utilisateur a gagné le jeu en devinant le bon nombre.

Nous avons également utilisé `continue` dans le jeu de devinette, qui dans une boucle indique au programme de sauter le reste du code dans cette itération de la boucle et de passer à l'itération suivante.
