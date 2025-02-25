# 行に分割する

`split_lines(s)` という関数を作成します。この関数は、複数行の文字列 `s` を入力として受け取り、個々の行のリストを返します。関数は各行の区切り文字 (`\n`) で文字列を分割し、結果として得られる行のリストを返す必要があります。

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a','multiline','string.', '']
```
