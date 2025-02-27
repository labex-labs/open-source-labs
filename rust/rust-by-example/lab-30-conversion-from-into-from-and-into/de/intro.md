# Einführung

In diesem Lab untersuchen wir die Konzepte der `From`- und `Into`-Traits in Rust, die zum Konvertieren zwischen verschiedenen Typen verwendet werden. Diese Traits sind von Natur aus miteinander verknüpft, wobei `Into` das Gegenteil von `From` ist. Der `From`-Trait ermöglicht es einem Typ, festzulegen, wie er sich selbst aus einem anderen Typ erstellt, was die einfache Umwandlung zwischen Typen ermöglicht. Der `Into`-Trait ruft die `From`-Implementierung automatisch auf, wenn dies erforderlich ist. Beide Traits können für benutzerdefinierte Typen implementiert werden, was Flexibilität bei der Typumwandlung bietet.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
