# Schreiben und Ausführen eines Rust-Programms

Als nächstes erstelle eine neue Quelldatei und nenne sie `main.rs`. Rust-Dateien enden immer mit der Erweiterung `.rs`. Wenn du in deinem Dateinamen mehr als ein Wort verwendest, ist die Konvention, sie mit einem Unterstrich zu trennen. Beispielsweise verwenden Sie `hello_world.rs` anstelle von `helloworld.rs`.

Öffne nun die gerade erstellte `main.rs`-Datei und gib den Code in Listing 1-1 ein.

Dateiname: `main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Listing 1-1: Ein Programm, das `Hello, world!` ausgibt

Speichere die Datei und kehre zum Terminalfenster im Verzeichnis `~/project/hello_world` zurück. Auf Linux oder macOS gib die folgenden Befehle ein, um die Datei zu kompilieren und auszuführen:

```bash
$ rustc main.rs
$./main
Hello, world!
```

Unabhängig von deinem Betriebssystem sollte die Zeichenfolge `Hello, world!` auf dem Terminal ausgegeben werden. Wenn du diese Ausgabe nicht siehst, wende dich an "Problembehandlung", um Hilfe zu erhalten.

Wenn `Hello, world!` tatsächlich ausgegeben wurde, herzlichen Glückwunsch! Du hast offiziell ein Rust-Programm geschrieben. Damit bist du ein Rust-Programmierer geworden - herzlich willkommen!
