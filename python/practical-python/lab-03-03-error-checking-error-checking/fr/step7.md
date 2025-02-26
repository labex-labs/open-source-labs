# Capturer toutes les erreurs

Pour capturer n'importe quelle exception, utilisez `Exception` comme ceci :

```python
try:
  ...
except Exception:       # DANGER. Voir ci-dessous
    print('An error occurred')
```

En général, écrire du code de cette manière est une mauvaise idée car vous n'aurez aucune idée du pourquoi de son échec.
