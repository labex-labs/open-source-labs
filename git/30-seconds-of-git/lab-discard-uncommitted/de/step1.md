# Nicht committete Änderungen verwerfen

Sie haben einige Änderungen an Ihrem lokalen Git-Repository vorgenommen, aber Sie haben sie noch nicht committet. Dennoch haben Sie beschlossen, diese Änderungen nicht mehr zu behalten und möchten sie verwerfen. Das Problem besteht darin, einen Weg zu finden, um alle nicht committeten Änderungen an der aktuellen Branch zu verwerfen.

Um diese Herausforderung zu bewältigen, verwenden Sie das Git-Repository im Verzeichnis `https://github.com/labex-labs/git-playground`. Folgen Sie den Schritten unten:

1. Klonen Sie das Repository auf Ihren lokalen Computer mit dem Befehl `git clone https://github.com/labex-labs/git-playground.git`.
2. Navigieren Sie zum geklonten Repository mit dem Befehl `cd git-playground`.
3. Machen Sie einige Änderungen an den Dateien im Repository, aber committen Sie sie nicht mit den Befehlen `echo "hello,world" > hello.txt` und `git add.`.
4. Verwenden Sie den Befehl `git status`, um die Änderungen zu sehen, die Sie vorgenommen haben.
5. Verwerfen Sie alle nicht committeten Änderungen mit dem Befehl `git reset --hard HEAD`.
6. Verwenden Sie erneut den Befehl `git status`, um zu bestätigen, dass alle Änderungen verworfen wurden.

Dies ist das Ergebnis von `git status`:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
