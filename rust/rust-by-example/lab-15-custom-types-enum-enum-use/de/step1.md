# use

Die `use`-Anweisung kann verwendet werden, um die manuellen Namensräume zu vermeiden:

```rust
// Ein Attribut, um Warnungen für nicht genutzten Code zu unterdrücken.
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
    // Explicit `use` jedes Namens, damit sie ohne manuellen Namensraum verfügbar sind.
    use crate::Status::{Poor, Rich};
    // Automatisch `use` jedes Namens innerhalb von `Work`.
    use crate::Work::*;

    // Entspricht `Status::Poor`.
    let status = Poor;
    // Entspricht `Work::Civilian`.
    let work = Civilian;

    match status {
        // Beachten Sie die fehlende Namensraumangabe aufgrund der expliziten `use` oben.
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        // Beachten Sie erneut die fehlende Namensraumangabe.
        Civilian => println!("Civilians work!"),
        Soldier  => println!("Soldiers fight!"),
    }
}
```
