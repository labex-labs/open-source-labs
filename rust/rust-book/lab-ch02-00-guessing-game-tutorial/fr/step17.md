# Gérer les entrées invalides

Pour affiner encore le comportement du jeu, plutôt que de faire planter le programme lorsque l'utilisateur entre un non-nombre, faisons en sorte que le jeu ignore un non-nombre pour que l'utilisateur puisse continuer à deviner. Nous pouvons le faire en modifiant la ligne où `guess` est converti d'une `String` en un `u32`, comme montré dans la Liste 2-5.

Nom de fichier : `src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

Liste 2-5 : Ignorer une proposition non numérique et demander une autre proposition au lieu de faire planter le programme

Nous passons d'un appel à `expect` à une expression `match` pour passer de la plantation en cas d'erreur à la gestion de l'erreur. Rappelez-vous que `parse` renvoie un type `Result` et que `Result` est un enum qui a les variantes `Ok` et `Err`. Nous utilisons une expression `match` ici, comme nous l'avons fait avec le résultat `Ordering` de la méthode `cmp`.

Si `parse` est capable de convertir avec succès la chaîne en un nombre, elle renverra une valeur `Ok` qui contient le nombre résultant. Cette valeur `Ok` correspondra au schéma du premier bras, et l'expression `match` renverra simplement la valeur `num` que `parse` a produite et placée dans la valeur `Ok`. Ce nombre se retrouvera exactement où nous le voulons dans la nouvelle variable `guess` que nous créons.

Si `parse` _n'est pas_ capable de convertir la chaîne en un nombre, elle renverra une valeur `Err` qui contient plus d'informations sur l'erreur. La valeur `Err` ne correspond pas au schéma `Ok(num)` dans le premier bras `match`, mais elle correspond au schéma `Err(_)` dans le second bras. Le tiret bas, `_`, est une valeur générique ; dans cet exemple, nous disons que nous voulons correspondre à toutes les valeurs `Err`, quelle que soit l'information qu'elles contiennent à l'intérieur. Le programme exécutera donc le code du second bras, `continue`, qui indique au programme d'aller à l'itération suivante de la `loop` et de demander une autre proposition. Ainsi, en fait, le programme ignore toutes les erreurs que `parse` pourrait rencontrer!

Maintenant, tout dans le programme devrait fonctionner comme prévu. Essayons :

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

Génial! Avec un dernier ajustement minuscule, nous terminerons le jeu de devinette. Rappelez-vous que le programme imprime toujours le nombre secret. Cela a bien fonctionné pour les tests, mais cela gâche le jeu. Supprimons l'instruction `println!` qui affiche le nombre secret. La Liste 2-6 montre le code final.

Nom de fichier : `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

Liste 2-6 : Code complet du jeu de devinette

À ce stade, vous avez construit avec succès le jeu de devinette. Félicitations!
