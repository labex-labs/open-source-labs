# 全局变量

函数可以自由访问在同一文件中定义的全局变量的值。

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # 使用 `name` 全局变量
```

然而，函数不能修改全局变量：

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # 输出 'Dave'
```

**记住：函数中的所有赋值都是局部的。**
