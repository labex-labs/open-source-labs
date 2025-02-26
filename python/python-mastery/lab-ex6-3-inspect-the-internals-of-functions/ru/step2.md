# Использование модуля inspect

Используйте модуль inspect, чтобы получить информацию о том, как функция вызывается:

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
