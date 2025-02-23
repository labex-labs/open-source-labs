# Den lokalen Speicherort optimieren

Im Laufe der Zeit kann Ihr Git-Repository mit alten Versionen von Dateien und anderen unnötigen Daten verwirrt werden. Dies kann Git verlangsamen und es schwieriger machen, mit Ihrem Repository umzugehen. Um Ihren lokalen Speicherort zu optimieren, müssen Sie diese unnötigen Daten entfernen. Dies kann mit dem Befehl `git gc` erreicht werden.

Der Befehl `git gc` steht für "Git-Sammelstammsäuberung". Er wird verwendet, um unnötige Daten in Ihrem Repository zu bereinigen. Wenn Sie `git gc` ausführen, entfernt Git alle lose Objekte (Objekte, auf die keine Branch oder Tag verweist) und packt die verbleibenden Objekte in eine neue Reihe von Packdateien. Dies kann die Größe Ihres Repositories erheblich reduzieren und die Leistung von Git verbessern.

Um den lokalen Speicherort zu optimieren, können Sie den Befehl `git gc` mit den Optionen `--prune=now` und `--aggressive` verwenden. Beispielsweise haben Sie ein Git-Repository namens `git-playground` im Home-Verzeichnis. Um dieses Repository zu optimieren, führen Sie folgenden Befehl aus:

```shell
cd git-playground
git gc --prune=now --aggressive
```

Dies ist das Ergebnis der Optimierung des `git-playground`-Repositories, indem alle lose Objekte entfernt und die verbleibenden Objekte in eine neue Reihe von Packdateien gepackt werden:

![Git repository optimization result](../assets/challenge-optimize-repository-step1-1.png)
