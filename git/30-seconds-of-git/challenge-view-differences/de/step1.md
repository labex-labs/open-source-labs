# Unterschiede in den Änderungen anzeigen

Als Entwickler möchten Sie möglicherweise die Unterschiede zwischen Ihren vorgesetzten oder nicht vorgesetzten Änderungen und dem letzten Commit anzeigen. Dies ist nützlich, wenn Sie Ihre Änderungen überprüfen möchten, bevor Sie sie committen, oder wenn Sie sehen möchten, welche Änderungen Sie seit dem letzten Commit vorgenommen haben.

## Aufgaben

Um zu demonstrieren, wie Sie Unterschiede in den Änderungen anzeigen können, verwenden wir das Repository `git-playground`. Nehmen Sie an, dass Sie einige Änderungen an der Datei `README.md` vorgenommen haben und die Unterschiede zwischen Ihren Änderungen und dem letzten Commit anzeigen möchten.

1. Öffnen Sie Ihr Terminal und navigieren Sie zum Verzeichnis `git-playground`.
2. Zeigen Sie die Unterschiede zwischen Ihren nicht vorgesetzten Änderungen und dem letzten Commit an.
3. Zeigen Sie die Unterschiede zwischen Ihren vorgesetzten Änderungen und dem letzten Commit an.

Dies ist das Ergebnis der Ausführung von Schritt 2:

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

Dies ist das Ergebnis der Ausführung von Schritt 3:

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
