# Lanzar excepciones

Para lanzar una excepción, use la instrucción `raise`.

```python
raise RuntimeError('What a kerfuffle')
```

Esto hará que el programa se detenga con una traza de excepción. A menos que sea capturado por un bloque `try-except`.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
