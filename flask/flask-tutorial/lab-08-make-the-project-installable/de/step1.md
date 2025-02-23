# Beschreibung des Projekts

Zunächst müssen wir eine `pyproject.toml`-Datei erstellen, um unser Projekt zu beschreiben und zu erklären, wie es gebaut werden soll.

Die `pyproject.toml`-Datei sollte so aussehen:

```toml
# pyproject.toml

[project]
name = "flaskr" # Name des Projekts
version = "1.0.0" # Version des Projekts
dependencies = [
    "flask", # Abhängigkeiten des Projekts
]

[build-system]
requires = ["setuptools"] # erforderliches Buildsystem
build-backend = "setuptools.build_meta" # Backend-Buildsystem
```
