# Einführung

In diesem Lab ist die primäre Methode der Dokumentation eines Rust-Projekts die Annotation des Quellcodes mit Dokumentationskommentaren, die in der CommonMark Markdown-Spezifikation geschrieben sind und Codeblöcke darin unterstützen. Rust kümmert sich um die Korrektheit und diese Codeblöcke werden kompiliert und als Dokumentationstests verwendet. Diese Tests werden automatisch ausgeführt, wenn der Befehl `cargo test` verwendet wird. Der Grund hinter den Dokumentationstests ist, als Beispiele zu dienen, die die Funktionalität testen und es ermöglichen, Beispiele aus der Dokumentation als vollständige Codeausschnitte zu verwenden.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
