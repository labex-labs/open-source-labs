# Einführung

In diesem Lab werden wir das leistungsstarke Makrosystem von Rust erkunden, das es ermöglicht, durch die Expansion von Makros in abstrakte Syntaxbäume Metaprogrammierung durchzuführen. Die `macro_rules!`-Makro wird verwendet, um Makros zu erstellen, und sie unterscheiden sich von Funktionen durch ihr abschließendes Ausrufezeichen `!`. Makros sind nützlich, um Codewiederholungen zu vermeiden, domänenspezifische Sprachen zu erstellen und variadische Schnittstellen für Funktionen zu definieren, die eine variable Anzahl von Argumenten akzeptieren können.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
