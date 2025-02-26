# Protokollierungskonfiguration

Das Protokollierungsverhalten wird separat konfiguriert.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Protokollausgabedatei
        level     = logging.INFO,   # Ausgabebereich
    )
```

Normalerweise ist dies eine einmalige Konfiguration beim Programmstart. Die Konfiguration ist getrennt von dem Code, der die Protokollierungsaufrufe macht.
