# Autoriser plusieurs propositions avec une boucle

Le mot clé `loop` crée une boucle infinie. Nous allons ajouter une boucle pour donner aux utilisateurs plus de chances de deviner le nombre :

Nom de fichier : `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = guess
         .trim()
         .parse()
         .expect("Please type a number!");

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }
}
```

Comme vous pouvez le voir, nous avons déplacé tout à partir de l'invite d'entrée de la proposition jusqu'à la boucle. Assurez-vous d'indenter les lignes à l'intérieur de la boucle de quatre espaces supplémentaires chacune et exécutez le programme à nouveau. Le programme demandera désormais une nouvelle proposition à l'infini, ce qui introduit en fait un nouveau problème. Il semble que l'utilisateur ne puisse pas quitter!

L'utilisateur pourrait toujours interrompre le programme en utilisant le raccourci clavier ctrl-C. Mais il y a un autre moyen d'échapper à ce monstre insatiable, comme mentionné dans la discussion de `parse` dans "Comparer la proposition avec le nombre secret" : si l'utilisateur entre une réponse non numérique, le programme plantera. Nous pouvons en profiter pour permettre à l'utilisateur de quitter, comme montré ici :

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
quit
thread'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Taper `quit` quittera le jeu, mais comme vous le remarquerez, entrer n'importe quelle autre entrée non numérique le fera également. Cela est du moins suboptimal ; nous voulons que le jeu s'arrête également lorsque le nombre correct est deviné.
