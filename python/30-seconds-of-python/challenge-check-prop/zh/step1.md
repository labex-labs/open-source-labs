# 检查属性

## 问题

创建一个名为 `check_prop` 的函数，它接受两个参数：`fn` 和 `prop`。`fn` 参数是一个谓词函数，将应用于字典的指定属性。`prop` 参数是一个字符串，表示谓词函数将应用于的属性名称。

`check_prop` 函数应返回一个 lambda 函数，该函数接受一个字典，并将谓词函数 `fn` 应用于指定的属性。

## 示例

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```

在上面的示例中，我们创建了一个 `check_age` 函数，用于检查字典中 `age` 属性的值是否大于或等于 18。然后，我们创建了一个包含姓名和年龄属性的 `user` 字典。最后，我们将 `user` 字典作为参数调用 `check_age` 函数，由于年龄属性等于 18，所以返回 `True`。
