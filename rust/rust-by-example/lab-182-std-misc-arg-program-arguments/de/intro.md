# Einführung

In diesem Lab können Sie auf die Befehlszeilenargumente in Rust zugreifen, indem Sie die Funktion `std::env::args` verwenden, die einen Iterator zurückgibt, der für jedes Argument eine `String` zurückgibt. Das erste Argument im zurückgegebenen Vektor ist der Pfad, der verwendet wird, um das Programm aufzurufen, während die restlichen Argumente die Befehlszeilenparameter sind. Alternativ können Sie Crates wie `clap` verwenden, um eine fortgeschrittene Behandlung von Befehlszeilenargumenten durchzuführen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
