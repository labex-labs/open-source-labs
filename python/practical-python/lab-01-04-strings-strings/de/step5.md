# String-Operationen

Verknüpfung, Länge, Mitgliedschaft und Replikation.

```python
# Verknüpfung (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# Länge (len)
s = 'Hello'
len(s)                  # 5

# Mitgliedschaftstest (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replikation (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
