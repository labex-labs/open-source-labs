# Verwenden einer Bibliothek

Um eine Kiste mit dieser neuen Bibliothek zu verknüpfen, können Sie die `--extern`-Flagge von `rustc` verwenden. Alle ihre Elemente werden dann unter einem Modul importiert, das den gleichen Namen wie die Bibliothek hat. Dieses Modul verhält sich im Allgemeinen genauso wie jedes andere Modul.

```rust
// extern crate rary; // Möglicherweise erforderlich für die Rust 2015-Edition oder ältere
fn main() {
    rary::public_function();

    // Fehler! `private_function` ist privat
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# Wenn library.rlib der Pfad zur kompilierten Bibliothek ist, angenommen, dass sie
# im selben Verzeichnis hier ist:
$ rustc executable.rs --extern rary=library.rlib &&./executable
gerufen rary's `public_function()`
gerufen rary's `indirect_access()`, das
> rief rary's `private_function()`
```
