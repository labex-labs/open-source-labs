# use

La déclaration `use` peut être utilisée pour ne pas avoir besoin de la portée manuelle :

```rust
// Un attribut pour masquer les avertissements pour le code inutilisé.
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // Utilisez explicitement chaque nom pour qu'ils soient disponibles sans
    // la portée manuelle.
    use crate::Status::{Poor, Rich};
    // Utilisez automatiquement chaque nom à l'intérieur de `Work`.
    use crate::Work::*;

    // Équivalent à `Status::Poor`.
    let status = Poor;
    // Équivalent à `Work::Civilian`.
    let work = Civilian;

    match status {
        // Notez l'absence de portée en raison de l'utilisation explicite ci-dessus.
        Rich => println!("Les riches ont beaucoup d'argent!"),
        Poor => println!("Les pauvres n'ont pas d'argent..."),
    }

    match work {
        // Notez encore une fois l'absence de portée.
        Civilian => println!("Les civils travaillent!"),
        Soldier  => println!("Les soldats combattent!"),
    }
}
```
