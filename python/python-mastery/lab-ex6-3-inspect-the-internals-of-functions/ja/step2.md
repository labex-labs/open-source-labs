# inspect モジュールの使用

inspect モジュールを使用して、関数に関する呼び出し情報を取得する：

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
