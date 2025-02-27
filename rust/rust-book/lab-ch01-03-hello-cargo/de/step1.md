# Hello, Cargo

Cargo ist das Build-System und Paketmanager von Rust. Die meisten Rust-Entwickler verwenden dieses Tool, um ihre Rust-Projekte zu verwalten, da Cargo für Sie viele Aufgaben erledigt, wie das Erstellen Ihres Codes, das Herunterladen der Bibliotheken, auf die Ihr Code zugreift, und das Erstellen dieser Bibliotheken. (Wir nennen die Bibliotheken, die Ihr Code benötigt, _Abhängigkeiten_.)

Die einfachsten Rust-Programme, wie die bisher von uns geschriebenen, haben keine Abhängigkeiten. Wenn wir das "Hello, world!"-Projekt mit Cargo gebaut hätten, würde es nur den Teil von Cargo verwenden, der das Erstellen Ihres Codes behandelt. Wenn Sie komplexere Rust-Programme schreiben, werden Sie Abhängigkeiten hinzufügen, und wenn Sie ein Projekt mit Cargo starten, wird das Hinzufügen von Abhängigkeiten viel einfacher.

Da der überwiegende Teil der Rust-Projekte Cargo verwendet, wird in diesem Buch davon ausgegangen, dass Sie auch Cargo verwenden. Cargo ist standardmäßig mit Rust installiert, wenn Sie die offiziellen Installationsprogramme aus "Installation" verwendet haben. Wenn Sie Rust auf andere Weise installiert haben, überprüfen Sie, ob Cargo installiert ist, indem Sie Folgendes in Ihrem Terminal eingeben:

```bash
cargo --version
```

Wenn Sie eine Versionsnummer sehen, haben Sie es! Wenn Sie einen Fehler wie "command not found" erhalten, lesen Sie die Dokumentation zu Ihrem Installationsverfahren, um zu bestimmen, wie Sie Cargo separat installieren können.
