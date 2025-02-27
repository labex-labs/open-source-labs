# Zum Release bauen

Wenn Ihr Projekt schließlich für die Veröffentlichung bereit ist, können Sie `cargo build --release` verwenden, um es mit Optimierungen zu kompilieren.

```bash
cargo build --release
```

Dieser Befehl erstellt eine ausführbare Datei in `target/release` statt in `target/debug`. Die Optimierungen machen Ihren Rust-Code schneller laufen, aber das Aktivieren der Optimierungen verlängert die Zeit, die es dauert, Ihr Programm zu kompilieren. Deshalb gibt es zwei verschiedene Profile: eines für die Entwicklung, wenn Sie schnell und oft neu bauen möchten, und eines für das Erstellen des endgültigen Programms, das Sie einem Benutzer geben werden, das nicht wiederholt neu gebaut werden wird und das so schnell wie möglich laufen wird. Wenn Sie die Laufzeit Ihres Codes benchmarken, stellen Sie sicher, dass Sie `cargo build --release` ausführen und mit der ausführbaren Datei in `target/release` benchmarken.
