# Crates

L'attribut `crate_type` peut être utilisé pour indiquer au compilateur si un crate est un binaire ou une bibliothèque (et même quel type de bibliothèque), et l'attribut `crate_name` peut être utilisé pour définir le nom du crate.

Cependant, il est important de noter que les attributs `crate_type` et `crate_name` n'ont **aucun** effet lorsqu'on utilise Cargo, le gestionnaire de packages Rust. Étant donné que Cargo est utilisé pour la majorité des projets Rust, cela signifie que les utilisations réelles de `crate_type` et `crate_name` sont relativement limitées.

```rust
// Ce crate est une bibliothèque
#![crate_type = "lib"]
// La bibliothèque s'appelle "rary"
#![crate_name = "rary"]

pub fn public_function() {
    println!("appelé `public_function()` de rary");
}

fn private_function() {
    println!("appelé `private_function()` de rary");
}

pub fn indirect_access() {
    print!("appelé `indirect_access()` de rary, qui\n> ");

    private_function();
}
```

Lorsque l'attribut `crate_type` est utilisé, on n'a plus besoin de passer le drapeau `--crate-type` à `rustc`.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
