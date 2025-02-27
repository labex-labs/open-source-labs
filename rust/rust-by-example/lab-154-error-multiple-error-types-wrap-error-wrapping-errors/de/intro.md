# Einführung

In diesem Lab wird der alternative Ansatz demonstriert, Fehler in einem benutzerdefinierten Fehlertyp zu verpacken. Das Codebeispiel zeigt, wie man einen `Result`-Typalias definiert, der die `DoubleError`-Enumeration als Fehlervariante verwendet, die die `ParseIntError` der Standardbibliothek umschließt. Indem man die `fmt::Display`, `error::Error` und `From`-Traits implementiert, kann der benutzerdefinierte Fehlertyp zusätzliche Informationen bereitstellen und zugrunde liegende Fehler behandeln.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
