# 拆分为行

编写一个名为 `split_lines(s)` 的函数，该函数接受一个多行字符串 `s` 作为输入，并返回一个由各行组成的列表。你的函数应在每个换行符（`\n`）处拆分字符串，并返回结果行的列表。

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.', '']
```
