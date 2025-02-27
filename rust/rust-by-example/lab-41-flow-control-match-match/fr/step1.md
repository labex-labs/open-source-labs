# match

Rust fournit la correspondance de motifs via le mot clé `match`, qui peut être utilisé comme un `switch` en C. Le premier bras correspondant est évalué et toutes les valeurs possibles doivent être couvertes.

```rust
fn main() {
    let number = 13;
    // TODO ^ Essayez différentes valeurs pour `number`

    println!("Dites-moi quelque chose à propos de {}", number);
    match number {
        // Correspondre à une seule valeur
        1 => println!("Un!"),
        // Correspondre à plusieurs valeurs
        2 | 3 | 5 | 7 | 11 => println!("C'est un nombre premier"),
        // TODO ^ Essayez d'ajouter 13 à la liste des nombres premiers
        // Correspondre à une plage inclusive
        13..=19 => println!("Un ado"),
        // Gérer le reste des cas
        _ => println!("Pas spécial"),
        // TODO ^ Essayez de commenter cette instruction de rattrapage
    }

    let boolean = true;
    // Match est également une expression
    let binary = match boolean {
        // Les bras d'un match doivent couvrir toutes les valeurs possibles
        false => 0,
        true => 1,
        // TODO ^ Essayez de commenter l'un de ces bras
    };

    println!("{} -> {}", boolean, binary);
}
```
