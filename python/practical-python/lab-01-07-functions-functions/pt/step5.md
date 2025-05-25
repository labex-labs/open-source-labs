# Levantando Exceções

Para levantar uma exceção, use a instrução `raise`.

```python
raise RuntimeError('What a kerfuffle')
```

Isso fará com que o programa seja abortado com um traceback de exceção. A menos que seja capturado por um bloco `try-except`.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
