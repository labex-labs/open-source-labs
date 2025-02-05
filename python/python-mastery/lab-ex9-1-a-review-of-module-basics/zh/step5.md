# 有问题的 reload()

创建一个实例：

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

现在，打开 `simplemod.py` 文件并将 `Spam.yow()` 的实现改为如下内容：

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('More Yow!')
```

现在，观察重新加载时会发生什么。这部分不需要重启Python。

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

注意你有两个 `Spam` 实例，但它们使用的是 `yow()` 方法的不同实现。是的，实际上两个版本的代码是同时加载的。你还会发现其他奇怪的地方。例如：

```python
>>> s
<simplemod.Spam object at 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
>>>
```

总结：对于任何重要的事情，可能最好不要依赖重新加载。如果你只是试图调试某些东西（只要你意识到它的局限性和风险），那可能还行。
