# Crates

Das Attribut `crate_type` kann verwendet werden, um dem Compiler mitzuteilen, ob ein Crate eine Binärdatei oder eine Bibliothek ist (und sogar welchen Typ von Bibliothek), und das Attribut `crate_name` kann verwendet werden, um den Namen des Crates festzulegen.

Es ist jedoch wichtig zu beachten, dass sowohl das Attribut `crate_type` als auch das Attribut `crate_name` **keine** Auswirkungen haben, wenn Cargo, der Rust-Paketmanager, verwendet wird. Da Cargo für die Mehrzahl der Rust-Projekte verwendet wird, bedeutet dies, dass die realen Anwendungen von `crate_type` und `crate_name` relativ begrenzt sind.

```rust
// Dieses Crate ist eine Bibliothek
#![crate_type = "lib"]
// Die Bibliothek heißt "rary"
#![crate_name = "rary"]

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

Wenn das Attribut `crate_type` verwendet wird, müssen wir das Flag `--crate-type` nicht mehr an `rustc` übergeben.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
