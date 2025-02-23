# Unterschiede in den Änderungen anzeigen

Als Entwickler möchten Sie möglicherweise die Unterschiede zwischen Ihren vorbereiteten oder nicht vorbereiteten Änderungen und dem letzten Commit anzeigen. Dies ist nützlich, wenn Sie Ihre Änderungen überprüfen möchten, bevor Sie sie committen, oder wenn Sie sehen möchten, welche Änderungen Sie seit dem letzten Commit vorgenommen haben.

Um zu demonstrieren, wie man Unterschiede in Änderungen anzeigt, verwenden wir das Repository `git-playground`. Nehmen wir an, Sie haben einige Änderungen am `README.md`-File vorgenommen und möchten die Unterschiede zwischen Ihren Änderungen und dem letzten Commit anzeigen.

1. Öffnen Sie Ihr Terminal und navigieren Sie zum `git-playground`-Verzeichnis:

```shell
cd git-playground
```

2. Verwenden Sie den Befehl `git diff`, um die Unterschiede zwischen Ihren nicht vorbereiteten Änderungen und dem letzten Commit anzuzeigen:

```shell
git diff
```

3. Alternativ können Sie die Option `--staged` verwenden, um die Unterschiede zwischen Ihren vorbereiteten Änderungen und dem letzten Commit anzuzeigen:

```shell
git diff --staged
```

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
