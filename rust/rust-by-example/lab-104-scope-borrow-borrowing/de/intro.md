# Einführung

In diesem Lab lernen wir über das Entleihen in Rust, das es ermöglicht, auf Daten zuzugreifen, ohne die Eigentumsgewalt zu übernehmen, indem Referenzen ('&T') verwendet werden, anstatt Objekte per Wert ('T') zu übergeben. Der Entleihprüfungsmechanismus gewährleistet, dass Referenzen immer auf gültige Objekte verweisen und verhindert die Zerstörung von Objekten, die entliehen werden.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
