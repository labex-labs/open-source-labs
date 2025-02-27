# Bibliothek erstellen

Lassen Sie uns eine Bibliothek erstellen und dann sehen, wie Sie sie an einen anderen Crate verknüpfen.

In `rary.rs`:

```rust
pub fn public_function() {
    println!("aufgerufen rary's `public_function()`");
}

fn private_function() {
    println!("aufgerufen rary's `private_function()`");
}

pub fn indirect_access() {
    print!("aufgerufen rary's `indirect_access()`, das\n> ");

    private_function();
}
```

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

Bibliotheken werden mit "lib" als Präfix versehen, und standardmäßig werden sie nach ihrer Crate-Datei benannt, aber dieser Standardname kann durch Angabe der Option `--crate-name` an `rustc` oder durch Verwendung des \[`crate_name`-Attributs\]\[crate-name\] überschrieben werden.
