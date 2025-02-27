# Einführung

In diesem Lab lernen wir über Rusts Foreign Function Interface (FFI), das es ermöglicht, mit C-Bibliotheken zu interagieren, indem wir fremde Funktionen innerhalb eines `extern`-Blocks deklarieren und sie mit einem `#[link]`-Attribut versehen, das den Namen der fremden Bibliothek enthält. Das Codebeispiel zeigt die Verwendung von FFI, um externe Funktionen aus der `libm`-Bibliothek aufzurufen, wie das Berechnen der Quadratwurzel einer einfachen Gleitkommazahl und die Berechnung des Kosinus einer komplexen Zahl. Safe Wrapper werden üblicherweise um diese unsicheren fremden Funktionsaufrufe verwendet. Das Lab enthält auch eine minimale Implementierung von einfachen Gleitkommazahlen und zeigt, wie man sichere APIs aufruft, die um unsichere Operationen gewrappt sind.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
