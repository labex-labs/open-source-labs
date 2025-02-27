# Das zweite Paket im Arbeitsbereich erstellen

Als nächstes erstellen wir in dem Arbeitsbereich ein weiteres Mitgliedspaket und nennen es `add_one`. Ändern Sie die oberste Ebene `Cargo.toml`, um den Pfad _add_one_ in der `members`-Liste anzugeben:

Dateiname: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

Dann erzeugen Sie einen neuen Bibliothekskraten namens `add_one`:

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

Ihr `add`-Verzeichnis sollte jetzt diese Verzeichnisse und Dateien haben:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

In der Datei `add_one/src/lib.rs` fügen wir eine `add_one`-Funktion hinzu:

Dateiname: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Jetzt können wir das `adder`-Paket mit unserer Binärdatei von dem `add_one`-Paket abhängig machen, das unsere Bibliothek enthält. Zunächst müssen wir eine Pfadabhängigkeit von `add_one` zu _adder/Cargo.toml_ hinzufügen:

Dateiname: `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo nimmt nicht an, dass die Kraten in einem Arbeitsbereich voneinander abhängen werden, daher müssen wir die Abhängigkeitsbeziehungen explizit angeben.

Als nächstes verwenden wir die `add_one`-Funktion (aus dem `add_one`-Kraten) im `adder`-Kraten. Öffnen Sie die Datei `adder/src/main.rs` und fügen Sie oben eine `use`-Zeile hinzu, um den neuen `add_one`-Bibliothekskraten in den Geltungsbereich zu bringen. Ändern Sie dann die `main`-Funktion, um die `add_one`-Funktion aufzurufen, wie in Listing 14-7.

Dateiname: `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Listing 14-7: Verwenden des `add_one`-Bibliothekskratens aus dem `adder`-Kraten

Lassen Sie uns den Arbeitsbereich erstellen, indem wir `cargo build` im obersten Ebene _add_-Verzeichnis ausführen!

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

Um das Binärpaket aus dem `add`-Verzeichnis auszuführen, können wir angeben, welches Paket im Arbeitsbereich wir ausführen möchten, indem wir das `-p`-Argument und den Paketnamen mit `cargo run` verwenden:

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

Dies führt den Code in `adder/src/main.rs` aus, der von dem `add_one`-Kraten abhängt.
