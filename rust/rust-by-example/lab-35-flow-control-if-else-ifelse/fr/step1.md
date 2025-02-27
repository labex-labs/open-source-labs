# if/else

La structure conditionnelle avec `if`-`else` est similaire à celle des autres langages. Contrairement à beaucoup d'entre eux, la condition booléenne n'a pas besoin d'être entourée de parenthèses, et chaque condition est suivie d'un bloc. Les conditionnels `if`-`else` sont des expressions, et toutes les branches doivent renvoyer le même type.

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} est négatif", n);
    } else if n > 0 {
        print!("{} est positif", n);
    } else {
        print!("{} est égal à zéro", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", et est un nombre petit, multipliez-le par dix");

            // Cette expression renvoie un `i32`.
            10 * n
        } else {
            println!(", et est un grand nombre, divisez-le par deux");

            // Cette expression doit également renvoyer un `i32`.
            n / 2
            // TODO ^ Essayez de supprimer cette expression en y ajoutant un point-virgule.
        };
    //   ^ N'oubliez pas d'y mettre un point-virgule ici! Toutes les liaisons `let` en ont besoin.

    println!("{} -> {}", n, big_n);
}
```
