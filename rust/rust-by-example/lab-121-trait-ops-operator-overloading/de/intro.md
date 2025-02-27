# Einführung

In diesem Lab untersuchen wir die Überladung von Operatoren in Rust und wie dies durch Traits erreicht werden kann. Operatoren in Rust können mithilfe von Traits überladen werden, was es ihnen ermöglicht, unterschiedliche Aufgaben basierend auf ihren Eingabeargumenten auszuführen. Der `+`-Operator ist beispielsweise syntaktischer Zucker für die `add`-Methode und kann von jedem Implementierer des `Add`-Traits verwendet werden. Die Traits, die Operatoren überladen, einschließlich `Add`, können in `core::ops` gefunden werden. Der bereitgestellte Rust-Code zeigt, wie der `+`-Operator für benutzerdefinierte Typen `Foo` und `Bar` überladen wird, was jeweils zu unterschiedlichen Ausgabetypen `FooBar` und `BarFoo` führt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
