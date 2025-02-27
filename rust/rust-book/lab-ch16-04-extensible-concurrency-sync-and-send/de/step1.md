# Erweiterbare Concurrency mit den Send- und Sync-Traits

Interessanterweise hat die Rust-Sprache _sehr_ wenige Concurrency-Features. Fast jede Concurrency-Funktion, über die wir bisher in diesem Kapitel gesprochen haben, war Teil der Standardbibliothek, nicht der Sprache. Ihre Optionen zur Behandlung von Concurrency sind nicht auf die Sprache oder die Standardbibliothek beschränkt; Sie können eigene Concurrency-Features schreiben oder die von anderen verwenden.

Allerdings sind zwei Concurrency-Konzepte in die Sprache eingebettet: die `std::marker`-Traits `Send` und `Sync`.
