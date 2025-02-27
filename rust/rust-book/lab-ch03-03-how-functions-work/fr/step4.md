# Fonctions avec valeurs de retour

Les fonctions peuvent renvoyer des valeurs au code qui les appelle. Nous ne nommons pas les valeurs de retour, mais nous devons déclarer leur type après une flèche (`->`). En Rust, la valeur de retour d'une fonction est synonyme de la valeur de la dernière expression dans le bloc du corps d'une fonction. Vous pouvez retourner rapidement d'une fonction en utilisant le mot clé `return` et en spécifiant une valeur, mais la plupart des fonctions renvoient implicitement la dernière expression. Voici un exemple d'une fonction qui renvoie une valeur :

Nom de fichier : `src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

Il n'y a pas d'appels de fonction, de macros ou même d'instructions `let` dans la fonction `five` - juste le nombre `5` tout seul. C'est une fonction parfaitement valide en Rust. Notez que le type de retour de la fonction est également spécifié, comme `-> i32`. Essayez d'exécuter ce code ; la sortie devrait ressembler à ceci :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

Le `5` dans `five` est la valeur de retour de la fonction, c'est pourquoi le type de retour est `i32`. Examnons cela plus en détail. Il y a deux points importants : tout d'abord, la ligne `let x = five();` montre que nous utilisons la valeur de retour d'une fonction pour initialiser une variable. Comme la fonction `five` renvoie un `5`, cette ligne est la même que la suivante :

```rust
let x = 5;
```

Deuxièmement, la fonction `five` n'a pas de paramètres et définit le type de la valeur de retour, mais le corps de la fonction est un seul `5` sans point-virgule car c'est une expression dont nous voulons renvoyer la valeur.

Examnons un autre exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

Exécuter ce code imprimera `The value of x is: 6`. Mais si nous plaçons un point-virgule à la fin de la ligne contenant `x + 1`, en la changeant d'une expression en une instruction, nous obtiendrons une erreur :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

La compilation de ce code produit une erreur, comme suit :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

Le principal message d'erreur, `mismatched types`, révèle le problème central de ce code. La définition de la fonction `plus_one` indique qu'elle renverra un `i32`, mais les instructions ne s'évaluent pas à une valeur, ce qui est exprimé par `()`, le type unité. Par conséquent, rien n'est renvoyé, ce qui contredit la définition de la fonction et entraîne une erreur. Dans cette sortie, Rust fournit un message pour peut-être aider à corriger ce problème : il suggère de supprimer le point-virgule, ce qui corrigerait l'erreur.
