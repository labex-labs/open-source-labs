# Using the inspect module

Use the inspect module to get calling information about the function:

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
