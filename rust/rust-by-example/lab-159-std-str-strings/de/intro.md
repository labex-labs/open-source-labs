# Einführung

In diesem Lab werden wir das Konzept von Strings in Rust erkunden. Rust hat zwei Arten von Strings: `String` und `&str`.

Ein `String` ist ein auf dem Heap zugewiesen, wachsender String, der als gültige UTF-8-Sequenz garantiert ist. Andererseits ist `&str` ein Slice, der auf eine gültige UTF-8-Sequenz zeigt und zum Betrachten eines `Strings` verwendet werden kann.

In Rust können Stringliterale auf verschiedene Weise geschrieben werden, einschließlich der Verwendung von Escape-Sequenzen zur Darstellung von Sonderzeichen. Beispielsweise repräsentiert `\x3F` das Fragezeichen und `\u{211D}` einen Unicode-Codepunkt. Wenn Sie einen String so wie er ist ohne Escape-Sequenzen schreiben möchten, können Sie auch Raw-Stringliterale verwenden.

Wenn Sie mit Byte-Strings arbeiten müssen, bietet Rust Byte-Stringliterale mit dem `b`-Prefix. Byte-Strings können Byte-Escape-Sequenzen haben, aber keine Unicode-Escape-Sequenzen. Raw-Byte-Strings können ebenfalls in ähnlicher Weise wie Raw-Stringliterale verwendet werden.

Es ist wichtig zu beachten, dass `str` und `String` immer gültige UTF-8-Sequenzen sein müssen. Wenn Sie mit Strings in anderen Codierungen arbeiten müssen, können Sie externe Crates wie `encoding` verwenden, um Umwandlungen zwischen Zeichensätzen durchzuführen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
