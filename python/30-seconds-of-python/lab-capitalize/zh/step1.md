# 字符串首字母大写

编写一个名为 `capitalize_string(s, lower_rest=False)` 的 Python 函数，该函数接受一个字符串作为参数，并返回一个首字母大写的新字符串。该函数应具有一个可选参数 `lower_rest`，如果设置为 `True`，则将字符串的其余部分转换为小写。

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
