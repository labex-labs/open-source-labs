# Separation of Concerns for Binary Projects

Das organisatorische Problem, die Verantwortung für mehrere Aufgaben der `main`-Funktion zuzuweisen, ist vielen binären Projekten gemeinsam. Aus diesem Grund hat die Rust-Community Leitlinien entwickelt, um die verschiedenen Aspekte eines binären Programms zu trennen, wenn `main` zu groß wird. Dieser Prozess hat die folgenden Schritte:

- Teilen Sie Ihr Programm in eine `main.rs`-Datei und eine `lib.rs`-Datei auf und verschieben Sie die Logik Ihres Programms in `lib.rs`.
- Solange Ihre Befehlszeilenanalyse-Logik klein ist, kann sie in `main.rs` verbleiben.
- Wenn die Befehlszeilenanalyse-Logik anspruchsvoller wird, extrahieren Sie sie aus `main.rs` und verschieben Sie sie in `lib.rs`.

Die Verantwortungen, die nach diesem Prozess in der `main`-Funktion verbleiben, sollten auf Folgendes beschränkt sein:

- Aufrufen der Befehlszeilenanalyse-Logik mit den Argumentwerten
- Einrichten jeder anderen Konfiguration
- Aufrufen einer `run`-Funktion in `lib.rs`
- Behandeln des Fehlers, wenn `run` einen Fehler zurückgibt

Dieses Muster geht darum, die Aspekte voneinander zu trennen: `main.rs` kümmert sich um das Ausführen des Programms, und `lib.rs` kümmert sich um alle Logiken der vorliegenden Aufgabe. Da Sie die `main`-Funktion nicht direkt testen können, ermöglicht diese Struktur, alle Logiken Ihres Programms zu testen, indem Sie sie in Funktionen in `lib.rs` verschieben. Der Code, der in `main.rs` verbleibt, wird klein genug sein, um seine Korrektheit durch das Lesen zu überprüfen. Lassen Sie uns unser Programm gemäß diesem Prozess umarbeiten.
