# 类型检查

如何判断一个对象是否为特定类型。

```python
if isinstance(a, list):
    print('a is a list')
```

检查对象是否属于多种可能类型之一。

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*注意：不要过度进行类型检查。这可能会导致代码复杂度大幅增加。通常，只有在这样做能够避免使用你代码的人犯常见错误时，你才应该进行类型检查。
