# Die Verwendung des `inspect`-Moduls

Verwenden Sie das `inspect`-Modul, um Aufrufinformationen über die Funktion zu erhalten:

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
