# Erstellen eines neuen Repositorys

Wir haben gelernt, wie man ein vorhandenes Git-Repository klonen kann. Lassen Sie uns nun von Grund auf ein neues Git-Repository erstellen.

Öffnen Sie Ihr Terminal oder die Befehlszeile und folgen Sie den untenstehenden Schritten, um ein neues Git-Repository zu erstellen:

```bash
cd ~/project
git init my_repo
```

Dies wird ein neues Verzeichnis namens `my_repo` in Ihrem aktuellen Arbeitsverzeichnis erstellen und darin ein neues Git-Repository initialisieren.

Schauen wir uns an, was sich im Verzeichnis `my_repo` befindet:

```bash
ls -a my_repo
```

Sie sollten die folgenden Dateien und Verzeichnisse sehen:

```plaintext
. .. .git
```

Das Verzeichnis `.` und `..` sind spezielle Verzeichnisse, die das aktuelle Verzeichnis und das übergeordnete Verzeichnis darstellen.

Das Verzeichnis `.git` ist der Ort, an dem Git alle Konfigurationsdateien und die Versionsgeschichte für das Repository speichert.

Versuchen Sie, den folgenden Befehl auszuführen, um die Dateien und Verzeichnisse im Verzeichnis `.git` anzuzeigen:

```bash
ls -a my_repo/.git
```

Sie sollten die folgenden Dateien und Verzeichnisse sehen:

```plaintext
. ..  branches  config  description  HEAD  hooks  info  objects  ref
```

- Das Verzeichnis `branches` enthält Verweise auf die Branches im Repository.
- Die Datei `config` enthält die für das Repository spezifischen Konfigurationsparameter.
- Die Datei `description` enthält eine kurze Beschreibung des Repositorys.
- Die Datei `HEAD` enthält einen Verweis auf den aktuell ausgecheckten Branch.
- Das Verzeichnis `hooks` enthält Skripte, die von Git-Ereignissen ausgelöst werden können.
- Das Verzeichnis `info` enthält globale Informationsdateien.
- Das Verzeichnis `objects` enthält alle Objekte im Repository.
- Das Verzeichnis `ref` enthält Verweise auf die Commits im Repository.

Wir müssen uns für jetzt nicht um den Inhalt des Verzeichnisses `.git` kümmern. Denken Sie sich einfach daran, dass es der Ort ist, an dem Git all die Informationen über das Repository speichert.
