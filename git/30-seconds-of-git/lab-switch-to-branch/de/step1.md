# Wechsel zu einem Branch

Du arbeitest an einem Projekt in einem Git-Repository namens `https://github.com/labex-labs/git-playground`. Dein Team hat einen neuen Branch namens `feature-1` erstellt, um an einer neuen Funktion zu arbeiten. Du musst zum Branch `feature-1` wechseln, um an der Funktion fortzufahren.

1. Klone das Git-Repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigiere zum Repository-Verzeichnis:

```shell
cd git-playground
```

3. Liste alle Branches im Repository auf:

```shell
git branch
```

Ausgabe:

```shell
feature-1
* master
```

4. Wechsel zum Branch `feature-1`:

```shell
git checkout feature-1
```

Ausgabe:

```shell
Switched to branch 'feature-1'
```

5. Verifiziere, dass du nun auf dem Branch `feature-1` bist:

```shell
git branch
```

Ausgabe:

```shell
* feature-1
master
```
