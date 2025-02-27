# Einführung

In diesem Lab lernen wir, dass eine `where`-Klausel in Rust verwendet werden kann, um die Grenzen für generische Typen getrennt von ihrer Deklaration auszudrücken, was zu einer klareren Syntax führt, und dass es auch möglich ist, Grenzen auf beliebige Typen anzuwenden, nicht nur auf Typparameter. Die `where`-Klausel ist besonders nützlich, wenn die Grenzen ausdrucksstärker sind als die normale Syntax, wie im Beispiel mit dem `PrintInOption`-Trait gezeigt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
