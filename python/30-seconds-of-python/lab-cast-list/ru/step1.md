# Преобразование в список

Напишите функцию `cast_list(val)`, которая принимает значение в качестве аргумента и возвращает его в виде списка. Если значение уже является списком, возвращаем его без изменений. Если значение не является списком, но является итерируемым, возвращаем его в виде списка. Если значение не является итерируемым, возвращаем его в виде списка с одним элементом.

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
