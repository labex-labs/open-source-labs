# Einführung

In diesem Lab haben wir eine `create`-Funktion, die eine Datei im schreibgeschützten Modus öffnet. Sie erstellt entweder eine neue Datei oder zerstört den alten Inhalt, wenn die Datei bereits existiert. Die Funktion verwendet die Standardbibliothek von Rust, um Dateioperationen zu verarbeiten. Das bereitgestellte Beispiel zeigt, wie die `create`-Funktion verwendet wird, um den Inhalt einer statischen `LOREM_IPSUM`-Zeichenfolge in eine Datei namens "lorem_ipsum.txt" zu schreiben. Die Ausgabe zeigt eine Bestätigung für einen erfolgreichen Schreibvorgang, und der Inhalt der Datei wird mit dem Befehl `cat` angezeigt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden, es mit `rustc main.rs &&./main` kompilieren und ausführen.
