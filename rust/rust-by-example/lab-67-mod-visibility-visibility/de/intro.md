# Einführung

In diesem Lab lernen wir über die Sichtbarkeit von Elementen in Rust-Modulen, einschließlich der standardmäßigen privaten Sichtbarkeit, der Verwendung des `pub`-Modifizierers, um die Sichtbarkeit zu überschreiben, und der verschiedenen Sichtbarkeitsstufen wie `pub(in path)`, `pub(self)`, `pub(super)` und `pub(crate)`. Wir untersuchen auch geschachtelte Module und die Einschränkungen bei der Zugriffnahme auf private Elemente innerhalb von Modulen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
