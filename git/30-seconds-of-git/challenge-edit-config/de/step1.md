# Bearbeite die Git-Konfigurationsdatei

Als Entwickler mögen Sie die Git-Konfigurationsdatei ändern, um das Verhalten von Git anzupassen. Die Git-Konfigurationsdatei ist eine einfache Textdatei, die Einstellungen im Format Schlüssel-Wert-Paare enthält. Die Datei kann mit jedem Texteditor bearbeitet werden, aber Git bietet einen eingebauten Texteditor an, mit dem die Konfigurationsdatei geändert werden kann.

## Aufgaben

In diesem Beispiel verwenden wir das Verzeichnis des Git-Repositorys mit der URL `https://github.com/labex-labs/git-playground`.

1. Öffnen Sie das Terminal und navigieren Sie zum Verzeichnis des Git-Repositorys.
2. Öffnen Sie die Git-Konfigurationsdatei im Git-Texteditor.
3. Ändern Sie die Einstellungen so, dass der Benutzername `labex_git` und die Benutzere-Mail `labex_git@example.com` ist.
4. Nachdem Sie die erforderlichen Änderungen vorgenommen haben, drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den Editor zu verlassen.

Dies ist das Ergebnis nach der Fertigstellung:

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
