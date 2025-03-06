# Anzeigen von Commits in einem bestimmten Datumsbereich

Jetzt lernen wir, wie man Commits anhand bestimmter Daten filtert. Git bietet zwei nützliche Optionen für diesen Zweck:

- `--since` oder `--after`: Zeigt Commits, die neuer als ein bestimmtes Datum sind
- `--until` oder `--before`: Zeigt Commits, die älter als ein bestimmtes Datum sind

Wenn wir diese Optionen kombinieren, können wir Commits innerhalb eines bestimmten Datumsbereichs anzeigen.

Lassen Sie uns alle Commits anzeigen, die zwischen dem 25. April 2023 und dem 27. April 2023 vorgenommen wurden:

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

Dieser Befehl zeigt alle Commits an, die zwischen dem 25. und dem 27. April 2023 vorgenommen wurden. Die Ausgabe sollte wie folgt aussehen:

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

Git akzeptiert viele Datumsformate, darunter:

- `"YYYY-MM-DD"` (z.B. `2023-04-25`)
- `"Month DD YYYY"` (z.B. `Apr 25 2023`)
- `"DD Month YYYY"` (z.B. `25 Apr 2023`)

Probieren Sie ein anderes Datumsformat aus, um zu sehen, ob es Commits in einem anderen Bereich gibt:

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

Dieser Befehl gibt möglicherweise keine Ergebnisse zurück, wenn es in diesem Zeitraum keine Commits gab. Das ist völlig normal.
