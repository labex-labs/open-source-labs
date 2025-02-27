# Einführung

In diesem Lab lernen wir, dass wenn wir in Rust Funktionen schreiben, die eine Closure als Eingabeparameter akzeptieren, der vollständige Typ der Closure mithilfe eines der `Traits`: `Fn`, `FnMut` oder `FnOnce` annotiert werden muss. Diese Traits bestimmen, wie die Closure den eingefangenen Wert verwendet, entweder per Referenz, mutabler Referenz oder Wert. Der Compiler fängt Variablen in der am wenigsten restriktiven Weise möglich basierend auf dem gewählten Trait für die Closure ein.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
