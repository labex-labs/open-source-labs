# Split into Lines

Write a function called `split_lines(s)` that takes a multiline string `s` as input and returns a list of individual lines. Your function should split the string at each line break (`\n`) and return a list of the resulting lines.

```py
def split_lines(s):
  return s.split('\n')
```

```py
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
```
