# Alle Einsparobjekte auflisten

Sie arbeiten an einem Projekt in einem Git-Repository und haben einige Änderungen vorgenommen, die noch nicht zum Commit bereit sind. Sie entscheiden, diese Änderungen einzusparen, damit Sie an einer anderen Aufgabe arbeiten können. Später möchten Sie eine Liste aller erstellten Einsparobjekte sehen, um zu entscheiden, welches Sie anwenden möchten. Wie können Sie alle Einsparobjekte in einem Git-Repository auflisten?

1. Navigieren Sie zum Verzeichnis `git-playground`:

```
cd git-playground
```

2. Erstellen Sie eine neue Datei namens `test.txt` und fügen Sie ihr etwas Inhalt hinzu:

```
echo "hello,world" > test.txt
git add.
```

3. Verwenden Sie den folgenden Befehl, um Ihre Änderungen einzusparen:

```
git stash save "Added test.txt"
```

4. Erstellen Sie eine weitere neue Datei namens `test2.txt` und fügen Sie ihr etwas Inhalt hinzu:

```
echo "hello,labex" > test2.txt
git add.
```

5. Verwenden Sie den folgenden Befehl, um Ihre Änderungen einzusparen:

```
git stash save "Added test2.txt"
```

6. Verwenden Sie den folgenden Befehl, um alle Einsparobjekte aufzulisten:

```
git stash list
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
