# 字符串转 Slug

编写一个函数 `slugify(s)`，它接受一个字符串 `s` 作为参数并返回一个 slug。该函数应执行以下操作：

1. 将字符串转换为小写并去除任何前导或尾随空格。
2. 将所有特殊字符（即任何不是字母、数字、空格、连字符或下划线的字符）替换为空字符串。
3. 将所有空格、连字符和下划线替换为单个连字符。
4. 去除任何前导或尾随连字符。

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
