# 壊れた reload()

インスタンスを作成します。

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

次に、`simplemod.py` ファイルに移動して、`Spam.yow()` の実装を次のように変更します。

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('More Yow!')
```

次に、再読み込み時に何が起こるか見てみましょう。この部分では Python を再起動しないでください。

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

`Spam` のインスタンスが 2 つあるのに、`yow()` メソッドの異なる実装を使用していることに注意してください。実際、コードの両方のバージョンが同時に読み込まれています。他にも奇妙なことがあります。たとえば：

```python
>>> s
<simplemod.Spam object at 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
>>>
```

結論：重要なことには再読み込みを依存しない方が良いでしょう。何かをデバッグしようとしている場合には問題ないかもしれません（その制限と危険性を認識している限り）。
