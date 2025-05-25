# Einführung

In diesem Lab werden wir Arrays und Slices in Rust erkunden. Ein Array ist eine Sammlung von Objekten vom gleichen Typ, die in zusammenhängender Speicherstelle gespeichert sind, und seine Länge ist zur Compile-Zeit bekannt. Ein Slice hingegen ähnelt sich einem Array，但其 Länge ist zur Compile-Zeit nicht bekannt. Slices können verwendet werden, um einen Abschnitt eines Arrays zu entleihen. Wir werden auch behandeln, wie Arrays erstellt werden, Elemente abgerufen werden, die Länge berechnet wird, Speicher zugewiesen wird, Arrays als Slices entliehen werden und mit leeren Slices gearbeitet wird. Darüber hinaus werden wir diskutieren, wie man sicher Elemente eines Arrays mit der `.get()`-Methode zugreift und außereinander liegende Fehler behandelt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
