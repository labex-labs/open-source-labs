# Повторная загрузка модуля

Убедитесь, что понимаете, что модули загружаются только один раз. Попробуйте повторный импорт и обратите внимание, что не видите вывода из функции `print`:

```python
>>> import simplemod
>>>
```

Попробуйте изменить значение `x` и убедитесь, что повторный импорт не имеет эффекта.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

Используйте `importlib.reload()`, если хотите принудительно перезагрузить модуль.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` — это словарь всех загруженных модулей. Посмотрите на него, удалите свой модуль и попробуйте повторный импорт.

```python
>>> sys.modules
... посмотрите на вывод...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>>
```
