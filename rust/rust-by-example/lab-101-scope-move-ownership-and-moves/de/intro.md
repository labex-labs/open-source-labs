# Einführung

In diesem Lab wird erklärt, dass in Rust Variablen die Eigentumsgewalt an Ressourcen haben und nur einen Besitzer haben können, was verhindert, dass Ressourcen mehrfach freigegeben werden. Wenn Variablen zugewiesen werden oder Funktionsargumente per Wert übergeben werden, wird die Eigentumsgewalt an die Ressourcen übertragen, was als Move bezeichnet wird. Nach dem Move kann der vorherige Besitzer nicht mehr verwendet werden, um das Erstellen von fehlerhaften Zeigern zu vermeiden. Das Codebeispiel demonstriert diese Konzepte, indem gezeigt wird, wie die Eigentumsgewalt von auf dem Stack und auf dem Heap zugewiesenen Variablen übertragen wird und wie das Zugreifen auf eine Variable nach Übertragung ihrer Eigentumsgewalt zu Fehlern führt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
