# Einführung

In diesem Lab untersuchen wir das Konzept von Phantom-Typ-Parametern, die Typ-Parameter sind, die statisch zur Compile-Zeit überprüft werden und keine Laufzeit-Behavior oder -Werte haben. Wir demonstrieren ihre Verwendung in Rust, indem wir `std::marker::PhantomData` mit dem Konzept von Phantom-Typ-Parametern kombinieren, um Tupel und Structs zu erstellen, die verschiedene Datentypen enthalten.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
