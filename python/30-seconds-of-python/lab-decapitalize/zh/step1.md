# 首字母转小写

编写一个函数 `decapitalize(s, upper_rest = False)`，它接受一个字符串 `s`，并返回一个首字母为小写的新字符串。该函数还应有一个可选参数 `upper_rest`，当设置为 `True` 时，会将字符串的其余部分转换为大写。

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
