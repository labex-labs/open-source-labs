# Einführung

In diesem Lab wird das Konzept der Zwangsumwandlung in Rust untersucht, bei der eine längere Lebensdauer in eine kürzere umgewandelt werden kann, um Funktionen innerhalb eines bestimmten Bereichs zu ermöglichen. Dies kann durch die von Rust-Compiler inferierte Zwangsumwandlung oder durch die Angabe eines Lebensdauerunterschieds mit Syntax wie `<'a: 'b, 'b>` erfolgen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
