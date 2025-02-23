# Einen Stash anwenden

Sie arbeiten an einer Feature-Branch im Repository `git-playground` und müssen zu einer anderen Branch wechseln, um einen Bug zu beheben. Allerdings haben Sie einige Änderungen, die noch nicht committet werden sollen. Sie möchten diese Änderungen speichern und zur anderen Branch wechseln. Nachdem Sie mit der Bugbehebung fertig sind, möchten Sie den Stash anwenden und fortfahren, indem Sie an Ihrer Feature-Branch arbeiten.

Die Änderungen wurden auf der Branch `feature-branch` gestasht, und die Stash-Nachricht lautet "my changes".

1. Wechseln Sie in das Verzeichnis `git-playground`:

```shell
cd git-playground
```

2. Wechseln Sie zur Branch `master` und stashen Sie sie nach der Bugbehebung. Die Stash-Nachricht lautet "fix the bug". Beheben Sie den Bug, indem Sie den Inhalt der Datei `file1.txt` auf "hello,world" aktualisieren:

```shell
git checkout master
echo "hello,world" > file1.txt
git stash save "fix the bug"
```

3. Wechseln Sie zur Branch `feature-branch`, betrachten Sie die Liste der Stashes und wenden Sie den Stash an, dessen Informationen "my changes" sind:

```shell
git checkout feature-branch
git stash apply stash@{1}
```

Dies ist der Inhalt der Datei `README.md`:

```
# git-playground
Git Playground
some changes
```

Sie sollten sehen, dass die Änderungen, die Sie vor dem Stashen gemacht haben, jetzt angewendet wurden.
