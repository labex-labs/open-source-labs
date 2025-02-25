# Операции со строками

Конкатенация, длина, принадлежность и повторение.

```python
# Конкатенация (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# Длина (len)
s = 'Hello'
len(s)                  # 5

# Проверка принадлежности (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Повторение (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
