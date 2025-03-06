# Verwenden von relativen Daten und Formatierungsoptionen

Git unterstützt auch relative Daten, was sehr praktisch ist, um schnell die jüngste Aktivität anzuzeigen.

Lassen Sie uns alle Commits der letzten 12 Wochen anzeigen:

```bash
git log --since='12 weeks ago'
```

Je nachdem, wann Sie diesen Befehl ausführen, sehen Sie möglicherweise alle Commits oder nur einige von ihnen, wenn sie in diesen Zeitraum fallen.

Andere nützliche relative Datumsformate sind:

- `"X days ago"` (vor X Tagen)
- `"X months ago"` (vor X Monaten)
- `"yesterday"` (gestern)
- `"last week"` (letzte Woche)

Lassen Sie uns versuchen, die Commits des letzten Jahres anzuzeigen:

```bash
git log --since='1 year ago'
```

Dieser Befehl zeigt alle Commits an, die im letzten Jahr vorgenommen wurden.

## Zusätzliche Formatierungsoptionen

`git log` bietet verschiedene Formatierungsoptionen, um die Ausgabe anzupassen. Hier sind einige nützliche:

1. Um ein kompakteres Log anzuzeigen, bei dem jeder Commit in einer einzigen Zeile steht:

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

Die Ausgabe sieht wie folgt aus:

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. Um die Dateien anzuzeigen, die in jedem Commit geändert wurden:

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

Dieser Befehl zeigt den Status der Dateien an, die in jedem Commit geändert wurden, was hilfreich sein kann, um zu verstehen, was geändert wurde.

Diese Formatierungsoptionen können mit Datumsfiltern kombiniert werden, um leistungsstarke Abfragen zu erstellen, die Ihnen helfen, die Historie eines Projekts effektiver zu verstehen.
