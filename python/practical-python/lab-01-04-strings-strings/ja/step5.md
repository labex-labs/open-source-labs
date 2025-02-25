# 文字列操作

連結、長さ、所属判定、複製

```python
# 連結 (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# 長さ (len)
s = 'Hello'
len(s)                  # 5

# 所属判定 (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# 複製 (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
