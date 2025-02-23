# Adresse bereits in Verwendung

Wenn Sie beim Versuch, den Server zu starten, eine `OSError` mit der Fehlermeldung "Address already in use" erhalten, bedeutet dies, dass ein anderer Programm bereits den Port 5000 verwendet, der der Standardport für den Entwicklungsserver ist. Sie können entweder das andere Programm identifizieren und beenden oder einen anderen Port wählen.

Um den Prozess zu identifizieren, der Port 5000 verwendet, können Sie den Befehl `netstat` oder `lsof` verwenden. Hier sind Beispiele für Linux, macOS und Windows:

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
-ano > netstat | findstr 5000
```

Sobald Sie den Prozess identifiziert haben, können Sie andere Betriebssystemtools verwenden, um ihn zu beenden. Nachdem Sie den Prozess beendet haben, sollten Sie in der Lage sein, den Entwicklungsserver ohne Probleme auszuführen.
