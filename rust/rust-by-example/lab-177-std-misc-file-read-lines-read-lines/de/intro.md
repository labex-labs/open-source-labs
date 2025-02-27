# Einführung

In diesem Lab erhalten wir eine naive Implementierung und eine effizientere Implementierung für das Lesen von Zeilen aus einer Datei in Rust. Der naive Ansatz verwendet `read_to_string`, um die Datei in einen einzelnen String zu lesen und teilt ihn dann in Zeilen auf, während der effizientere Ansatz einen `BufReader` verwendet, um die Datei Zeile für Zeile zu lesen, ohne den gesamten Inhalt in den Speicher zu laden.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
