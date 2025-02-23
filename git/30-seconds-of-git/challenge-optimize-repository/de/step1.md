# Den lokalen Git-Repository optimieren

Im Laufe der Zeit kann Ihr Git-Repository mit alten Versionen von Dateien und anderen unnötigen Daten verwirrt werden. Dies kann Git verlangsamen und es schwieriger machen, mit Ihrem Repository umzugehen. Um Ihren lokalen Git-Repository zu optimieren, müssen Sie diese unnötigen Daten entfernen.

Wenn Sie den Befehl ausführen, entfernt Git alle lose Objekte (Objekte, auf die keine Branch oder Tag verweist) und packt die verbleibenden Objekte in eine neue Gruppe von Pack-Dateien. Dies kann die Größe Ihres Repositories erheblich reduzieren und die Leistung von Git verbessern.

## Aufgaben

Nehmen wir an, dass Sie ein Git-Repository namens `git-playground` im Home-Verzeichnis haben und dieses Repository optimieren möchten.

Dies ist das Ergebnis der Optimierung des `git-playground`-Repositories, indem alle lose Objekte entfernt und die verbleibenden Objekte in eine neue Gruppe von Pack-Dateien gepackt werden:

![Optimized Git repository result](../assets/challenge-optimize-repository-step1-1.png)
