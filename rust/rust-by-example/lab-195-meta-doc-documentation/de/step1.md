# Dokumentation

Verwenden Sie `cargo doc`, um die Dokumentation in `target/doc` zu erstellen.

Verwenden Sie `cargo test`, um alle Tests (einschließlich der Dokumentationstests) auszuführen, und `cargo test --doc`, um nur die Dokumentationstests auszuführen.

Diese Befehle werden entsprechend `rustdoc` (und `rustc`) gemäß den Anforderungen aufrufen.

## Doc-Kommentare

Doc-Kommentare sind sehr nützlich für große Projekte, die eine Dokumentation erfordern. Wenn `rustdoc` ausgeführt wird, sind dies die Kommentare, die in die Dokumentation kompiliert werden. Sie werden durch ein `///` gekennzeichnet und unterstützen \[Markdown\].

````rust
#![crate_name = "doc"]

/// Ein Mensch wird hier dargestellt
pub struct Person {
    /// Ein Mensch muss einen Namen haben, egal wie sehr Juliet es hasst
    name: String,
}

impl Person {
    /// Gibt eine Person mit dem angegebenen Namen zurück
    ///
    /// # Argumente
    ///
    /// * `name` - Ein String-Slice, der den Namen der Person enthält
    ///
    /// # Beispiele
    ///
    /// ```
    /// // Sie können Rust-Code zwischen den Fences innerhalb der Kommentare haben
    /// // Wenn Sie `--test` an `rustdoc` übergeben, wird es ihn sogar für Sie testen!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// Gibt einen freundlichen Gruß!
    ///
    /// Sagt "Hallo, [name](Person::name)" zur `Person`, auf der es aufgerufen wird.
    pub fn hello(& self) {
        println!("Hallo, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

Um die Tests auszuführen, bauen Sie zunächst den Code als Bibliothek und geben Sie `rustdoc` anschließend an, wo es die Bibliothek finden kann, damit es sie in jedes Doctest-Programm verknüpfen kann:

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## Doc-Attribute

Im Folgenden finden Sie einige Beispiele der am häufigsten verwendeten `#[doc]`-Attribute, die mit `rustdoc` verwendet werden.

## `inline`

Wird verwendet, um die Docs inlining zu verwenden, anstatt auf eine separate Seite zu verlinken.

```rust
#[doc(inline)]
pub use bar::Bar;

/// bar docs
mod bar {
    /// die Docs für Bar
    pub struct Bar;
}
```

## `no_inline`

Wird verwendet, um das Verlinken auf eine separate Seite oder überhaupt zu verhindern.

```rust
// Beispiel aus libcore/prelude
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

Wenn Sie dies verwenden, wird `rustdoc` dazu veranlasst, dies nicht in die Dokumentation aufzunehmen:

```rust
// Beispiel aus der futures-rs-Bibliothek
#[doc(hidden)]
pub use self::async_await::*;
```

Für die Dokumentation wird `rustdoc` von der Community weit verbreitet verwendet. Mit ihm werden die [std-Bibliothek-Dokumentationen](https://doc.rust-lang.org/std/) erstellt.
