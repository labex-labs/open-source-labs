# 文字列をパディングする

指定された文字で文字列を両端にパディングする関数 `pad(s: str, length: int, char: str ='') -> str` を書きます。文字列が指定された長さより短い場合です。この関数は3つのパラメータを受け取る必要があります。

- `s`: パディングする必要のある文字列
- `length`: パディングされた文字列の合計長を指定する整数
- `char`: 文字列をパディングするために使用される文字。デフォルト値は空白文字です。

この関数はパディングされた文字列を返す必要があります。

```python
from math import floor

def pad(s, length, char =''):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) #' cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
