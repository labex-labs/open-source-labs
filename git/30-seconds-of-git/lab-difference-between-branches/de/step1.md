# Unterschied zwischen Branches

Sie arbeiten an einem Projekt mit Ihrem Team und haben einen Branch namens `feature-1` erstellt, um an einem neuen Feature zu arbeiten. Ihr Kollege hat ebenfalls einen Branch namens `feature-2` erstellt, um an einem anderen Feature zu arbeiten. Sie möchten die Änderungen zwischen den beiden Branches vergleichen, um zu sehen, was hinzugefügt, geändert oder gelöscht wurde. Wie können Sie den Unterschied zwischen den beiden Branches anzeigen?

Nehmen Sie an, dass Ihr GitHub-Konto ein Repository namens `git-playground` von `https://github.com/labex-labs/git-playground.git` klont. Folgen Sie den Schritten unten:

1. Wechseln Sie in das Verzeichnis des Repositorys mit dem Befehl `cd git-playground`.
2. Konfigurieren Sie Ihr GitHub-Konto in dieser Umgebung mit den Befehlen `git config --global user.name "Ihr Name"` und `git config --global user.email "ihr@email.com"`.
3. Erstellen Sie und wechseln Sie zum Branch `feature-1` mit dem Befehl `git checkout -b feature-1`, fügen Sie "hello" zur Datei `README.md` hinzu, fügen Sie es zum Staging-Area hinzu und committen Sie es, die Commit-Nachricht lautet "Add new content to README.md" mit den Befehlen `echo "hello" >> README.md `, `git add.` und `git commit -am "Add new content to README.md"`.
4. Wechseln Sie zurück zum `master`-Branch.
5. Erstellen Sie und wechseln Sie zum Branch `feature-2` mit dem Befehl `git checkout -b feature-2`, fügen Sie "world" zur Datei `index.html` hinzu, fügen Sie es zum Staging-Area hinzu und committen Sie es, die Commit-Nachricht lautet "Update index.html file" mit den Befehlen `echo "world" > index.htm`, `git add.` und `git commit -am "Update index.html file"`.
6. Zeigen Sie den Unterschied zwischen den beiden Branches mit dem Befehl `git diff feature-1..feature-2`.

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
