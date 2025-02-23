# Fehlende Submodule klonen

Sie arbeiten an einem Projekt, das Submodule enthält. Wenn Sie das Projekt klonen, werden die Submodule nicht automatisch kloniert. Dies verursacht Probleme, wenn Sie versuchen, das Projekt zu erstellen oder auszuführen. Sie müssen die fehlenden Submodule klonen und die richtigen Commits auschecken.

Für dieses Lab verwenden wir das Git-Repository mit der URL `https://github.com/git/git`. Dieses Repository enthält Submodule, die nicht automatisch kloniert werden, wenn Sie das Repository klonen.

Führen Sie die folgenden Schritte aus, um die fehlenden Submodule zu klonen und die richtigen Commits auszuchecken:

1. Wechseln Sie in das Repository-Verzeichnis:
   ```
   cd git
   ```
2. Initialisieren Sie die Submodule:
   ```
   git submodule update --init --recursive
   ```
3. Wechseln Sie zum richtigen Commit der Submodule, d.h. zur `master`-Branch:
   ```
   git submodule foreach git checkout master
   ```
   Hier ist das Endresultat:

```shell
Submodule'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
