# Fügen Sie eine Commit-Nachricht-Vorlage hinzu

Ohne eine Commit-Nachricht-Vorlage können Entwickler versucht sein, vage oder uninformative Commit-Nachrichten zu schreiben, wie z. B. "Bug behoben" oder "Code aktualisiert". Dies erschwert es anderen, den Zweck der Änderung zu verstehen und kann zu Verwirrung oder Fehlern führen. Indem eine Commit-Nachricht-Vorlage eingerichtet wird, werden Entwicklern ermutigt, detailliertere und informativere Commit-Nachrichten zu liefern, was die Zusammenarbeit und die Produktivität verbessern kann.

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten, um eine Commit-Nachricht-Vorlage für dieses Repository einzurichten:

1. Klonen Sie das Repository auf Ihren lokalen Computer, indem Sie den Befehl `git clone https://github.com/labex-labs/git-playground` verwenden.
2. Navigieren Sie zum Repository-Verzeichnis, indem Sie den Befehl `cd git-playground` verwenden, und konfigurieren Sie Ihr GitHub-Konto, indem Sie die Befehle `git config --global user.name "Ihr-Benutzername"` und `git config --global user.email "Ihre-E-Mail"` verwenden.
3. Erstellen Sie in dem Repository-Verzeichnis eine neue Datei namens `commit-template`, indem Sie den Befehl `vim commit-template` verwenden.
4. Öffnen Sie die Datei `commit-template` in einem Texteditor und fügen Sie die folgenden Zeilen hinzu:

```shell
# <type>: <subject>

# <body>

# <footer>

#Dies erstellt eine Vorlage mit drei Abschnitten, wobei "<type>" den Typ der Abgabe angibt, wie z. B. "feat" oder "fix", "<subject>" eine kurze Zusammenfassung ist, die den Inhalt der Abgabe beschreibt, "<body>" eine detailliertere Beschreibung ist und "<footer>" andere Metadaten enthalten kann, wie die zugehörige Issues-Nummer oder andere Kommentare.
```

5. Drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den `commit-template`-Dateieditor zu verlassen.
6. Verwenden Sie den Befehl `git add commit-template`, um die `commit-template`-Dateien zum Staging-Bereich hinzuzufügen.
7. Verwenden Sie den Befehl `git config commit.template commit-template`, um die `commit-template`-Datei als Commit-Nachricht-Vorlage für das Repository festzulegen.
8. Verwenden Sie den Befehl `git commit`, um den Commit-Nachrichteneditor zu öffnen, und beobachten Sie, dass der Commit-Nachrichteneditor jetzt die Commit-Nachricht-Vorlage enthält, die Sie in Schritt 4 erstellt haben.
9. Drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:q</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um den Commit-Nachrichteneditor zu verlassen.
