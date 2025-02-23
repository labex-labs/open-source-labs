# Installiere das Projekt

Als nächstes werden wir `pip` verwenden, um das Projekt in der virtuellen Umgebung zu installieren.

Führe den folgenden Befehl in Ihrem Terminal aus:

```none
pip install -e.
```

Dies sagt `pip`, in das aktuelle Verzeichnis nach `pyproject.toml` zu suchen und das Projekt im editierbaren oder Entwicklungsmodus zu installieren. Der editierbare Modus bedeutet, dass Sie bei Änderungen am lokalen Code nur dann erneut installieren müssen, wenn Sie die Metadaten des Projekts ändern.

Um die Installation zu überprüfen, verwenden Sie den Befehl `pip list`:

```none
pip list
```

Die Ausgabe sollte das installierte Projekt und seine Abhängigkeiten anzeigen.
