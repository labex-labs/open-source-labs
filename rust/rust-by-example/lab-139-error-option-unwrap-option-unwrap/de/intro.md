# Einführung

In diesem Lab lernen wir über die `Option`-Enumeration in der `std`-Bibliothek von Rust, die verwendet wird, um Fälle zu behandeln, in denen das Fehlen möglich ist. Sie bietet zwei Optionen: `Some(T)` für den Fall, dass ein Element vom Typ `T` gefunden wird, und `None` für den Fall, dass kein Element gefunden wird. Diese Fälle können explizit mit `match` behandelt oder implizit mit `unwrap` behandelt werden. Die explizite Behandlung ermöglicht eine größere Kontrolle und sinnvolle Ausgabe, während `unwrap` entweder das innere Element zurückgeben oder einen Fehler auslösen kann.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
