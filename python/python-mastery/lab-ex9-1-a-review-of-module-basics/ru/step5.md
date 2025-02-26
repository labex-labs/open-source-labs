# Неправильная работа reload()

Создайте экземпляр:

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

Теперь перейдите к файлу `simplemod.py` и измените реализацию `Spam.yow()` следующим образом:

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('More Yow!')
```

Теперь посмотрите, что происходит при перезагрузке. Для этой части не перезапускайте Python.

```python
>>> importlib.reload(simplemod)
Loaded simplemod
<module'simplemod' from'simplemod.py'>
>>> s.yow()
'Yow!'
>>> t = simplemod.Spam()
>>> t.yow()
'More Yow!'
>>>
```

Обратите внимание, что у вас есть два экземпляра `Spam`, но они используют разные реализации метода `yow()`. Да, на самом деле обе версии кода загружаются одновременно. Вы также обнаружите и другие странности. Например:

```python
>>> s
<simplemod.Spam object at 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
>>>
```

В заключение: наверное, лучше не полагаться на перезагрузку для чего-то важного. Возможно, это будет нормально, если вы просто пытаетесь отладить что-то (пока вы знаете о его ограничениях и опасностях).
