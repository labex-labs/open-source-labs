# Surcharge

Les macros peuvent être surchargées pour accepter différentes combinaisons d'arguments. A cet égard, `macro_rules!` peut fonctionner de manière similaire à un bloc `match` :

```rust
// `test!` comparera `$left` et `$right`
// de différentes manières selon la façon dont vous l'appelez :
macro_rules! test {
    // Les arguments n'ont pas besoin d'être séparés par une virgule.
    // N'importe quel modèle peut être utilisé!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ chaque branche doit se terminer par un point-virgule.
    ($left:expr; or $right:expr) => {
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    };
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}
```
