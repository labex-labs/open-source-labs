# Einführung

In diesem Lab lernst du über das `cfg`-Attribut und die `cfg!`-Makro in Rust, die jeweils bedingte Prüfungen bei der Konfiguration und der Auswertung ermöglichen. Das `cfg`-Attribut ermöglicht die bedingte Kompilierung, während das `cfg!`-Makro zur Laufzeit als wahr oder falsch ausgewertet wird. Codeblöcke, die `cfg!` verwenden, müssen unabhängig vom Auswertungsergebnis gültig sein, im Gegensatz zu `#[cfg]`, das Code entfernen kann.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, kannst du einen beliebigen Dateinamen verwenden. Beispielsweise kannst du `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
