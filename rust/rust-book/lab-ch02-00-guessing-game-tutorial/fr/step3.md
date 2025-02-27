# Processing a Guess

La première partie du programme du jeu de devinette demandera l'entrée de l'utilisateur, traitera cette entrée et vérifiera que l'entrée est dans la forme attendue. Pour commencer, nous allons permettre au joueur d'entrer une proposition. Entrez le code de la Liste 2-1 dans `src/main.rs`.

Nom du fichier : `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Liste 2-1 : Code qui obtient une proposition de l'utilisateur et l'affiche

Ce code contient beaucoup d'informations, passons donc en revue chaque ligne. Pour obtenir l'entrée de l'utilisateur puis afficher le résultat en sortie, nous devons inclure la bibliothèque d'entrée/sortie `io` dans la portée. La bibliothèque `io` provient de la bibliothèque standard appelée `std` :

```rust
use std::io;
```

Par défaut, Rust a un ensemble d'éléments définis dans la bibliothèque standard qu'il inclut dans la portée de chaque programme. Cet ensemble est appelé le _préambule_, et vous pouvez voir tout ce qu'il contient sur *https://doc.rust-lang.org/std/prelude/index.html*.

Si un type que vous voulez utiliser n'est pas dans le préambule, vous devez l'inclure explicitement dans la portée avec une instruction `use`. L'utilisation de la bibliothèque `std::io` vous offre un certain nombre de fonctionnalités utiles, y compris la possibilité d'accepter l'entrée de l'utilisateur.

Comme vous l'avez vu au chapitre 1, la fonction `main` est le point d'entrée du programme :

```rust
fn main() {
```

La syntaxe `fn` déclare une nouvelle fonction ; les parenthèses `()` indiquent qu'il n'y a pas de paramètres ; et la accolade `{` démarre le corps de la fonction.

Comme vous l'avez également appris au chapitre 1, `println!` est un macro qui imprime une chaîne sur l'écran :

```rust
println!("Guess the number!");

println!("Please input your guess.");
```

Ce code imprime une invite indiquant ce que le jeu est et demandant une entrée à l'utilisateur.
