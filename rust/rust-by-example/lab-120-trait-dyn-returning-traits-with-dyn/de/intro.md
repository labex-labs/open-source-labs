# Einführung

In diesem Lab lernen wir, wie wir die Beschränkung umgehen, direkt Traits in Rust zurückzugeben, indem wir den Typ `Box<dyn Animal>` verwenden, der es Funktionen ermöglicht, einen Verweis auf ein auf dem Heap zugewiesenes Objekt zurückzugeben, das das `Animal`-Trait implementiert.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
