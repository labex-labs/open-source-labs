# Einführung

In diesem Lab können Sie `cargo doc` verwenden, um die Dokumentation in `target/doc` zu erstellen. Sie können auch `cargo test` verwenden, um alle Tests, einschließlich der Dokumentationstests, auszuführen, und `cargo test --doc`, um nur die Dokumentationstests auszuführen. Doc-Kommentare, gekennzeichnet durch `///`, werden von `rustdoc` in die Dokumentation kompiliert und unterstützen Markdown. Diese Kommentare sind nützlich, um den Code in großen Projekten zu dokumentieren. Doc-Attribute wie `inline`, `no_inline` und `hidden` werden häufig mit `rustdoc` verwendet. Rustdoc wird von der Community weit verbreitet zur Generierung von Dokumentation verwendet, einschließlich der Standardbibliothek-Dokumentationen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
