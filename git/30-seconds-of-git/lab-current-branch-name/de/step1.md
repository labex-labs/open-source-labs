# Holt den Namen des aktuellen Branches

Schreiben Sie einen Befehl, der den Namen des aktuellen Branches in einem Git-Repository ausgibt.

Angenommen, Sie arbeiten an einem Projekt, das im Repository `https://github.com/labex-labs/git-playground` gespeichert ist. Sie haben einige Änderungen am `README.md`-File vorgenommen und möchten sie an den aktuellen Branch committen. Bevor Sie dies tun, möchten Sie jedoch sicherstellen, dass Sie sich auf dem richtigen Branch befinden.

Um den aktuellen Branch zu überprüfen, können Sie folgenden Befehl verwenden:

```shell
git rev-parse --abbrev-ref HEAD
```

Dies wird den Namen des aktuellen Branches in der Konsole ausgeben. Beispielsweise wird die Ausgabe lauten, wenn Sie sich derzeit auf dem `master`-Branch befinden:

```shell
master
```

Wenn Sie zu einem anderen Branch wechseln, wie `feature-branch`, wird die Ausgabe entsprechend geändert:

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

Dies wird die folgende Ausgabe erzeugen:

```shell
feature-branch
```
