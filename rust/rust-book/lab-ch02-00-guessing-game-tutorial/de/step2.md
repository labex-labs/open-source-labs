# Ein neues Projekt einrichten

Um ein neues Projekt einzurichten, gehe in das `project`-Verzeichnis, das du im ersten Kapitel erstellt hast, und erstelle ein neues Projekt mit Cargo wie folgt:

```bash
cargo new guessing_game
cd guessing_game
```

Der erste Befehl, `cargo new`, nimmt den Namen des Projekts (`guessing_game`) als erstes Argument. Der zweite Befehl wechselt in das Verzeichnis des neuen Projekts.

Schau dir die generierte `Cargo.toml`-Datei an:

Dateiname: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# Weitere Schlüssel und ihre Definitionen findest du unter
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Wie du im ersten Kapitel gesehen hast, generiert `cargo new` ein "Hello, world!"-Programm für dich. Schau dir die `src/main.rs`-Datei an:

Dateiname: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Lassen Sie uns dieses "Hello, world!"-Programm jetzt kompilieren und in einem Schritt mit dem Befehl `cargo run` ausführen:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

Der Befehl `run` ist praktisch, wenn Sie schnell iterieren müssen, wie wir es in diesem Spiel tun werden, indem Sie jede Iteration schnell testen, bevor Sie zur nächsten übergehen.

Öffnen Sie die `src/main.rs`-Datei erneut. In dieser Datei werden Sie den gesamten Code schreiben.
