# from module import

Перезапустите Python и импортируйте выбранный символ из модуля.

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
>>>
```

Обратите внимание, как это загрузило весь модуль (обратите внимание на вывод функции `print` и на то, как переменная `x` используется).

Когда вы используете `from`, сам объект модуля не виден. Например:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
>>>
```

Убедитесь, что понимаете, что когда вы экспортируете элементы из модуля, они являются просто ссылками на имена. Например, попробуйте это и объясните:

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x is 42
>>> x = 13
>>> foo()
x is 42                   #!! Объясните, пожалуйста
>>> x
13
>>>
```
