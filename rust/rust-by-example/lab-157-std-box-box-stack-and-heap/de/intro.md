# Einführung

In diesem Lab wird das Konzept des Boxings, der Stack- und Heap-Allokation in Rust untersucht. Alle Werte in Rust werden standardmäßig auf dem Stack zugewiesen, können jedoch mit dem Typ `Box<T>` geboxed (auf dem Heap zugewiesen) werden. Ein Box ist ein Smart-Pointer auf einen auf dem Heap zugewiesenen Wert, und wenn er außer Reichweite gelangt, wird dessen Destruktor aufgerufen und der Speicher auf dem Heap freigegeben. Boxing ermöglicht die Erstellung von Doppelindirektion und kann mit dem `*`-Operator dereferenziert werden. Das Lab bietet Codebeispiele und Erklärungen dazu, wie Boxing funktioniert und wie es die Speicherzuweisung auf dem Stack beeinflusst.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
