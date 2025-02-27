# use

La declaración `use` se puede utilizar para que no sea necesario un alcance manual:

```rust
// Un atributo para ocultar advertencias de código no utilizado.
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
    // Explicitamente `use` cada nombre para que estén disponibles sin
    // alcance manual.
    use crate::Status::{Poor, Rich};
    // Automáticamente `use` cada nombre dentro de `Work`.
    use crate::Work::*;

    // Equivalente a `Status::Poor`.
    let status = Poor;
    // Equivalente a `Work::Civilian`.
    let work = Civilian;

    match status {
        // Observe la falta de alcance debido al `use` explícito anterior.
        Rich => println!("Los ricos tienen mucho dinero!"),
        Poor => println!("Los pobres no tienen dinero..."),
    }

    match work {
        // Observe nuevamente la falta de alcance.
        Civilian => println!("Los civiles trabajan!"),
        Soldier  => println!("Los soldados pelean!"),
    }
}
```
