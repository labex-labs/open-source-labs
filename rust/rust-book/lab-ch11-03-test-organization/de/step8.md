# Integrations-Tests für binäre Kisten

Wenn unser Projekt eine binäre Kiste ist, die nur eine Datei `src/main.rs` enthält und keine Datei `src/lib.rs` hat, können wir keine Integrations-Tests im `tests`-Verzeichnis erstellen und Funktionen, die in der Datei `src/main.rs` definiert sind, mit einer `use`-Anweisung in den Geltungsbereich bringen. Nur Bibliothekskisten stellen Funktionen zur Verfügung, die andere Kisten verwenden können; binäre Kisten sind dazu gedacht, einzeln ausgeführt zu werden.

Dies ist einer der Gründe, warum Rust-Projekte, die eine Binärdatei liefern, eine einfache `src/main.rs`-Datei haben, die Logik aufruft, die in der Datei `src/lib.rs` enthalten ist. Mit dieser Struktur können Integrations-Tests die Bibliothekskiste mit `use` testen, um die wichtigen Funktionen verfügbar zu machen. Wenn die wichtigen Funktionen funktionieren, wird auch der kleine Code in der Datei `src/main.rs` funktionieren, und dieser kleine Code muss nicht getestet werden.
