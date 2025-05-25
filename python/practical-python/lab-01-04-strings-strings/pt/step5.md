# Operações com Strings

Concatenação, comprimento, teste de pertinência (membership) e replicação.

```python
# Concatenação (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Comprimento (len)
s = 'Hello'
len(s)                  # 5

# Teste de pertinência (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replicação (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
