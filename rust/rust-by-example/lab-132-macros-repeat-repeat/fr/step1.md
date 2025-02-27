# Répéter

Les macros peuvent utiliser `+` dans la liste d'arguments pour indiquer qu'un argument peut se répéter au moins une fois, ou `*`, pour indiquer que l'argument peut se répéter zéro ou plusieurs fois.

Dans l'exemple suivant, entourer le correspondant avec `$(...),+` correspondra à une ou plusieurs expressions, séparées par des virgules. Notez également que le point-virgule est facultatif dans le dernier cas.

```rust
// `find_min!` calculera le minimum de n'importe quel nombre d'arguments.
macro_rules! find_min {
    // Cas de base :
    ($x:expr) => ($x);
    // `$x` suivi d'au moins un `$y,`
    ($x:expr, $($y:expr),+) => (
        // Appelez `find_min!` sur la queue `$y`
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
