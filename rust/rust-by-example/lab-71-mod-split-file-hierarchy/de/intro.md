# Einführung

In diesem Lab kann die Dateihierarchie der Module im Codebeispiel wie folgt dargestellt werden: Es gibt ein Verzeichnis namens "my", das zwei Dateien enthält, "inaccessible.rs" und "nested.rs". Darüber hinaus gibt es eine Datei namens "my.rs" und eine Datei namens "split.rs". Die Datei "split.rs" enthält das Modul "my", das in der Datei "my.rs" definiert ist, und die Datei "my.rs" enthält die Module "inaccessible" und "nested", die in den Dateien "inaccessible.rs" und "nested.rs" definiert sind.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
