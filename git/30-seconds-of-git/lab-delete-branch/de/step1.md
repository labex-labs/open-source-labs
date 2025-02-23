# Ein Branch löschen

Du hast einen lokalen Branch in deinem Git-Repository erstellt und brauchst ihn nicht mehr. Du möchtest den Branch löschen, um dein Repository sauber und strukturiert zu halten.

1. Navigiere zum geklonten Repository:

```shell
cd git-playground
```

2. Zeige die aktuellen Branches an:

```shell
git branch
```

3. Lösche den Branch `feature-1`:

```shell
git branch -d feature-1
```

4. Verifiziere, dass der Branch gelöscht wurde:

```shell
git branch
```

Dies ist das Ergebnis der Ausführung des Befehls `git branch`:

```
* master
```
