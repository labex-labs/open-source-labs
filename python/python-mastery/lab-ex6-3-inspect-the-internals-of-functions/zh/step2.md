# 使用 inspect 模块

使用 inspect 模块获取有关该函数的调用信息：

```python
>>> import inspect
>>> sig = inspect.signature(add)
>>> sig
<Signature (x, y)>
>>> sig.parameters
mappingproxy(OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)]))
>>> tuple(sig.parameters)
('x', 'y')
>>>
```
