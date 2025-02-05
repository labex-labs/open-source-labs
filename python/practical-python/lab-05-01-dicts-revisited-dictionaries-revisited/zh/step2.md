# 字典（Dict）与模块（Module）

在一个模块（module）中，字典（dictionary）会保存所有的全局变量和函数。

```python
# foo.py

x = 42
def bar():
   ...

def spam():
   ...
```

如果你查看 `foo.__dict__` 或 `globals()`，就会看到这个字典。

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```
