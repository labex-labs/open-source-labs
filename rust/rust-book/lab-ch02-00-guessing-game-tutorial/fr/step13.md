# Générer un nombre aléatoire

Commenceons à utiliser `rand` pour générer un nombre à deviner. La prochaine étape est de mettre à jour `src/main.rs`, comme indiqué dans la Liste 2-3.

Nom de fichier : `src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Liste 2-3 : Ajout de code pour générer un nombre aléatoire

Tout d'abord, nous ajoutons la ligne `use rand::Rng;` \[1\]. Le trait `Rng` définit les méthodes que les générateurs de nombres aléatoires implémentent, et ce trait doit être dans la portée pour que nous puissions utiliser ces méthodes. Le Chapitre 10 couvrira les traits en détail.

Ensuite, nous ajoutons deux lignes au milieu. Dans la première ligne \[2\], nous appelons la fonction `rand::thread_rng` qui nous donne le générateur de nombres aléatoires particulier que nous allons utiliser : celui qui est local au fil d'exécution actuel et est initialisé par le système d'exploitation. Ensuite, nous appelons la méthode `gen_range` sur le générateur de nombres aléatoires. Cette méthode est définie par le trait `Rng` que nous avons mis dans la portée avec l'instruction `use rand::Rng;`. La méthode `gen_range` prend une expression de plage en argument et génère un nombre aléatoire dans la plage. Le type d'expression de plage que nous utilisons ici prend la forme `start..=end` et est inclusive pour les bornes inférieure et supérieure, donc nous devons spécifier `1..=100` pour demander un nombre entre 1 et 100.

> Note : Vous ne saurez pas tout de suite quels traits utiliser et quelles méthodes et fonctions appeler à partir d'un paquet, donc chaque paquet a une documentation avec des instructions pour l'utiliser. Une autre fonction pratique de Cargo est que l'exécution de la commande `cargo doc --open` construira la documentation fournie par toutes vos dépendances localement et l'ouvrira dans votre navigateur. Si vous êtes intéressé par d'autres fonctionnalités dans le paquet `rand`, par exemple, exécutez `cargo doc --open` et cliquez sur `rand` dans la barre latérale de gauche.

La deuxième nouvelle ligne \[3\] affiche le nombre secret. Cela est utile pendant que nous développons le programme pour pouvoir le tester, mais nous le supprimerons de la version finale. Ce n'est pas vraiment un jeu si le programme affiche la réponse dès le début!

Essayez d'exécuter le programme plusieurs fois :

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

Vous devriez obtenir des nombres aléatoires différents, et ils devraient tous être des nombres entre 1 et 100. Bravo!
