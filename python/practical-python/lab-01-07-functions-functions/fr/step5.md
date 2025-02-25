# Lèvement d'exceptions

Pour lever une exception, utilisez l'instruction `raise`.

```python
raise RuntimeError('What a kerfuffle')
```

Cela entraînera l'arrêt du programme avec une trace d'exception. Sauf si elle est capturée par un bloc `try-except`.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
