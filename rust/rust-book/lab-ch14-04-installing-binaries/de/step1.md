# Binäre Pakete mit cargo install installieren

Der Befehl `cargo install` ermöglicht es Ihnen, binäre Crates lokal zu installieren und zu verwenden. Dies ist nicht gedacht, um Systempakete zu ersetzen; es soll eine bequeme Möglichkeit für Rust-Entwickler sein, Tools zu installieren, die andere auf *https://crates.io* geteilt haben. Beachten Sie, dass Sie nur Pakete installieren können, die binäre Ziele haben. Ein _binäres Ziel_ ist das ausführbare Programm, das erstellt wird, wenn das Crate eine `src/main.rs`-Datei oder eine andere als binär angegebene Datei hat, im Gegensatz zu einem Bibliotheksziel, das nicht eigenständig ausgeführt werden kann, aber für die Einbindung in andere Programme geeignet ist. Normalerweise enthalten Crates in der _README_-Datei Informationen darüber, ob ein Crate eine Bibliothek ist, ein binäres Ziel hat oder beides.

Alle mit `cargo install` installierten Binärdateien werden im `bin`-Ordner des Installationsroots gespeichert. Wenn Sie Rust mit `rustup.rs` installiert haben und keine benutzerdefinierten Konfigurationen haben, wird dieser Ordner `$HOME/.cargo/bin` sein. Stellen Sie sicher, dass dieser Ordner in Ihrem `$PATH` ist, um die Programme auszuführen, die Sie mit `cargo install` installiert haben.

Zum Beispiel haben wir im Kapitel 12 erwähnt, dass es eine Rust-Implementierung des `grep`-Tools namens `ripgrep` für die Suche in Dateien gibt. Um `ripgrep` zu installieren, können wir Folgendes ausführen:

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

Die vorletzte Zeile der Ausgabe zeigt den Speicherort und den Namen der installierten Binärdatei, was im Falle von `ripgrep` `rg` ist. Solange das Installationsverzeichnis in Ihrem `$PATH` ist, wie zuvor erwähnt, können Sie dann `rg --help` ausführen und ein schnelleres, rustigeres Tool für die Suche in Dateien verwenden!
