# Unterschiede zwischen Branches

Sie arbeiten an einem Projekt mit Ihrem Team und haben einen Branch namens `feature-1` erstellt, um an einer neuen Funktion zu arbeiten. Ihr Kollege hat ebenfalls einen Branch namens `feature-2` erstellt, um an einer anderen Funktion zu arbeiten. Sie möchten die Änderungen zwischen den beiden Branches vergleichen, um zu sehen, was hinzugefügt, geändert oder gelöscht wurde. Wie können Sie den Unterschied zwischen den beiden Branches anzeigen?

## Aufgaben

Nehmen Sie an, dass Ihr GitHub-Konto ein Repository namens `git-playground` von `https://github.com/labex-labs/git-playground.git` klont.

1. Navigieren Sie zum Repository-Verzeichnis und konfigurieren Sie Ihre GitHub-Identität.
2. Wechseln Sie zum Branch `feature-1` und fügen Sie "hello" zur Datei `README.md` hinzu, fügen Sie es zum Staging-Bereich hinzu und committen Sie es, die Commit-Nachricht lautet "Add new content to README.md".
3. Wechseln Sie zum Branch `feature-2` und fügen Sie "world" zur Datei `index.html` hinzu, fügen Sie es zum Staging-Bereich hinzu und committen Sie es, die Commit-Nachricht lautet "Update index.html file".
4. Zeigen Sie den Unterschied zwischen den beiden Branches an.

Die Ausgabe sollte den Unterschied zwischen den Branches `feature-1` und `feature-2` anzeigen. Dies zeigt, wie das Endresultat aussehen wird:

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
