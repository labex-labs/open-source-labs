# Einführung

In diesem Lab lernen wir über divergierende Funktionen, die in Rust mit `!` markiert werden. Divergierende Funktionen geben niemals zurück, und ihr Rückgabetyp ist ein leerer Typ. Dies unterscheidet sich vom `()`-Typ, der nur einen möglichen Wert hat. Divergierende Funktionen können nützlich sein, wenn eine Umwandlung in einen anderen Typ erforderlich ist, wie in `match`-Zweigen. Sie sind auch der Rückgabetyp von Funktionen, die für immer in einer Schleife verbleiben oder den Prozess beenden.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
