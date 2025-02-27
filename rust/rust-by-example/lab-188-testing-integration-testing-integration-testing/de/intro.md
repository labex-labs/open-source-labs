# Einführung

In diesem Lab wird die Integrationstestung diskutiert, bei der mehrere Teile einer Bibliothek zusammen mithilfe ihrer öffentlichen Schnittstelle getestet werden. Integrationstests können im Verzeichnis `tests` neben dem Verzeichnis `src` in einem Rust-Crate platziert werden und mit dem Befehl `cargo test` ausgeführt werden. Darüber hinaus kann gemeinsamer Code zwischen Integrationstests geteilt werden, indem ein Modul mit öffentlichen Funktionen erstellt und innerhalb der Tests importiert wird.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
