# Hiérarchie de fichiers

Les modules peuvent être mappés à une hiérarchie de fichiers/répertoires. Analysons l'exemple de visibilité dans les fichiers :

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

Dans `split.rs` :

```rust
// Cette déclaration cherchera un fichier nommé `my.rs` et insérera
// son contenu dans un module nommé `my` dans ce contexte
mod my;

fn function() {
    println!("appelé `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

Dans `my.rs` :

```rust
// De même, `mod inaccessible` et `mod nested` trouveront les fichiers
// `nested.rs` et `inaccessible.rs` et les inséreront ici dans leurs
// modules respectifs
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("appelé `my::function()`");
}

fn private_function() {
    println!("appelé `my::private_function()`");
}

pub fn indirect_access() {
    print!("appelé `my::indirect_access()`, qui\n> ");

    private_function();
}
```

Dans `my/nested.rs` :

```rust
pub fn function() {
    println!("appelé `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("appelé `my::nested::private_function()`");
}
```

Dans `my/inaccessible.rs` :

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("appelé `my::inaccessible::public_function()`");
}
```

Vérifions que tout fonctionne toujours comme avant :

```shell
$ rustc split.rs &&./split
appelé `my::function()`
appelé `function()`
appelé `my::indirect_access()`, qui
> appelé `my::private_function()`
appelé `my::nested::function()`
```
