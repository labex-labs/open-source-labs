# Einführung

In diesem Lab lernen wir über die Begrenzungen in Rust, die verwendet werden, um die Lebensdauern oder Traits von generischen Typen einzuschränken. Das Zeichen `:` wird verwendet, um anzuzeigen, dass alle Referenzen in einem Typ eine bestimmte Lebensdauer überdauern müssen, während `+` verwendet wird, um anzuzeigen, dass ein Typ ein bestimmtes Trait implementieren muss und alle darin enthaltenen Referenzen eine bestimmte Lebensdauer überdauern müssen. Ein Beispielcodeausschnitt zeigt die Syntax und Verwendung von Begrenzungen in Rust.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
