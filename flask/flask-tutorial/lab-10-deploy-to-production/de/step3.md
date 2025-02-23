# Geheimschlüssel konfigurieren

In einer Produktionsumgebung sollten Sie den Geheimschlüssel auf einen zufälligen Wert ändern. Um einen zufälligen Geheimschlüssel zu generieren, führen Sie den folgenden Befehl aus:

```bash
# Generieren Sie einen zufälligen Geheimschlüssel
python -c 'import secrets; print(secrets.token_hex())'
```

Erstellen Sie in einem `config.py`-Datei im Instanzordner und legen Sie `SECRET_KEY` auf den generierten Wert fest.

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
