# Einführung

In diesem Lab werden wir auf das Konzept der Bezeichner in Rust-Makros eingewiesen. Bezeichner werden verwendet, um die Argumente eines Makros voranzustellen und sind typannotiert. Einige Beispiele für Bezeichner sind `ident` für Variablennamen/Funktionsnamen, `expr` für Ausdrücke, `block` für Codeblöcke und `pat` für Muster. Diese Bezeichner werden innerhalb von Makrosregeln verwendet, um Code basierend auf den bereitgestellten Argumenten zu generieren.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
