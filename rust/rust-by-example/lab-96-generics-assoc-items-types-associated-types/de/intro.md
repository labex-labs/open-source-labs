# Einführung

In diesem Lab untersuchen wir das Konzept assoziierter Typen in Rust, das es ermöglicht, die Lesbarkeit des Codes zu verbessern, indem innere Typen lokal innerhalb eines Traits als Ausgabetypen definiert werden. Dies wird durch Verwendung des `type`-Schlüsselworts innerhalb der Traitdefinition erreicht. Mit assoziierten Typen müssen Funktionen, die das Trait verwenden, die Typen `A` und `B` nicht mehr explizit ausdrücken, was den Code kompakter und flexibler macht. Wir schreiben ein Beispiel aus einem vorherigen Abschnitt um, um die Verwendung von assoziierten Typen in der Praxis zu veranschaulichen.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
