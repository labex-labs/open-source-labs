# Einführung

In diesem Lab untersuchen wir die Verwendung des `?`-Operators in Rust, mit dem man `Option`-Werte einfach entpacken kann, ohne dass geschachtelte `match`-Anweisungen erforderlich sind. Der `?`-Operator kann verwendet werden, um den zugrunde liegenden Wert schnell zurückzugeben, wenn die `Option` `Some` ist, oder die Funktion zu beenden und `None` zurückzugeben, wenn die `Option` `None` ist. Dieser Operator kann verkettet werden, um den Code lesbarer und präziser zu machen.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
