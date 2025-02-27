# Einführung

In diesem Lab untersuchen wir die Verwendung des `if let`-Konstrukts in Rust, das für einen saubereren Code sorgt, wenn Enums abgeglichen werden, und die Möglichkeit bietet, Fehlermöglichkeiten anzugeben. Wir demonstrieren auch, wie `if let` verwendet werden kann, um jeden Enum-Wert abzugleichen, einschließlich nicht parametrisierter Varianten. Darüber hinaus geben wir ein Beispiel dafür, wie Code repariert werden kann, der versucht, zwei Enum-Werte miteinander zu vergleichen, indem stattdessen `if let` verwendet wird.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
