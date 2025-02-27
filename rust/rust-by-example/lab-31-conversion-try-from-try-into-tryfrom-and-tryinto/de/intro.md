# Einführung

In diesem Lab untersuchen wir die Verwendung von `TryFrom` und `TryInto` in Rust, die generische Traits sind, die für fehlerbehaftete Konvertierungen zwischen Typen verwendet werden und `Result`-Typen zurückgeben. Wir stellen einen Beispiel-Codeschnipsel bereit, der die Implementierung von `TryFrom` zur Konvertierung einer `i32` in eine benutzerdefinierte `EvenNumber`-Struktur demonstriert, und zeigen dann, wie `TryFrom` und `TryInto` verwendet werden, um die Konvertierung durchzuführen und die möglichen Fehler zu behandeln.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
