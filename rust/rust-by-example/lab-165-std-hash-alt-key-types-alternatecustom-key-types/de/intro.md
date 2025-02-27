# Einführung

In diesem Lab untersuchen wir die Verwendung alternativer/benutzerdefinierter Schlüsseltypen in Rusts `HashMap`, die Typen umfassen können, die die `Eq`- und `Hash`-Traits implementieren, wie `bool`, `int`, `uint`, `String` und `&str`. Darüber hinaus können wir diese Traits für benutzerdefinierte Typen mithilfe des `#[derive(PartialEq, Eq, Hash)]`-Attributs implementieren, was es ihnen ermöglicht, als Schlüssel in einer `HashMap` zu verwendet werden.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
