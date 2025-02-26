# Protokollierungsgrundlagen

Erstellen Sie ein Logger-Objekt.

```python
log = logging.getLogger(name)   # name ist ein String
```

Ausgeben von Protokollierungsnachrichten.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Jede Methode stellt ein unterschiedliches Schwerelevel dar._

Alle erzeugen eine formattierte Protokollierungsnachricht. `args` wird mit dem `%`-Operator verwendet, um die Nachricht zu erstellen.

```python
logmsg = message % args # In das Protokoll geschrieben
```
