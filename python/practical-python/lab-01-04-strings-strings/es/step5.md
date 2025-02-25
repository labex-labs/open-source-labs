# Operaciones con cadenas

Concatenación, longitud, pertenencia y replicación.

```python
# Concatenación (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# Longitud (len)
s = 'Hello'
len(s)                  # 5

# Prueba de pertenencia (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replicación (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
