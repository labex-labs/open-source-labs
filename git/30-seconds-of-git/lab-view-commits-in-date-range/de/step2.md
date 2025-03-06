# Erkundung des grundlegenden `git log`-Befehls

Jetzt, da wir das Repository geklont haben, lernen wir, wie man die Commit-Historie mit dem `git log`-Befehl anzeigt.

Der `git log`-Befehl zeigt eine Liste aller Commits im Repository an, beginnend mit dem neuesten. Jeder Commit-Eintrag enthält:

- Einen eindeutigen Commit-Hash (Bezeichner)
- Autorinformationen
- Datum und Uhrzeit des Commits
- Commit-Nachricht

Lassen Sie uns die grundlegende Commit-Historie anzeigen:

```bash
git log
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

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

Wenn die Ausgabe lang ist, können Sie sie wie folgt durchsuchen:

- Drücken Sie `Leertaste`, um vorwärts zu blättern.
- Drücken Sie `b`, um rückwärts zu blättern.
- Drücken Sie `q`, um die Log-Ansicht zu verlassen.

Beachten Sie, dass jeder Commit einen eindeutigen Bezeichner (die lange hexadezimale Zeichenkette), die Informationen des Autors, das Datum und die Uhrzeit des Commits sowie eine Nachricht enthält, die beschreibt, welche Änderungen vorgenommen wurden.
