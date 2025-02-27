# Fonctions

Les fonctions sont déclarées à l'aide du mot clé `fn`. Ses arguments sont annotés avec leur type, tout comme les variables, et, si la fonction renvoie une valeur, le type de retour doit être spécifié après une flèche `->`.

La dernière expression dans la fonction sera utilisée comme valeur de retour. Alternativement, l'instruction `return` peut être utilisée pour renvoyer une valeur plus tôt à l'intérieur de la fonction, même à l'intérieur de boucles ou d'instructions `if`.

Réécrivons FizzBuzz à l'aide de fonctions!

```rust
// Contrairement à C/C++, il n'y a pas de restriction sur l'ordre des définitions de fonctions
fn main() {
    // Nous pouvons utiliser cette fonction ici, et la définir plus tard quelque part
    fizzbuzz_to(100);
}

// Fonction qui renvoie une valeur booléenne
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // Cas limité, retour anticipé
    if rhs == 0 {
        return false;
    }

    // Ceci est une expression, le mot clé `return` n'est pas nécessaire ici
    lhs % rhs == 0
}

// Fonctions qui "ne" renvoient pas de valeur, renvoient en fait le type unité `()`
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// Lorsqu'une fonction renvoie `()`, le type de retour peut être omis de la
// signature
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
