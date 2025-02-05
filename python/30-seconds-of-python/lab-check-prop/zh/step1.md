# 检查属性

创建一个名为 `check_prop` 的函数，它接受两个参数：`fn` 和 `prop`。`fn` 参数是一个谓词函数，将应用于字典的指定属性。`prop` 参数是一个字符串，表示谓词函数将应用于的属性名称。

`check_prop` 函数应返回一个 lambda 函数，该函数接受一个字典，并将谓词函数 `fn` 应用于指定的属性。

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
