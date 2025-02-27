# Einführung

In diesem Lab zeigt der Code, wie man den `Box`-Typ verwendet, um ursprüngliche Fehler zu bewahren, indem man sie umschließt, um eine dynamische Fehlerbehandlung zu ermöglichen. Das `From`-Attribut der `Std`-Bibliothek hilft dabei, beliebige Typen, die das `Error`-Attribut implementieren, in das Attributobjekt `Box<Error>` umzuwandeln. Es enthält ein Beispiel zur Umwandlung und Behandlung von Fehlern mit `Box` mit einem benutzerdefinierten Fehlertyp.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
