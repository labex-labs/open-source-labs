# 字符串操作

拼接、长度、成员关系和复制。

```python
# 拼接 (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say'+ a          # 'Say HelloWorld'

# 长度 (len)
s = 'Hello'
len(s)                  # 5

# 成员测试 (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# 复制 (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
