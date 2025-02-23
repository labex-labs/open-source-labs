# Ausführen des Entwicklungsservers aus Python

Neben der Verwendung des Flask-Befehlszeilenbefehls können Sie auch den Entwicklungsserver aus Python-Code starten. Fügen Sie den folgenden Code am Ende Ihrer `app.py`-Datei hinzu:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Jetzt können Sie den Entwicklungsserver starten, indem Sie die `app.py`-Datei mit Python ausführen:

```bash
python app.py
```

Dadurch wird der Entwicklungsserver gestartet und Sie können auf Ihre Flask-Anwendung auf die gleiche Weise wie zuvor zugreifen.
