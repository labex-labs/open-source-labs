# Dateihierarchie

Module können in eine Datei-/Verzeichnis-Hierarchie abgebildet werden. Betrachten wir das Beispiel zur Sichtbarkeit in Dateien:

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

In `split.rs`:

```rust
// Diese Deklaration sucht nach einer Datei namens `my.rs` und
// fügt deren Inhalt in ein Modul namens `my` innerhalb dieses Bereichs ein
mod my;

fn function() {
    println!("aufgerufen `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

In `my.rs`:

```rust
// Ähnlich werden `mod inaccessible` und `mod nested` die Dateien `nested.rs`
// und `inaccessible.rs` finden und hier unter ihren jeweiligen Modulen einfügen
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("aufgerufen `my::function()`");
}

fn private_function() {
    println!("aufgerufen `my::private_function()`");
}

pub fn indirect_access() {
    print!("aufgerufen `my::indirect_access()`, das\n> ");

    private_function();
}
```

In `my/nested.rs`:

```rust
pub fn function() {
    println!("aufgerufen `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("aufgerufen `my::nested::private_function()`");
}
```

In `my/inaccessible.rs`:

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("aufgerufen `my::inaccessible::public_function()`");
}
```

Überprüfen wir, ob alles weiterhin wie zuvor funktioniert:

```shell
$ rustc split.rs &&./split
aufgerufen `my::function()`
aufgerufen `function()`
aufgerufen `my::indirect_access()`, das
> aufgerufen `my::private_function()`
aufgerufen `my::nested::function()`
```
