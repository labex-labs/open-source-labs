# Den neuesten Stash anwenden

Sie arbeiten an einem Projekt in Ihrem Git-Repository und haben einige Änderungen vorgenommen, die noch nicht zum Committen bereit sind. Sie müssen jedoch zu einer anderen Branch oder einem anderen Commit wechseln, um an einer anderen Funktion zu arbeiten. Sie möchten Ihre Änderungen nicht verlieren, also entscheiden Sie sich, sie zu stashen. Später, wenn Sie bereit sind, fortzufahren, Ihre Änderungen zu bearbeiten, müssen Sie den neuesten Stash auf Ihr Arbeitsverzeichnis anwenden.

## Aufgaben

Um den neuesten Stash auf Ihr Git-Repository anzuwenden, führen Sie die folgenden Schritte aus:

1. Auflisten Ihrer Stashes. Sie sollten einen Stash in der Liste sehen.
2. Den neuesten Stash auf Ihr Arbeitsverzeichnis anwenden.
3. Überprüfen Sie die Datei `README.md`, um zu sehen, dass Ihre Änderungen angewendet wurden.

Dies ist das Ergebnis des Ausführens des Befehls `cat README.md`:

![README-Dateiänderungen angewendet](../assets/challenge-apply-latest-stash-step1-1.png)

Dieser Befehl wendet die Änderungen aus dem zuletzt gespeicherten Stash erneut auf das aktuelle Arbeitsverzeichnis an und fügt der Datei `README.md` die neue Zeile "Dies ist eine neue Zeile" hinzu.
