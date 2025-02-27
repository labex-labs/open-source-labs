# Einführung

In diesem Lab untersuchen wir das `newtype`-Idiom, das Kompilierzeitgarantien bietet, indem es uns ermöglicht, einen neuen Typ zu erstellen, der von seinem zugrunde liegenden Typ unterschieden ist. Ein Beispiel wird gezeigt, bei dem eine Struktur `Years` verwendet wird, um das Alter in Jahren darzustellen, und eine Struktur `Days` verwendet wird, um das Alter in Tagen darzustellen. Mit dem `newtype`-Idiom können wir sicherstellen, dass der richtige Werttyp an ein Programm übergeben wird, wie beispielsweise in der Altersüberprüfungsfunktion `old_enough`, die einen Wert vom Typ `Years` erfordert. Darüber hinaus lernen wir, wie wir den Wert eines `newtype` als seinen zugrunde liegenden Typ mithilfe von Tuple- oder Destrukturierungsyntax erhalten.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
