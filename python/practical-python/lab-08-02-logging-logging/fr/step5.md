# Configuration de la journalisation

Le comportement de la journalisation est configuré séparément.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Fichier de sortie du journal
        level     = logging.INFO,   # Niveau de sortie
    )
```

En général, il s'agit d'une configuration unique au démarrage du programme. La configuration est séparée du code qui effectue les appels de journalisation.
