# Capturer plusieurs erreurs

Vous pouvez capturer différents types d'exceptions en utilisant plusieurs blocs `except`.

```python
try:
...
except LookupError as e:
...
except RuntimeError as e:
...
except IOError as e:
...
except KeyboardInterrupt as e:
...
```

Alternativement, si les instructions pour les gérer sont les mêmes, vous pouvez les regrouper :

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
