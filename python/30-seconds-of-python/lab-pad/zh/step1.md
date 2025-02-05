# 填充字符串

编写一个函数 `pad(s: str, length: int, char: str ='') -> str`，如果字符串短于指定长度，则在其两侧用指定字符进行填充。该函数应接受三个参数：

- `s`：需要填充的字符串
- `length`：指定填充后字符串的总长度的整数
- `char`：用于填充字符串的字符。默认值是一个空白字符

该函数应返回填充后的字符串。

```python
from math import floor

def pad(s, length, char =' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) #' cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
