# Einführung

In diesem Lab wird die Verwendung von `let`-`else` in Rust demonstriert, wobei ein widerlegbarer Muster Variablen im umgebenden Gültigkeitsbereich abgleichen und binden kann, oder andernfalls bei einem nicht übereinstimmenden Muster durch Verwendung von Anweisungen wie `break`, `return` oder `panic!` divergieren kann. Dieser Aufbau ermöglicht es, bei der Behandlung von Musterabgleich und Fehlerbehandlungsszenarien kompakte und lesbare Code zu schreiben, wodurch die Wiederholung von Codeblöcken oder die Verwendung von äußeren `let`-Anweisungen entfällt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
