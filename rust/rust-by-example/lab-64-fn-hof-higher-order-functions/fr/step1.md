# Higher Order Functions

Rust fournit des fonctions de premier ordre (HOF). Ce sont des fonctions qui prennent une ou plusieurs fonctions et/ou produisent une fonction plus utile. Les HOF et les itérateurs paresseux donnent à Rust son goût fonctionnel.

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Trouvez la somme de tous les nombres impairs au carré inférieurs à 1000");
    let upper = 1000;

    // Approche impérative
    // Décarez la variable accumulatrice
    let mut acc = 0;
    // Itérez : 0, 1, 2,... jusqu'à l'infini
    for n in 0.. {
        // Élevez le nombre au carré
        let n_squared = n * n;

        if n_squared >= upper {
            // Sortez de la boucle si vous avez dépassé la limite supérieure
            break;
        } else if is_odd(n_squared) {
            // Accumulez la valeur, si elle est impaire
            acc += n_squared;
        }
    }
    println!("style impératif: {}", acc);

    // Approche fonctionnelle
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // Tous les nombres naturels au carré
            .take_while(|&n_squared| n_squared < upper) // En dessous de la limite supérieure
            .filter(|&n_squared| is_odd(n_squared))     // Qui sont impairs
            .sum();                                     // Sommez-les
    println!("style fonctionnel: {}", sum_of_squared_odd_numbers);
}
```

Option et Iterator implémentent leur part fair de HOF.
