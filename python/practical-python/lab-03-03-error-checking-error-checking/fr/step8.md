# Mauvaise manière de capturer les erreurs

Voici la mauvaise manière d'utiliser les exceptions.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

Cela capture toutes les erreurs possibles et peut rendre impossible le débogage lorsque le code échoue pour une raison que vous n'attendiez absolument pas (par exemple, un module Python non installé, etc.).
