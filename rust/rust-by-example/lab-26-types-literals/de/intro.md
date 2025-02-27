# Einführung

In diesem Lab lernen wir über Literale in Rust und wie wir ihren Typ durch Hinzufügen eines Suffixes angeben können. Suffixed Literale haben ihren Typ bei der Initialisierung bekannt, während der Typ von unsuffixed Literalen von der Verwendung abhängt. Die `size_of_val`-Funktion wird verwendet, um die Größe einer Variable in Bytes zu bestimmen, und sie wird mit ihrem vollständigen Pfad `std::mem::size_of_val` aufgerufen. Die `size_of_val`-Funktion ist in das `mem`-Modul definiert, das wiederum im `std`-Kasten definiert ist.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
