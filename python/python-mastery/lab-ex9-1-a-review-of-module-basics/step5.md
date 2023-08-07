# Broken reload()

Create an instance:

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

Now, go to the `simplemod.py` file and change the implementation of `Spam.yow()` to the following:

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('More Yow!')
```

Now, watch what happens on a reload. Do not restart Python for this part.

```python
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> s.yow()
'Yow!'
>>> t = simplemod.Spam()
>>> t.yow()
'More Yow!'
>>>
```

Notice how you have two instances of `Spam`, but they're using different implementations of the `yow()` method. Yes, actually both versions of code are loaded at the same time. You'll find other oddities as well. For example:

```python
>>> s
<simplemod.Spam object at 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
>>>
```

Bottom line: It's probably best not to rely on reloading for anything important. It might be fine if you're just trying to debug some things (as long as you're aware of its limitations and dangers).
