# Git-Konfigurationsdatei bearbeiten

Als Entwickler müssen Sie möglicherweise die Git-Konfigurationsdatei ändern, um das Verhalten von Git anzupassen. Die Git-Konfigurationsdatei ist eine einfache Textdatei, die Einstellungen im Format Schlüssel-Wert-Paare enthält. Die Datei kann mit jedem Texteditor bearbeitet werden, aber Git bietet einen eingebauten Texteditor, der zur Bearbeitung der Konfigurationsdatei verwendet werden kann.

In diesem Beispiel verwenden wir das Git-Repository im Verzeichnis `https://github.com/labex-labs/git-playground`, um zu demonstrieren, wie die Git-Konfigurationsdatei bearbeitet wird.

1. Öffnen Sie das Terminal und navigieren Sie zum Verzeichnis des Git-Repositorys:

```shell
cd git-playground
```

2. Verwenden Sie den folgenden Befehl, um die Git-Konfigurationsdatei im Git-Texteditor zu öffnen:

```shell
git config --global -e
```

3. Der obige Befehl öffnet die Git-Konfigurationsdatei im standardmäßigen Git-Texteditor. Sie können die Einstellungen ändern, sodass der Benutzername `labex_git` und die Benutzere-Mail `labex_git@example.com` ist.
4. Nachdem Sie die erforderlichen Änderungen vorgenommen haben, drücken Sie <kbd>Esc</kbd> und geben Sie den Befehl <kbd>:wq</kbd> ein, dann drücken Sie <kbd>Enter</kbd>, um Ihre Änderungen zu speichern und den Editor zu verlassen.

Dies ist das Ergebnis nach Abschluss:

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
