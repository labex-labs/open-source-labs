# Einführung

In diesem Lab wird das Konzept der Entwicklungsabhängigkeiten erklärt. Entwicklungsabhängigkeiten werden im Abschnitt `[dev-dependencies]` der Datei `Cargo.toml` hinzugefügt und werden für Tests, Beispiele oder Benchmarks verwendet. Ein Beispiel für eine Entwicklungsabhängigkeit ist `pretty_assertions`, das standardmäßige Makros wie `assert_eq!` und `assert_ne!` erweitert, um farbige Differenzen bereitzustellen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
