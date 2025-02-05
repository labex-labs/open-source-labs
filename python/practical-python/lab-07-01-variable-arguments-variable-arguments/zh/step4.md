# 传递元组和字典

元组可以展开为可变参数。

```python
numbers = (2,3,4)
f(1, *numbers)      # 等同于 f(1,2,3,4)
```

字典也可以展开为关键字参数。

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# 等同于 f(data, color='red', delimiter=',', width=400)
```
