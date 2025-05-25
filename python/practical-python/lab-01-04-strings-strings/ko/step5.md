# 문자열 연산 (String operations)

연결, 길이, 멤버십 (membership) 및 반복.

```python
# 연결 (+) (Concatenation (+))
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# 길이 (len) (Length (len))
s = 'Hello'
len(s)                  # 5

# 멤버십 테스트 (`in`, `not in`) (Membership test (`in`, `not in`))
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# 반복 (s * n) (Replication (s * n))
rep = s * 5             # 'HelloHelloHelloHelloHello'
```
