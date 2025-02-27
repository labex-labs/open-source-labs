# Einführung

In diesem Lab haben wir einen Codeausschnitt in Rust, der zeigt, wie man native Betriebssystem-Threads mit der `spawn`-Funktion und einer verschiebenden Closure erzeugt. Der Code erstellt einen Vektor, um die erzeugten Threads zu speichern, iteriert über einen Zahlenbereich, um mehrere Threads zu erzeugen und gibt eine Nachricht aus, die jede Threadnummer identifiziert. Schließlich wartet der Hauptthread, bis jeder erzeugte Thread mit der `join`-Funktion abgeschlossen ist.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
