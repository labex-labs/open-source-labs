# Einführung

In diesem Lab untersuchen wir das Konzept von Domain Specific Languages (DSLs) in Rust, die als kleine "Sprachen" in Rust-Makros eingebettet sind. Diese Makros erweitern sich zu normalen Rust-Konstrukten, bieten jedoch eine präzise und intuitive Syntax für spezifische Funktionen. Ein praktisches Beispiel wird anhand einer Taschenrechner-API demonstriert, bei der ein Ausdruck an das Makro übergeben wird und das Ergebnis auf der Konsole ausgegeben wird. Dies ermöglicht die Erstellung von komplexeren Schnittstellen wie denen in Bibliotheken wie `lazy_static` oder `clap`.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
