# Sortiere Git-Branches nach Datum

Sie haben ein Git-Repository mit mehreren Branches und möchten sie nach Datum sortieren. Dadurch können Sie sehen, welche Branches kürzlich aktualisiert wurden und welche nicht. Das Sortieren von Branches nach Datum kann Ihnen auch helfen, Branches zu identifizieren, die eventuell Beachtung oder Zusammenführung benötigen.

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`.

1. Klone das Repository auf Ihren lokalen Computer:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navigiere zum Repository-Verzeichnis und konfiguriere Ihre GitHub-Identität:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Erstelle einen Branch namens `one`, modifiziere den Code und commite ihn:

```shell
git checkout -b one
touch hello.txt
git add.
git commit -m "hello.txt"
```

4. Wechsel zum Branch namens `master` und erstelle einen Branch namens `two`:

```shell
git checkout master
git checkout -b two
```

5. Um die Branches nach Datum zu sortieren, verwenden Sie folgenden Befehl:

```shell
git branch --sort=-committerdate
```

Dies zeigt eine Liste aller lokalen Branches an und sortiert sie basierend auf dem Datum ihres letzten Commits. Sie können die Pfeiltasten verwenden, um die Liste zu durchlaufen, und drücken Sie <kbd>Q</kbd>, um zu beenden.

Dies ist das fertige Ergebnis:

![sorted git branches list](../assets/challenge-sort-branches-by-date.png)
