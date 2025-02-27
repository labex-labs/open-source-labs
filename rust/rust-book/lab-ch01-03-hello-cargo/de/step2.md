# Ein Projekt mit Cargo erstellen

Lassen Sie uns ein neues Projekt mit Cargo erstellen und sehen, wie es sich von unserem ursprünglichen "Hello, world!"-Projekt unterscheidet. Navigieren Sie zurück in Ihr `project`-Verzeichnis (oder in das Verzeichnis, in dem Sie Ihre Code-Dateien gespeichert haben). Anschließend führen Sie auf jedem Betriebssystem Folgendes aus:

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

Der erste Befehl erstellt ein neues Verzeichnis und Projekt namens _hello_cargo_. Wir haben unseren Projektnamen _hello_cargo_ gewählt, und Cargo erstellt seine Dateien in einem Verzeichnis mit demselben Namen.

Gehen Sie in das Verzeichnis `hello_cargo` und listen Sie die Dateien auf. Sie werden sehen, dass Cargo zwei Dateien und ein Verzeichnis für uns erstellt hat: eine Datei namens `Cargo.toml` und ein Verzeichnis `src` mit einer Datei `main.rs` darin.

Es hat auch ein neues Git-Repository zusammen mit einer _.gitignore_-Datei initialisiert. Wenn Sie `cargo new` innerhalb eines bestehenden Git-Repositorys ausführen, werden keine Git-Dateien erstellt; Sie können dieses Verhalten überschreiben, indem Sie `cargo new --vcs=git` verwenden.

> Hinweis: Git ist ein übliches Versionskontrollsystem. Sie können `cargo new` ändern, um ein anderes Versionskontrollsystem oder kein Versionskontrollsystem zu verwenden, indem Sie das Flag `--vcs` verwenden. Führen Sie `cargo new --help` aus, um die verfügbaren Optionen anzuzeigen.

Öffnen Sie `Cargo.toml` in Ihrem bevorzugten Texteditor. Es sollte ähnlich wie der Code in Listing 1-2 aussehen.

Dateiname: `Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

Listing 1-2: Inhalt von `Cargo.toml`, der von `cargo new` generiert wurde

Diese Datei ist im _TOML_ (_Tom's Obvious, Minimal Language_)-Format, das das Konfigurationsformat von Cargo ist.

Die erste Zeile, `[package]`, ist ein Abschnittstitel, der angibt, dass die folgenden Angaben eine Paketkonfiguration sind. Wenn wir mehr Informationen zu dieser Datei hinzufügen, werden wir weitere Abschnitte hinzufügen.

Die nächsten drei Zeilen legen die Konfigurationsinformationen fest, die Cargo benötigt, um Ihr Programm zu kompilieren: den Namen, die Version und die Rust-Edition, die verwendet werden soll. Wir werden im Anhang E über den Schlüssel `edition` sprechen.

Die letzte Zeile, `[dependencies]`, ist der Beginn eines Abschnitts, in dem Sie alle Abhängigkeiten Ihres Projekts auflisten können. In Rust werden Code-Pakete als _Crates_ bezeichnet. Für dieses Projekt werden wir keine weiteren Crates benötigen, aber wir werden dies im ersten Projekt im Kapitel 2, daher werden wir diesen Abhängigkeitsabschnitt dann verwenden.

Öffnen Sie nun `src/main.rs` und schauen Sie sich an:

Dateiname: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo hat Ihnen ein "Hello, world!"-Programm generiert, genau wie das, das wir in Listing 1-1 geschrieben haben! Bisher unterscheiden sich unsere Projekt und das von Cargo generierte Projekt darin, dass Cargo den Code im `src`-Verzeichnis platziert hat und wir eine `Cargo.toml`-Konfigurationsdatei im obersten Verzeichnis haben.

Cargo erwartet, dass Ihre Quellcode-Dateien im `src`-Verzeichnis gespeichert sind. Das oberste Projektverzeichnis ist nur für README-Dateien, Lizenzhinweise, Konfigurationsdateien und alles andere, das nicht mit Ihrem Code zusammenhängt. Die Verwendung von Cargo hilft Ihnen, Ihre Projekte zu organisieren. Es gibt einen Platz für alles, und alles ist an seinem Platz.

Wenn Sie ein Projekt gestartet haben, das nicht Cargo verwendet, wie wir es mit dem "Hello, world!"-Projekt getan haben, können Sie es in ein Projekt umwandeln, das Cargo verwendet. Verschieben Sie den Projektcode in das `src`-Verzeichnis und erstellen Sie eine passende `Cargo.toml`-Datei.
