# Création d'une bibliothèque

Créons une bibliothèque, puis voyons comment la lier à une autre boîte crânienne (crate).

Dans `rary.rs` :

```rust
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

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

Les bibliothèques sont préfixées avec "lib", et par défaut elles prennent le nom de leur fichier de boîte crânienne, mais ce nom par défaut peut être remplacé en passant l'option `--crate-name` à `rustc` ou en utilisant l'[`attribut crate_name`][crate-name].
