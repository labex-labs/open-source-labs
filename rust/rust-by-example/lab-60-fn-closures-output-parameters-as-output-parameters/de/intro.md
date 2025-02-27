# Einführung

In diesem Lab lernen wir, dass Closures als Eingabeparameter verwendet werden können und auch als Ausgabeparameter zurückgegeben werden können, indem wir `impl Trait` verwenden und die gültigen Traits (`Fn`, `FnMut`, `FnOnce`) angeben. Das `move`-Schlüsselwort wird verwendet, um anzuzeigen, dass alle Captures per Wert erfolgen, um ungültige Referenzen zu vermeiden.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
