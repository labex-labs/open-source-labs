# Opérations sur les chaînes de caractères

Concaténation, longueur, appartenance et replication.

```python
# Concaténation (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# Longueur (len)
s = 'Hello'
len(s)                  # 5

# Test d'appartenance (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replication (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
