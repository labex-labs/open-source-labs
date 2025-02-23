# Fügen Sie eine Commit-Nachricht-Vorlage hinzu

Ohne eine Commit-Nachricht-Vorlage können Entwickler versucht sein, vage oder uninformativ Commit-Nachrichten zu schreiben, wie z. B. "Bug behoben" oder "Code aktualisiert". Dies erschwert es anderen, den Zweck der Änderung zu verstehen und kann zu Verwirrung oder Fehlern führen. Indem eine Commit-Nachricht-Vorlage eingerichtet wird, werden Entwicklern ermutigt, detailliertere und informativere Commit-Nachrichten zu liefern, was die Zusammenarbeit und Produktivität verbessern kann.

## Aufgaben

Für diese Herausforderung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Navigieren Sie zum Repository-Verzeichnis und konfigurieren Sie Ihre GitHub-Identität.
2. Erstellen Sie in dem aktuellen Verzeichnis des Repositorys eine neue Datei namens `commit-template`.
3. Öffnen Sie die Datei `commit-template` in einem Texteditor und fügen Sie die folgenden Zeilen hinzu:

```shell
# <type>: <subject>

# <body>

# <footer>

# Dies erstellt eine Vorlage mit drei Abschnitten:
# "<type>" gibt den Typ der Abgabe an, z. B. "feat" oder "fix"
# "<subject>" ist eine kurze Zusammenfassung, die den Inhalt der Abgabe beschreibt
# "<body>" ist eine detailliertere Beschreibung
# "<footer>" kann andere Metadaten enthalten, wie die zugehörige Issue-Nummer oder andere Anmerkungen.
```

4. Drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den `commit-template`-Dateieditor zu verlassen.
5. Fügen Sie die `commit-template`-Dateien in den Staging-Bereich hinzu.
6. Legen Sie die `commit-template`-Datei als Commit-Nachricht-Vorlage für das Repository fest.
7. Öffnen Sie den Commit-Nachrichteneditor und beobachten Sie, dass der Commit-Nachrichteneditor jetzt die von Ihnen in Schritt 3 erstellte Commit-Nachricht-Vorlage enthält.
8. Drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:q</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um den Commit-Nachrichteneditor zu verlassen.
