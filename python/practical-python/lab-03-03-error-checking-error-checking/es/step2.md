# Excepciones

Las excepciones se utilizan para señalar errores. Para generar una excepción por tu cuenta, utiliza la instrucción `raise`.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

Para capturar una excepción, utiliza `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
