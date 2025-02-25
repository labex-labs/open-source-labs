# Capturer et gérer les exceptions

Les exceptions peuvent être capturées et gérées.

Pour les capturer, utilisez l'instruction `try - except`.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
  ...
```

Le nom `ValueError` doit correspondre au type d'erreur que vous essayez de capturer.

Il est souvent difficile de savoir exactement quels types d'erreurs peuvent survenir à l'avance, selon l'opération en cours. Pour le mieux ou pour le pire, la gestion d'exceptions est souvent ajoutée _après_ qu'un programme est tombé en panne de manière inattendue (c'est-à-dire : "oh, on avait oublié de capturer cette erreur. On devrait la gérer!").
