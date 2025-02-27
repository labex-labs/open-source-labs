# Einführung

In diesem Lab lernen wir über Variable Bindungen, deren Gültigkeitsbereich und das Konzept des Shadowings in Rust. Variable Bindungen sind auf einen Block beschränkt, der eine Sammlung von Anweisungen ist, die in geschweiften Klammern eingeschlossen sind. Es werden zwei Beispiele angegeben, um diese Konzepte zu veranschaulichen. Im ersten Beispiel wird gezeigt, wie eine Variable Bindung, die innerhalb eines Blocks deklariert wird, auf den Gültigkeitsbereich dieses Blocks beschränkt ist und außerhalb davon nicht zugänglich ist. Im zweiten Beispiel wird das Variable Shadowing demonstriert, bei dem eine neue Bindung mit dem gleichen Namen innerhalb eines Blocks deklariert wird, was effektiv die äußere Bindung überdeckt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
