# Les bases de la journalisation

Créer un objet journal.

```python
log = logging.getLogger(name)   # name est une chaîne de caractères
```

Émettre des messages de journal.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Chacune des méthodes représente un niveau différent de gravité._

Toutes créent un message de journal formaté. `args` est utilisé avec l'opérateur `%` pour créer le message.

```python
logmsg = message % args # Écrit dans le journal
```
