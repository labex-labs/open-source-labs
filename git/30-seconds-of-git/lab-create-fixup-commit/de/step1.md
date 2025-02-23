# Erstellen eines Fixup-Commits

Angenommen, Sie arbeiten an einem Projekt mit mehreren anderen Entwicklern und bemerken einen kleinen Fehler in einem Commit, der vor ein paar Tagen gemacht wurde. Sie möchten den Fehler beheben, aber Sie möchten keinen neuen Commit erstellen und die Arbeit der anderen Entwickler stören. Hier kommen Fixup-Commits sehr praktisch zum Einsatz. Indem Sie einen Fixup-Commit erstellen, können Sie die erforderlichen Änderungen vornehmen, ohne einen neuen Commit zu erstellen, und der Fixup-Commit wird automatisch mit dem ursprünglichen Commit während der nächsten Rebase zusammengeführt.

Zum Beispiel ist Ihre Aufgabe, die Zeichenfolge "hello,world" in die Datei `hello.txt` zu schreiben und sie als "Fixup"-Commit zum Commit mit der Nachricht "Added file1.txt" hinzuzufügen, so dass sie automatisch in einem späteren Rebase-Vorgang zusammengeführt werden kann.

Für diese Übung verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Erstellen Sie eine Datei `hello.txt`, schreiben Sie "hello,world" darin und fügen Sie sie zum Staging-Bereich hinzu:

```shell
echo "hello,world" > hello.txt
git add.
```

3. Um einen Fixup-Commit zu erstellen, können Sie den Befehl `git commit --fixup <commit>` verwenden:

```shell
git commit --fixup cf80005
# Dies ist der Hash des Commit-Messages "Added file1.txt".
```

Dies wird einen Fixup-Commit für den angegebenen Commit erstellen. Beachten Sie, dass Sie Ihre Änderungen vor dem Erstellen des Fixup-Commits auf die Staging-Liste legen müssen. 4. Nachdem Sie den Fixup-Commit erstellt haben, können Sie den Befehl `git rebase --interactive --autosquash` verwenden, um den Fixup-Commit automatisch mit dem ursprünglichen Commit während der nächsten Rebase zusammenzuführen. Beispiel:

```shell
git rebase --interactive --autosquash HEAD~3
```

Wenn Sie den interaktiven Editor öffnen, müssen Sie den Text nicht ändern und können ihn einfach speichern und schließen. Dies führt eine Rebase auf den letzten 3 Commits durch und fügt automatisch alle Fixup-Commits mit ihren entsprechenden ursprünglichen Commits zusammen.

Dies ist das Ergebnis des Ausführens des Befehls `git show HEAD~1`:

```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
