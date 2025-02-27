# Einführung

In diesem Lab werden wir die `Path`-Struktur in Rust untersuchen, die Dateipfade im zugrunde liegenden Dateisystem repräsentiert. Sie kommt in zwei Varianten: `posix::Path` für UNIX-ähnliche Systeme und `windows::Path` für Windows. Ein `Path` kann aus einem `OsStr` erstellt werden und bietet verschiedene Methoden, um Informationen aus der Datei oder dem Verzeichnis zu erhalten, auf das der Pfad zeigt. Es ist wichtig zu beachten, dass ein `Path` unveränderlich ist, und seine eigene Version heißt `PathBuf`, die in-place verändert werden kann. Die Beziehung zwischen `Path` und `PathBuf` ist ähnlich der zwischen `str` und `String`.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
