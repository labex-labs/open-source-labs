# Pakete vs. Module

Für größere Code-Sammlungen ist es üblich, Module in ein Paket zu organisieren.

```code
# Von diesem
pcost.py
report.py
fileparse.py

# Zu diesem
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Wählen Sie einen Namen und erstellen Sie ein oberstes Verzeichnis. `porty` im obigen Beispiel (klarerweise ist das Wählen dieses Namens der wichtigste erste Schritt).

Fügen Sie eine `__init__.py`-Datei in das Verzeichnis hinzu. Sie kann leer sein.

Legen Sie Ihre Quelltexte in das Verzeichnis ab.
