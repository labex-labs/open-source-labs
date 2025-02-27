#Comparer la proposition avec le nombre secret

Maintenant que nous avons une entrée utilisateur et un nombre aléatoire, nous pouvons les comparer. Cette étape est montrée dans la Liste 2-4. Notez que ce code ne compilera pas encore, comme nous allons l'expliquer.

Nom de fichier : `src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Liste 2-4 : Gérer les valeurs de retour possibles de la comparaison de deux nombres

Tout d'abord, nous ajoutons une autre instruction `use` \[1\], qui importe un type appelé `std::cmp::Ordering` depuis la bibliothèque standard. Le type `Ordering` est un autre enum et a les variantes `Less`, `Greater` et `Equal`. Ces sont les trois résultats possibles lorsqu'on compare deux valeurs.

Ensuite, nous ajoutons cinq nouvelles lignes en bas qui utilisent le type `Ordering`. La méthode `cmp` \[3\] compare deux valeurs et peut être appelée sur tout ce qui peut être comparé. Elle prend une référence à ce que vous voulez comparer : ici, elle compare `guess` avec `secret_number`. Ensuite, elle renvoie une variante de l'enum `Ordering` que nous avons importé avec l'instruction `use`. Nous utilisons une expression `match` \[2\] pour décider de ce qu'il faut faire ensuite en fonction de la variante de `Ordering` qui a été renvoyée par l'appel à `cmp` avec les valeurs de `guess` et `secret_number`.

Une expression `match` est composée de _bras_. Un bras est composé d'un _schéma_ à comparer, et du code qui devrait être exécuté si la valeur donnée à `match` correspond au schéma de cet bras. Rust prend la valeur donnée à `match` et parcourt successivement les schémas de chaque bras. Les schémas et la structure `match` sont des fonctionnalités puissantes de Rust : elles vous permettent d'exprimer diverses situations que votre code peut rencontrer et vous assurent de les gérer toutes. Ces fonctionnalités seront couvertes en détail respectivement au Chapitre 6 et au Chapitre 18.

Parcourons un exemple avec l'expression `match` que nous utilisons ici. Disons que l'utilisateur a deviné 50 et que le nombre secret généré aléatoirement cette fois est 38.

Lorsque le code compare 50 avec 38, la méthode `cmp` renverra `Ordering::Greater` car 50 est supérieur à 38. L'expression `match` reçoit la valeur `Ordering::Greater` et commence à vérifier chaque schéma d'arm. Elle regarde le schéma du premier bras, `Ordering::Less`, et constate que la valeur `Ordering::Greater` ne correspond pas à `Ordering::Less`, donc elle ignore le code de cet bras et passe au suivant. Le schéma du bras suivant est `Ordering::Greater`, qui _correspond_ à `Ordering::Greater`! Le code associé à cet bras sera exécuté et affichera `Too big!` à l'écran. L'expression `match` se termine après le premier match réussi, donc elle ne regardera pas le dernier bras dans ce scénario.

Cependant, le code de la Liste 2-4 ne compilera pas encore. Essayons :

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

Le cœur de l'erreur indique qu'il y a des _types non compatibles_. Rust a un système de types fort et statique. Cependant, il a également une inférence de type. Lorsque nous avons écrit `let mut guess = String::new()`, Rust a été capable d'inférer que `guess` devrait être une `String` et ne nous a pas obligé à écrire le type. En revanche, `secret_number` est un type numérique. Plusieurs types numériques de Rust peuvent avoir une valeur comprise entre 1 et 100 : `i32`, un nombre sur 32 bits ; `u32`, un nombre non signé sur 32 bits ; `i64`, un nombre sur 64 bits ; ainsi que d'autres. Sauf indication contraire, Rust utilise par défaut un `i32`, qui est le type de `secret_number` à moins que vous n'ajoutiez des informations de type ailleurs qui entraîneraient Rust à inférer un autre type numérique. La raison de l'erreur est que Rust ne peut pas comparer une chaîne de caractères et un type numérique.

En fin de compte, nous voulons convertir la `String` que le programme lit en entrée en un vrai type numérique pour pouvoir la comparer numériquement au nombre secret. Nous le faisons en ajoutant cette ligne au corps de la fonction `main` :

Nom de fichier : `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

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
```

Nous créons une variable nommée `guess`. Mais attends, le programme n'a-t-il pas déjà une variable nommée `guess`? Oui, mais heureusement Rust nous permet de masquer la valeur précédente de `guess` avec une nouvelle. Le _masquage_ nous permet de réutiliser le nom de variable `guess` plutôt que de devoir créer deux variables uniques, telles que `guess_str` et `guess`, par exemple. Nous aborderons ceci en détail au Chapitre 3, mais pour l'instant, sachez que cette fonction est souvent utilisée lorsque vous voulez convertir une valeur d'un type à un autre type.

Nous liisons cette nouvelle variable à l'expression `guess.trim().parse()`. Le `guess` dans l'expression fait référence à la variable `guess` d'origine qui contenait l'entrée sous forme de chaîne de caractères. La méthode `trim` sur une instance de `String` éliminera tout espace blanc au début et à la fin, ce que nous devons faire pour pouvoir comparer la chaîne avec le `u32`, qui ne peut contenir que des données numériques. L'utilisateur doit appuyer sur Entrée pour satisfaire `read_line` et entrer sa proposition, ce qui ajoute un caractère de nouvelle ligne à la chaîne. Par exemple, si l'utilisateur tape `5` et appuie sur Entrée, `guess` ressemble à ceci : `5\n`. Le `\n` représente "retour à la ligne." (Sur Windows, appuyer sur Entrée résulte en un retour chariot et une nouvelle ligne, `\r\n`.) La méthode `trim` élimine `\n` ou `\r\n`, donnant juste `5`.

La méthode `parse` sur les chaînes de caractères convertit une chaîne en un autre type. Ici, nous l'utilisons pour convertir d'une chaîne à un nombre. Nous devons dire à Rust le type numérique exact que nous voulons en utilisant `let guess: u32`. Le deux-points (`:`) après `guess` indique à Rust que nous allons annoter le type de la variable. Rust a plusieurs types numériques intégrés ; le `u32` que l'on voit ici est un entier non signé sur 32 bits. C'est un bon choix par défaut pour un petit nombre positif. Vous apprendrez à propos d'autres types numériques au Chapitre 3.

De plus, l'annotation `u32` dans ce programme d'exemple et la comparaison avec `secret_number` signifient que Rust devra également inférer que `secret_number` devrait être un `u32`. Maintenant, la comparaison sera entre deux valeurs du même type!

La méthode `parse` ne fonctionnera que sur des caractères qui peuvent logiquement être convertis en nombres et peut donc facilement entraîner des erreurs. Par exemple, si la chaîne contenait `A`👍`%`, il n'y aurait aucun moyen de la convertir en nombre. Comme cela peut échouer, la méthode `parse` renvoie un type `Result`, tout comme la méthode `read_line` (discutée précédemment dans "Gérer les échecs potentiels avec Result"). Nous traiterons ce `Result` de la même manière en utilisant à nouveau la méthode `expect`. Si `parse` renvoie une variante `Err` de `Result` parce qu'elle n'a pas pu créer un nombre à partir de la chaîne, l'appel à `expect` fera planter le jeu et affichera le message que nous lui donnons. Si `parse` peut convertir avec succès la chaîne en nombre, elle renverra la variante `Ok` de `Result`, et `expect` renverra le nombre que nous voulons à partir de la valeur `Ok`.

Exécutons le programme maintenant :

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

Très bien! Même si des espaces ont été ajoutés avant la proposition, le programme a quand même compris que l'utilisateur avait deviné 76. Exécutez le programme plusieurs fois pour vérifier le comportement différent avec différents types d'entrée : devinez le nombre correctement, devinez un nombre trop élevé et devinez un nombre trop bas.

Nous avons maintenant la majeure partie du jeu fonctionnelle, mais l'utilisateur ne peut faire qu'une seule proposition. Modifions cela en ajoutant une boucle!
