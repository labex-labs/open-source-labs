# Einführung

In diesem Lab haben wir einige Rust-Code, der die Verwendung von Lebensdauern in Structs demonstriert. Der Code enthält ein Struct namens `Borrowed`, das eine Referenz auf ein `i32` aufnimmt, und die Referenz muss die Lebensdauer des Structs selbst überdauern. Es gibt auch ein Struct namens `NamedBorrowed` mit zwei Referenzen auf `i32`, von denen beide die Lebensdauer des Structs überdauern müssen. Darüber hinaus gibt es eine Enumeration namens `Either`, die entweder ein `i32` oder eine Referenz auf eines sein kann, und die Referenz muss die Lebensdauer der Enumeration überdauern. Schließlich erstellt der Code Instanzen dieser Structs und Enumeration und druckt deren Inhalte aus, um die Verwendung von Lebensdauern in Rust zu demonstrieren.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
