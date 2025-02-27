# while

Le mot clé `while` peut être utilisé pour exécuter une boucle tant qu'une condition est vraie.

Écrivons le fameux FizzBuzz à l'aide d'une boucle `while`.

```rust
fn main() {
    // Une variable compteur
    let mut n = 1;

    // Boucle tant que `n` est inférieur à 101
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // Incrémenter le compteur
        n += 1;
    }
}
```
